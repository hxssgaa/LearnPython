# coding=utf-8
"""
矩阵乘法计算量估算

矩阵乘法的运算量与矩阵乘法的顺序强相关。

例如：
    A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵

计算A*B*C有两种顺序：（（AB）C）或者（A（BC）），前者需要计算15000次乘法，后者只需要3500次。

编写程序计算不同的计算顺序需要进行的乘法次数

4
50 10
10 20
20 5
5 30
(A(BC)D)

这个题考察带括号的简单计算--也就是栈的使用, 由于不是后缀表达式, 因此需要不断Pop栈到(为止, 然后顺序计算其值.
"""


class Solution(object):
    def matrix_multiplication_calculation(self, n, m, exp):
        stk, temp = [], []
        cnt = 0
        for e in exp:
            if e == ')':
                temp = []
                while stk[-1] != '(':
                    temp.append(stk.pop())
                stk.pop()
                while len(temp) > 1:
                    cnt += temp[-1][0] * temp[-1][1] * temp[-2][1]
                    temp.append((temp.pop()[0], temp.pop()[1]))
                stk.append(temp[0])
            elif e == '(':
                stk.append(e)
            else:
                stk.append(m[e])
        return cnt


def main():
    n = input()
    mat = {chr(ord('A') + i): tuple(map(int, raw_input().split())) for i in xrange(n)}
    exp = raw_input()
    print Solution().matrix_multiplication_calculation(n, mat, exp)


if __name__ == '__main__':
    main()
