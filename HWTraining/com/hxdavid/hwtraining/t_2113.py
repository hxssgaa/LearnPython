# coding=utf-8
"""
整数与IP地址间的转换

原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

的每段可以看成是一个0-255的整数，需要对IP地址进行校验
10.0.3.193
167773121
"""


class Solution(object):
    def ip_to_decimal(self, ip):
        return int("".join(str(bin(int(e)))[2:].zfill(8) for e in ip.split(".")), 2)

    def decimal_to_ip(self, num):
        bin_str = str(bin(int(num)))[2:].zfill(32)
        return ".".join(str(int(bin_str[i * 8: (i + 1) * 8], 2)) for i in xrange(4))


def main():
    print Solution().ip_to_decimal(raw_input())
    print Solution().decimal_to_ip(raw_input())


if __name__ == '__main__':
    main()
