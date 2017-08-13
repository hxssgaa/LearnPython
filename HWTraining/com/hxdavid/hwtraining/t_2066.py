# coding=utf-8
"""
四则运算

输入一个算术表达式
得到计算结果

3+2*{1+2*[-4/(8-6)+7]}   ==> 25

这个题实际上就是中缀转后缀就可以了, 但是出于方便, 我们直接用built-in eval进行表达式计算, 非常方便.
"""


def main():
    print int(eval(raw_input().replace('^', '**').replace('[', '(')
                   .replace(']', ')').replace('{', '(').replace('}', ')')))


if __name__ == '__main__':
    main()
