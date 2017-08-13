# coding=utf-8
"""
简单错误记录

开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
处理：
1、 记录最多8条错误记录，循环记录，对相同的错误记录（净文件名称和行号完全匹配）只记录一条，错误计数增加；
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
3、 输入的文件可能带路径，记录文件名称不能带路径。

这个题需要注意 OrderedDict 的使用, 题目要求是不超过8条, 是按照FIFO的方式的结果map不超过8条, 不要会错意思
另外一点是注意: 对于command+D的EOF标示符, 在Python中用EOFError来表示, 也就是raw_input()会抛出这个异常.
"""
from collections import OrderedDict


class Solution(object):
    def record_wrong_file_and_line(self, lines):
        m = OrderedDict()
        for l in lines:
            l = l.split()
            if not l or len(l) == 1:
                continue
            file_name, line = l[0].strip(), l[1].strip()
            file_name = file_name[file_name.rindex("\\") + 1:][-16:]
            if (file_name, line) not in m:
                if len(m) >= 8:
                    m.popitem(False)
                m[(file_name, line)] = 1
            else:
                m[(file_name, line)] += 1
        return "\n".join("%s %s %d" % (k[0], k[1], m[k]) for k in m)


def main():
    lines = []
    while True:
        try:
            line = raw_input()
            lines.append(line)
        except EOFError:
            break
    print Solution().record_wrong_file_and_line(lines)


if __name__ == '__main__':
    main()
