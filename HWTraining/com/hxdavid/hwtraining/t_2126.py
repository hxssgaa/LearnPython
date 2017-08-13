# coding=utf-8
"""
字符串合并处理

按照指定规则对输入的字符串进行处理。
详细描述：
将输入的两个字符串合并。
对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。这里的下标意思是字符在字符串中的位置。
对排训后的字符串进行操作，如果字符为‘0’——‘9’或者‘A’——‘F’或者‘a’——‘f’，则对他们所代表的16进制的数进行BIT倒序的操作，并转换为相应的大
写字符。如字符为‘4’，为0100b，则翻转后为0010b，也就是2。转换后的字符为‘2’； 如字符为‘7’，为0111b，则翻转后为1110b，也就是e。转换后的
字符为大写‘E’。

举例：输入str1为"dec"，str2为"fab"，合并为“decfab”，分别对“dca”和“efb”进行排序，排序后为“abcedf”，转换后为“5D37BF”
接口设计及说明：
/*
功能:字符串处理
输入:两个字符串,需要异常处理
输出:合并处理后的字符串，具体要求参考文档
返回:无
"""
from com.hxdavid.utils.utils import statistics


class Solution(object):
    @statistics(run_count=1000)
    def process_str(self, str1, str2):
        s = str1 + str2
        evens = sorted(filter(lambda x: x[0] % 2 == 0, [(i, e) for i, e in enumerate(s)]), key=lambda x: x[1])
        odds = sorted(filter(lambda x: x[0] % 2 == 1, [(i, e) for i, e in enumerate(s)]), key=lambda x: x[1])
        s = "".join(evens[i // 2][1] if i % 2 == 0 else odds[i // 2][1] for i in range(len(s)))

        def chr_map(c):
            if '0' <= c <= '9':
                return str(hex(int("".join(reversed(str(bin(int(c)))[2:].zfill(4))), 2)))[2:].upper()
            elif 'a' <= c <= 'f':
                return str(hex(int("".join(reversed(str(bin(10 + ord(c) - ord('a')))[2:].zfill(4))), 2)))[2:].upper()
            elif 'A' <= c <= 'F':
                return str(hex(int("".join(reversed(str(bin(10 + ord(c) - ord('A')))[2:].zfill(4))), 2)))[2:].upper()
            else:
                return c
        return "".join(map(chr_map, s))


def main():
    ss = raw_input().split()
    print Solution().process_str(ss[0], ss[1])


if __name__ == '__main__':
    main()
