# coding=utf-8
"""
按字节截取字符串

实际上这个题虽然有编码问题, 但是应该注意byte数组的使用, 学会将某个字符串转换成Java对应的字符数组的形式[-128~127]
对于某一个Python str字符c 转换成Java的byte应该用
ord(c) - 256 if ord(c) > 127 else ord(c)

即:
char_array = [ord(c) - 256 if ord(c) > 127 else ord(c) for c in s]
(其中s为待转换的Python字符串)
"""


class Solution(object):
    def cut_string(self, s, length):
        """
        :type s: str
        :type length: int
        :rtype: str
        """
        index = 0
        char_array = [ord(c) - 256 if ord(c) > 127 else ord(c) for c in s]
        while index < length:
            if char_array[index] < 0 and index < length - 1:
                index += 2
            elif char_array[index] < 0 and index == length - 1:
                break
            else:
                index += 1
        return s[: index]


def main():
    print Solution().cut_string(raw_input(), input())


if __name__ == '__main__':
    main()
