# encryption
## 作业详情
### 开发手册
#### 1.项目介绍
#### 2.算法实现
#### 3.gui实现
### 用户指南
#### 1.概述

1.1 项目介绍

本项目名为S-DES加密解密系统。采用轻量级的对称加密算法 S-DES（Simplified Data Encryption Standard），能够对数据的安全进行一定的保护。该算法由美国圣克拉拉大学的Edward Schaefer教授于1996年提出，适用于教育用途。

1.2 用户指南概览

本用户指南将帮助您了解如何本项目的实现原理和使用流程。



#### 2.数学基础

2.1 本项目的运行原理

本项目采用S-DES算法，明文分组为8位，主密钥分组为10位，采用两轮选代。

2.3 密钥生成

利用随机种子随机生成一个10bit密钥

2.2 加密和解密

加密算法的数学表示：<img width="100" alt="image" src="./image/加密公式.png">

解密算法的数学表示：<img width="100" alt="image" src="./image/解密公式.png">

2.4 暴力破解

遍历所有密钥，直到找到符合要求的密钥


#### 3.使用流程

3.1 准备密钥

首先，您需要一个密钥，可通过以下方式获取：

-   获取一个有效的S-DES密钥（10bit）。

-   准备要加密的明文数据。

3.2 示例：如何使用S-DES加密二进制数据

<img width="411" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/a4cc39fd-1407-4cff-95d9-4870a52ddc17">


3.3 示例：如何使用S-DES加密ASCII字符串

<img width="398" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/f475b733-2691-4357-ba3e-fca82d6895dc">


#### 4.使用S-DES解密数据

4.1 准备工作

在使用S-DES解密数据之前，您需要：

-   获取一个有效的S-DES密钥(10bit)。

-   准备要解密的密文数据。

4.2 示例：如何使用S-DES解密数据

<img width="362" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/6e292772-db74-414e-92f9-673e514c290e">


4.3 示例：如何使用S-DES解密ASCII字符串


<img width="356" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/4c975dfe-15d5-462a-ae4f-ea331c92eb1e">



#### 5.S-DES的参数设置

5.1 密钥长度

S-DES使用二进制10bit密钥

5.2 密钥扩展置换


<img width="318" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/fef85d39-0982-4caf-ae1b-fa4aaadd1f0a">



5.3 初始置换盒

<img width="300" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/0c86fd57-6c6d-4d85-b5a0-e1bbec2eef1c">


5.4 最终置换盒

<img width="296" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/5b7f688e-91d7-4023-b817-8dbfc714eb4f">


5.5 扩展置换盒

<img width="267" alt="image" src="https://github.com/Xialanshan/S_DES/assets/110965468/6e41529e-64df-4af4-a76c-2894344c0984">


5.6替换盒

SBox1:

![image](https://github.com/Xialanshan/S_DES/assets/110965468/0c301247-8a5c-44ac-aaae-5d7f54b253b6)


SBox2:

![image](https://github.com/Xialanshan/S_DES/assets/110965468/5d99bc14-fa64-4a1b-a1ae-59fbd1a6412b)


SPBox:


![image](https://github.com/Xialanshan/S_DES/assets/110965468/9323a4f5-f7e2-4ee2-8cbe-7ccab616f9e1)



#### 6.安全性和注意事项

6.1 S-DES的安全性

S-DES算法的密钥空间相对较小，不是高度安全的加密算法，不适用于处理高度敏感的数据。了解其局限性并采取必要的安全措施。

6.2 密钥管理

密钥的安全存储和分发是使用S-DES时的关键问题。确保密钥不会泄露给未授权的人员。

#### 7.常见问题解答

Q: S-DES与标准DES的区别

A: S-DES是标准DES的简化版本，主要区别在于密钥长度和轮数。标准DES使用56位密钥和16轮Feistel网络运算，更安全但也更复杂。

Q: 为什么我无法解密我的数据

A: 请检查您输入的密钥是否正确，确保与加密时使用的密钥相同。

Q: 我忘记了密钥，如何解密数据？

A: 如果您忘记了密钥，无法解密数据，因为S-DES是对称加密算法，密钥是解密的关键。

Q: 是否有S-DES的编程库或工具？

A: S-DES的编程库和工具可能存在，但不如更现代的加密标准普遍。您可以搜索相关资源或开发自己的S-DES实现。
### 测试结果
#### 第一关：基本测试
#### 第二关：交叉测试
#### 第三关：拓展功能
#### 第四关：暴力破解
#### 第五关：封闭测试
