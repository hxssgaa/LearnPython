# coding=utf-8
"""
【中级】单词倒排

题目描述
对字符串中的所有单词进行倒排。
说明：
1、每个单词是以26个大写或小写英文字母构成；
2、非构成单词的字符均视为单词间隔符；
3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；
4、每个单词最长20个字母；
样例输入
I am a student
样例输入
student a am I
"""
import re


class Solution(object):
    def reverse_words(self, l):
        words = re.split(r'[^a-zA-Z]+', l)
        return " ".join(reversed(filter(lambda x: x and len(x) <= 20, words)))


def main():
    print Solution().reverse_words(raw_input())


if __name__ == '__main__':
    main()
