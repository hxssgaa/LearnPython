# coding=utf-8
"""
字符串加解密

题目描述
1、对输入的字符串进行加解密，并输出。
2加密方法为：
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。
3、解密方法为加密的逆过程。

接口描述：
    实现接口，每个接口实现1个基本操作：
void Encrypt (char aucPassword[], char aucResult[])：在该函数中实现字符串加密并输出
说明：
1、字符串以\0结尾。
2、字符串最长100个字符。

int unEncrypt (char result[], char password[])：在该函数中实现字符串解密并输出
说明：
1、字符串以\0结尾。
    2、字符串最长100个字符。
"""


class Solution(object):
    def encrypt(self, s):
        def encrypt_char(c):
            if 'a' <= c <= 'z':
                if c == 'z':
                    return 'A'
                return chr(ord(c.upper()) + 1)
            elif 'A' <= c <= 'Z':
                if c == 'Z':
                    return 'a'
                return chr(ord(c.lower()) + 1)
            elif '0' <= c <= '9':
                return str((int(c) + 1) % 10)
            else:
                return c

        return "".join(map(encrypt_char, s))

    def decrypt(self, s):
        def decrypt_char(c):
            if 'a' <= c <= 'z':
                if c == 'a':
                    return 'Z'
                return chr(ord(c.upper()) - 1)
            elif 'A' <= c <= 'Z':
                if c == 'A':
                    return 'z'
                return chr(ord(c.lower()) - 1)
            elif '0' <= c <= '9':
                return str(9 if int(c) == 0 else int(c) - 1)
            else:
                return c

        return "".join(map(decrypt_char, s))


def main():
    print Solution().encrypt(raw_input())
    print Solution().decrypt(raw_input())


if __name__ == '__main__':
    main()