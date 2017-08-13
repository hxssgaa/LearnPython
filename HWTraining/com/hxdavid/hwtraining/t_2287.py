# coding=utf-8
"""
图片整理

Lily上课时使用字母数字图片教小朋友们学习英语单词，
每次都需要把这些图片按照大小（ASCII码值从小到大）排列收好。请大家给Lily帮忙，通过C语言解决。
"""


class Solution(object):
    @staticmethod
    def sort_pic(pics):
        return "".join(sorted(pics.strip()))


def main():
    print Solution.sort_pic(raw_input())


if __name__ == '__main__':
    main()
