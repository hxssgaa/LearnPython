# coding=utf-8
"""
查找兄弟单词

3
abc
bca
cab
abc
1
"""
from com.hxdavid.utils.utils import statistics


class Solution(object):
    @statistics(run_count=10000)
    def find_brother_word(self, d, target, index):
        """
        :type d: list[str]
        :type target: str
        :type index: int
        :rtype: str
        """
        brother = []
        sorted_target = sorted(target)
        for e in d:
            if e != target and sorted(e) == sorted_target:
                brother.append(e)
        return "%d\n%s" % (len(brother), "".join(sorted(brother)[index - 1]))


def main():
    n = input()
    d = []
    for _ in range(n):
        d.append(raw_input())
    target = raw_input()
    index = input()
    print Solution().find_brother_word(d, target, index)


if __name__ == '__main__':
    main()
