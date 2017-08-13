# coding=utf-8
"""
合法IP

现在IPV4下用一个32位无符号整数来表示，一般用点分方式来显示，点将IP地址分成4个部分，每个部分为8位，表示成一个无符号整数
（因此不需要用正号出现），如10.137.17.1，是我们非常熟悉的IP地址，一个IP地址串中没有空格出现（因为要表示成一个32数字）。
现在需要你用程序来判断IP是否合法。
"""


class Solution(object):
    def is_valid_ip(self, ip_es):
        if not ip_es or len(ip_es) != 4:
            return False
        try:
            ip_es = map(int, ip_es)
            for e in ip_es:
                if e < 0 or e > 255:
                    return False
            return True
        except ValueError:
            return False


def main():
    print "YES" if Solution().is_valid_ip(raw_input().split('.')) else "NO"


if __name__ == '__main__':
    main()
