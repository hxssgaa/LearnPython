# coding=utf-8
"""
MP3光标位置

输入说明：
1 输入歌曲数量
2 输入命令 U或者D

输出说明
1 输出当前列表
2 输出当前选中歌曲

10
UUUU
7 8 9 10
7

此题纯属逻辑题, 搞清楚逻辑即可.
"""


class Solution(object):
    def input_pre_condition(self, n, ops):
        ops = ops.upper()
        cur = 1
        sel = range(1, min(n, 4) + 1)
        for op in ops:
            cur += -1 if op == 'U' else 1
            if cur == 0:
                cur = n
                sel = range(max(1, n - 4 + 1), n + 1)
            elif cur == n + 1:
                cur = 1
                sel = range(1, min(5, n + 1))
            elif cur == sel[0] - 1:
                sel = range(sel[0] - 1, sel[-1])
            elif cur == sel[-1] + 1:
                sel = range(sel[0] + 1, sel[-1] + 2)
        return "%s\n%d" % (" ".join(map(str, sel)), cur)


def main():
    print Solution().input_pre_condition(input(), raw_input())


if __name__ == '__main__':
    main()
