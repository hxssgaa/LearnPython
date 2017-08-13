# coding=utf-8
"""
字符串加密

有一种技巧可以对数据进行加密，它使用一个单词作为它的密匙。下面是它的工作原理：首先，选择一个单词作为密匙，如TRAILBLAZERS。
如果单词中包含有重复的字母，只保留第1个，其余几个丢弃。现在，修改过的那个单词死于字母表的下面，如下所示：
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T R A I L B Z E S C D F G H J K M N O P Q U V W X Y
上面其他用字母表中剩余的字母填充完整。在对信息进行加密时，信息中的每个字母被固定于顶上那行，
并用下面那行的对应字母一一取代原文的字母(字母字符的大小写状态应该保留)。因此，使用这个密匙，
Attack AT DAWN(黎明时攻击)就会被加密为Tpptad TP ITVH。
"""


class Solution(object):
    def encrypt(self, key, data):
        if not key or not data:
            return ""
        key = key.upper()
        cur_k, cur_c = 0, 0
        m, used = {}, set()
        for i in xrange(ord('A'), ord('Z') + 1):
            while cur_k < len(key) and key[cur_k] in used:
                cur_k += 1
            if cur_k < len(key):
                m[chr(i)] = key[cur_k]
                used.add(m[chr(i)])
                cur_k += 1
            else:
                while chr(ord('A') + cur_c) in used:
                    cur_c += 1
                m[chr(i)] = chr(ord('A') + cur_c)
                cur_c += 1
        return "".join((m[c.upper()].lower() if c.islower() else m[c.upper()].upper()) if c.isalpha() else c
                       for c in data)


def main():
    print Solution().encrypt(raw_input(), raw_input())


if __name__ == '__main__':
    main()
