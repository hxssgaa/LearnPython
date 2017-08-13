# coding=utf-8
"""
取近似值

写出一个程序，接受一个浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
"""


class Solution(object):
    def approximate_value(self, n):
        if n < 0:
            return -self.approximate_value(-n)
        return int(n + 0.5)


def main():
    print Solution().approximate_value(float(raw_input()))


if __name__ == '__main__':
    main()
