# coding=utf-8
"""
求解立方根

•计算一个数字的立方根，不使用库函数
详细描述：
•接口说明
原型：
public static double getCubeRoot(double input)
输入:double 待求解参数
返回值:double  输入参数的立方根

"""


class Solution(object):
    def cube_root(self, num):
        return num ** (1.0 / 3)


def main():
    print '%.1f' % Solution().cube_root(float(raw_input()))


if __name__ == '__main__':
    main()
