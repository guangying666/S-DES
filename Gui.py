import tkinter as tk
import tkinter.messagebox
from tkinter import *
import DesEncode
import ttkbootstrap as ttk

# 窗口大小
page_size = '800x500+900+450'


# 主页面
class MainPage(object):
    # 初始化页面
    def __init__(self, master_page):
        self.page = None
        self.root = master_page
        self.root.geometry(page_size)
        self.init_page()

    def init_page(self):
        self.page = tk.Frame(self.root)
        self.page.pack(fill='both', ipadx=15, ipady=10, expand=True)

        '''
        '具体布局
        '''
        # 标题
        title_label = tk.Label(self.page, text='请选择您想要进行的操作', height=3, width=200, bg='white',
                               font=('Arial', 14))
        title_label.pack()

        # 设计按钮的样式，大小和位置
        # 跳转密钥破解
        to_secret_button = ttk.Button(self.page, text='    获取随机密钥    ', style='raised',
                                      command=self.to_get_secret)
        to_secret_button.pack(padx=5, ipady=10, pady=10, anchor='center')
        # 跳转加密
        to_encrypt_button = ttk.Button(self.page, text='    加密    ', style='raised', command=self.to_encrypt)
        to_encrypt_button.pack(padx=5, ipady=10, pady=10, anchor='center')
        # 跳转解密
        to_decrypt_button = ttk.Button(self.page, text='    解密    ', style='raised', command=self.to_decrypt)
        to_decrypt_button.pack(padx=5, ipady=10, pady=10, anchor='center')
        # 跳转密钥破解
        to_crack_button = ttk.Button(self.page, text='    密钥破解    ', style='raised', command=self.to_crack_key)
        to_crack_button.pack(padx=5, ipady=10, pady=10, anchor='center')

    # 跳转
    def to_get_secret(self):
        self.page.destroy()
        GetSecret(self.root)

    def to_encrypt(self):
        self.page.destroy()
        Encrypt(self.root)

    def to_decrypt(self):
        self.page.destroy()
        Decrypt(self.root)

    def to_crack_key(self):
        self.page.destroy()
        CrackKey(self.root)


# 获取密钥页面
class GetSecret(object):
    # 初始化页面
    def __init__(self, master_page):
        self.page = None
        self.root = master_page
        self.root.geometry(page_size)
        self.init_page()

    def init_page(self):
        self.page = tk.Frame(self.root)
        self.page.pack(fill='both', ipadx=15, ipady=10, expand=True)

        '''
        '功能实现
        '''

        def get_secret():
            key = DesEncode.DesEncode().create_key()
            secret_show.delete(0.0, tk.END)
            secret_show.insert('insert', key)

        '''
        '具体布局
        '''
        # 标题
        title_label = tk.Label(self.page, text='获取随机密钥', height=3, width=200, bg='white',
                               font=('Arial', 14))
        title_label.pack()

        # 密钥显示框
        secret_show = Text(self.page, height=1, width=20)
        secret_show.pack(pady=50, anchor='center')

        # 密钥获取按钮
        get_secret_button = ttk.Button(self.page, text='获取密钥', style='raised',
                                       command=get_secret)
        get_secret_button.pack(padx=100, ipady=100, pady=10)
        get_secret_button.place(x=250, y=300)

        # 返回按钮
        back_button = ttk.Button(self.page, text='返回', style='raised',
                                 command=self.to_back)
        back_button.pack(padx=100, ipady=100, pady=10)
        back_button.place(x=450, y=300)

    # 跳转
    def to_back(self):
        self.page.destroy()
        MainPage(self.root)


# 加密页面
class Encrypt(object):
    # 初始化页面
    def __init__(self, master_page):
        self.page = None
        self.root = master_page
        self.root.geometry(page_size)
        self.plain_text = ttk.StringVar()
        self.secret_key = ttk.StringVar()
        self.init_page()

    def init_page(self):
        self.page = tk.Frame(self.root)
        self.page.pack(fill='both', ipadx=15, ipady=10, expand=True)

        '''
        '功能实现
        '''

        # 实现输入框默认提示
        def key_fun(event):
            if self.secret_key.get() == '请在此输入密钥':
                secret_key_input.delete('0', 'end')
            if self.plain_text.get() == '':
                plain_text_input.insert('insert', '请在此输入明文')

        def plain_fun(event):
            if self.plain_text.get() == '请在此输入明文':
                plain_text_input.delete('0', 'end')
            if self.secret_key.get() == '':
                secret_key_input.insert('insert', '请在此输入密钥')

        # 实现加密操作
        def encrypt():
            secret_text_output.delete('0', 'end')
            key = self.secret_key.get()
            if len(key) != 10:
                tk.messagebox.showerror('err', '密钥长度有误，请检查')
                return -1
            if not key.isdigit():
                tk.messagebox.showerror('err', '密钥含有非二进制字符，请检查')
                return -1
            for i in range(len(key)):
                if int(key[i]) not in [0, 1]:
                    tk.messagebox.showerror('err', '密钥含有非二进制字符,请重新输入')
                    return -1
            plain = self.plain_text.get()
            # secret_text = DesEncode.DesEncode().encode()
            secret_text = '这是默认密文'
            secret_text_output.insert('insert', '密文：' + secret_text)

        '''
        '具体布局
        '''
        # 标题
        title_label = tk.Label(self.page, text='加密', height=3, width=200, bg='white',
                               font=('Arial', 14))
        title_label.pack()

        # 秘钥输入
        secret_key_input = ttk.Entry(self.page, textvariable=self.secret_key)
        secret_key_input.insert('insert', '请在此输入密钥')
        secret_key_input.bind('<Button-1>', key_fun)
        secret_key_input.pack(padx=100, ipady=100, pady=10)
        secret_key_input.place(relx=0.35, rely=0.2)

        # 明文输入
        plain_text_input = ttk.Entry(self.page, textvariable=self.plain_text)
        plain_text_input.insert('insert', '请在此输入明文')
        plain_text_input.bind('<Button-1>', plain_fun)
        plain_text_input.pack(padx=100, ipady=100, pady=10)
        plain_text_input.place(relx=0.35, rely=0.3)

        # 密文输出
        secret_text_output = ttk.Text(self.page, height=5, width=30)
        secret_text_output.place(relx=0.28, rely=0.4)
        secret_text_output.insert('insert', '密文：')
        secret_text_output['fg'] = 'grey'

        # 加密按钮
        encrypt_button = ttk.Button(self.page, text='加密', style='raised',
                                    command=encrypt)
        encrypt_button.pack(padx=100, ipady=100, pady=10)
        encrypt_button.place(relx=0.45, rely=0.7)

        # 返回按钮
        back_button = ttk.Button(self.page, text='返回', style='raised',
                                 command=self.to_back)
        back_button.pack(padx=100, ipady=100, pady=10)
        back_button.place(relx=0.45, rely=0.8)

    # 跳转
    def to_back(self):
        self.page.destroy()
        MainPage(self.root)


# 解密页面
class Decrypt(object):
   # 初始化页面
    def __init__(self, master_page):
        self.page = None
        self.root = master_page
        self.root.geometry(page_size)
        self.secret_text = ttk.StringVar()
        self.secret_key = ttk.StringVar()
        self.init_page()

    def init_page(self):
        self.page = tk.Frame(self.root)
        self.page.pack(fill='both', ipadx=15, ipady=10, expand=True)

        '''
        '功能实现
        '''

        # 实现输入框默认提示
        def key_fun(event):
            if self.secret_key.get() == '请在此输入密钥':
                secret_key_input.delete('0', 'end')
            if self.secret_text.get() == '':
                secret_text_input.insert('insert', '请在此输入密文')

        def secret_fun(event):
            if self.secret_text.get() == '请在此输入密文':
                secret_text_input.delete('0', 'end')
            if self.secret_key.get() == '':
                secret_key_input.insert('insert', '请在此输入密钥')

        # 实现解密操作
        def decrypt():
            decrypt_text_output.delete('0.0', 'end')
            key = self.secret_key.get()
            if len(key) != 10:
                tk.messagebox.showerror('err', '密钥长度有误，请检查')
                return -1
            if not key.isdigit():
                tk.messagebox.showerror('err', '密钥含有非二进制字符，请检查')
                return -1
            for i in range(len(key)):
                if int(key[i]) not in [0, 1]:
                    tk.messagebox.showerror('err', '密钥含有非二进制字符,请重新输入')
                    return -1
            secret_text = self.secret_text.get()
            # decrypt_text = DesEncode.DesEncode().decode()
            decrypt_text = '这是默认解密后的明文'
            decrypt_text_output.insert('insert', '解密结果：' + decrypt_text)

        '''
        '具体布局
        '''
        # 标题
        title_label = tk.Label(self.page, text='解密', height=3, width=200, bg='white',
                               font=('Arial', 14))
        title_label.pack()

        # 秘钥输入
        secret_key_input = ttk.Entry(self.page, textvariable=self.secret_key)
        secret_key_input.insert('insert', '请在此输入密钥')
        secret_key_input.bind('<Button-1>', key_fun)
        secret_key_input.pack(padx=100, ipady=100, pady=10)
        secret_key_input.place(relx=0.35, rely=0.2)

        # 密文输入
        secret_text_input = ttk.Entry(self.page, textvariable=self.secret_text)
        secret_text_input.insert('insert', '请在此输入密文')
        secret_text_input.bind('<Button-1>', secret_fun)
        secret_text_input.pack(padx=100, ipady=100, pady=10)
        secret_text_input.place(relx=0.35, rely=0.3)

        # 解密后的明文输出
        decrypt_text_output = ttk.Text(self.page, height=5, width=30)
        decrypt_text_output.place(relx=0.28, rely=0.4)
        decrypt_text_output.insert('insert', '解密结果：')
        decrypt_text_output['fg'] = 'grey'

        # 解密按钮
        decrypt_button = ttk.Button(self.page, text='解密', style='raised',
                                    command=decrypt)
        decrypt_button.pack(padx=100, ipady=100, pady=10)
        decrypt_button.place(relx=0.45, rely=0.7)

        # 返回按钮
        back_button = ttk.Button(self.page, text='返回', style='raised',
                                 command=self.to_back)
        back_button.pack(padx=100, ipady=100, pady=10)
        back_button.place(relx=0.45, rely=0.8)

    # 跳转
    def to_back(self):
        self.page.destroy()
        MainPage(self.root)


# 密钥破解页面
class CrackKey(object):
    # 初始化页面
    def __init__(self, master_page):
        self.page = None
        self.root = master_page
        self.root.geometry(page_size)
        self.secret_text = ttk.StringVar()
        self.init_page()

    def init_page(self):
        self.page = tk.Frame(self.root)
        self.page.pack(fill='both', ipadx=15, ipady=10, expand=True)

        '''
        '功能实现
        '''

        # 实现输入框默认提示

        def secret_fun(event):
            if self.secret_text.get() == '请在此输入密文':
                secret_text_input.delete('0', 'end')

        # 实现解密操作
        def decrypt():
            decrypt_text_output.delete('0.0', 'end')
            secret_text = self.secret_text.get()
            # decrypt_text = DesEncode.DesEncode().decode()
            decrypt_text = '这是默认解密后的明文'
            decrypt_text_output.insert('insert', '解密结果：' + decrypt_text)

        '''
        '具体布局
        '''
        # 标题
        title_label = tk.Label(self.page, text='暴力破解', height=3, width=200, bg='white',
                               font=('Arial', 14))
        title_label.pack()

        # 密文输入
        secret_text_input = ttk.Entry(self.page, textvariable=self.secret_text)
        secret_text_input.insert('insert', '请在此输入密文')
        secret_text_input.bind('<Button-1>', secret_fun)
        secret_text_input.pack(padx=100, ipady=100, pady=10)
        secret_text_input.place(relx=0.35, rely=0.3)

        # 解密后的明文输出
        decrypt_text_output = ttk.Text(self.page, height=5, width=30)
        decrypt_text_output.place(relx=0.28, rely=0.4)
        decrypt_text_output.insert('insert', '解密结果：')
        decrypt_text_output['fg'] = 'grey'

        # 解密按钮
        decrypt_button = ttk.Button(self.page, text='暴力破解', style='raised',
                                    command=decrypt)
        decrypt_button.pack(padx=100, ipady=100, pady=10)
        decrypt_button.place(relx=0.42, rely=0.7)

        # 返回按钮
        back_button = ttk.Button(self.page, text='返回', style='raised',
                                 command=self.to_back)
        back_button.pack(padx=100, ipady=100, pady=10)
        back_button.place(relx=0.45, rely=0.8)

    # 跳转
    def to_back(self):
        self.page.destroy()
        MainPage(self.root)


page = ttk.Window()
page.geometry('600x400+900+450')
# 窗口名称
page.title('S-DES加密解密系统')
# 禁止调节窗口大小
page.resizable(False, False)
MainPage(page)
page.mainloop()
