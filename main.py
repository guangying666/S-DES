import random


class DesEncode:
    Ip = [2, 6, 3, 1, 4, 8, 5, 7]  # 初始置换盒
    Ip1 = [4, 1, 3, 5, 7, 2, 8, 6]  # 最终置换盒

    EpBox = [4, 1, 2, 3, 2, 3, 4, 1]  # E扩展置换
    Sbox1 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 0, 2]
    ]  # 第一个S盒替代
    Sbox2 = [
        [0, 1, 2, 3],
        [2, 3, 1, 0],
        [3, 0, 1, 2],
        [2, 1, 0, 3]
    ]  # 第二个S盒替代
    SPbox = [2, 4, 3, 1]  # P盒置换

    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]

    def bit_encode(self, s: str, rule: str = "utf-8") -> str:
        """
        将明文字符串按照rule的格式转化为01字符串
        s: 待编码字符串
        rule: 编码方案 默认utf-8
        return: 字符串对应01字符串
        """
        bytes_array = s.encode(rule)  # 首先将字符串s编码，返回一个bytes类型bytes_array
        bin_str_array = [bin(int(i))[2:].rjust(8, '0') for i in bytes_array]  # bytes_array转二进制字符串数组（每个byte8个bit）
        return ''.join(bin_str_array)  # 返回01字符串

    def group_by_8_bit(self, enter: str, is_bit_string: bool = False) -> list:
        """
        将输入的字符串转换为二进制形式，并8位为一组进行分割
        enter:要转换的字符串
        is_bit_string: 是否为bit字符串，如果是比特字符串，则填True，否则False
        return: 8倍整数的字符串数组
        """
        result = []
        bit_string = enter if is_bit_string else self.bit_encode(enter)

        for i in range(len(bit_string) // 8):
            result.append(bit_string[i * 8: i * 8 + 8])

        return result

    # 置换函数
    def permute(self, input_str, table) -> str:
        output_str = ""
        for bit_position in table:
            output_str += input_str[bit_position - 1]
        return output_str

    # 生成10位随机密钥
    def create_key(self) -> str:
        str_key = ""
        for i in range(10):
            key = random.randint(0, 1)
            str_key += str(key)
        return str(str_key)

    # 左移函数
    def lelf_move(self, key, n) -> list:
        # 将密钥分成两段并循环左移 n 位
        left_half = key[:5]
        right_half = key[5:]
        shifted_left = left_half[n:] + left_half[:n]
        shifted_right = right_half[n:] + right_half[:n]
        return shifted_left + shifted_right

    # 子密钥生成
    def child_key(self, k, p10, p8) -> tuple:
        # 执行 P10 置换
        p10_key = self.permute(k, p10)
        # 对结果进行左移操作和P8置换，得到 K1
        k1 = self.permute(self.lelf_move(p10_key, 1), p8)
        # 再次对上一步结果进行左移操作h和P8置换，得到 K2
        k2 = self.permute(self.lelf_move(self.lelf_move(p10_key, 1), 2), p8)
        return k1, k2

    # f函数
    def F_fuction(self, right_half, k) -> str:
        # 对右半部分进行 E/P 扩展置换
        expanded = self.permute(right_half, self.EpBox)
        # 对结果与 K1 进行异或操作
        xored = '{0:08b}'.format(int(expanded, 2) ^ int(k, 2))
        # 将结果分为两组，并根据 S-box 进行替换
        s0_input = xored[:4]
        s1_input = xored[4:]
        # 根据S盒规则行列查找
        s0_row = int(s0_input[0] + s0_input[-1], 2)
        s0_col = int(s0_input[1:-1], 2)
        s1_row = int(s1_input[0] + s1_input[-1], 2)
        s1_col = int(s1_input[1:-1], 2)
        # 转换为2位二进制数
        s0_output = f"{self.Sbox1[s0_row][s0_col]:02b}"
        s1_output = f"{self.Sbox2[s1_row][s1_col]:02b}"
        # 对两个输出串进行 P4 置换得到最终结果
        s_output = s0_output + s1_output
        return self.permute(s_output, self.SPbox)

    # 加密函数
    def encode(self, p, childk1, childk2) -> str:
        # 执行初始置换
        p = self.permute(p, self.Ip)
        l0 = p[:4]
        r0 = p[4:]
        l1 = r0
        # 第一轮的P4
        f_result = self.F_fuction(r0, childk1)
        # p41和L0异或,结果转换为4位二进制数（如果不足4位，左边会用0填充）
        r1 = f"{int(l0, 2) ^ int(f_result, 2):04b}"
        # 第二轮的P4
        f_result = self.F_fuction(r1, childk2)
        # p42和L1异或,结果转换为4位二进制数（如果不足4位，左边会用0填充）
        r2 = f"{int(l1, 2) ^ int(f_result, 2):04b}"
        # 逆置换并返回结果(左边R2右边R1)
        return self.permute(r2 + r1, self.Ip1)

    # 解密函数
    def decode(self, c, childk1, childk2) -> str:
        # 执行初始置换
        c = self.permute(c, self.Ip)
        r2 = c[:4]
        l2 = c[4:]
        # 第一轮的P4
        f_result = self.F_fuction(l2, childk2)
        # p41和R2异或,结果转换为4位二进制数（如果不足4位，左边会用0填充）
        l1 = f"{int(r2, 2) ^ int(f_result, 2):04b}"
        # 第二轮的P4
        f_result = self.F_fuction(l1, childk1)
        # p42和R1异或,结果转换为4位二进制数（如果不足4位，左边会用0填充）
        r1 = f'{int(l2, 2) ^ int(f_result, 2):04b}'
        # 逆置换并返回明文
        return self.permute(r1 + l1, self.Ip1)

    # 针对字符串的加密函数
    def str_encode(self, str_list) -> tuple:
        res_list = []
        p = str_list
        key = d1.create_key()
        ch_key = d1.child_key(key, d1.P10, d1.P8)
        for i in range(len(p)):
            c = self.encode(p[i], childk1=ch_key[0], childk2=ch_key[1])
            res_list.append(c)
        return res_list, ch_key  # 返回本次加密的密文数组以及加密所用的子密钥

    # 针对字符串的解密函数
    def str_decode(self, str_list, ch_key1, ch_key2) -> list:
        res_list = []
        c = str_list
        for i in range(len(c)):
            p = self.decode(c[i], childk1=ch_key1, childk2=ch_key2)
            res_list.append(p)
        return res_list

    # 将二进制的字符串数组变成输入的明文字符串
    def str_to_word(self, p_list):
        temp_str = ""
        for i in range(len(p_list)):
            temp_str += p_list[i]
        ascii_string = ''.join(chr(int(temp_str[i:i + 8], 2)) for i in range(0, len(temp_str), 8))
        return ascii_string


if __name__ == '__main__':
    num1 = "hLLLL"
    d1 = DesEncode()
    num1 = d1.group_by_8_bit(num1)
    print("转换为二进制的字符串数组"+str(num1))
    num2 = d1.str_encode(num1)
    print(num2)
    print("加密后的字符串数组: " + str(num2[0])+"所使用的子密钥1为"+str(num2[1][0])+",子密钥2为"+str(num2[1][1]))
    num3 = d1.str_decode(num2[0], num2[1][0], num2[1][1])
    print("解密后的二进制字符串数组为"+str(num3))
    print(d1.str_to_word(num3))




