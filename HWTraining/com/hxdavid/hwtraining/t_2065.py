# coding=utf-8
"""
输出单向链表中倒数第k个结点

输入一个单向链表，输出该链表中倒数第k个结点，链表的倒数第0个结点为链表的尾指针。
"""


def main():
    n = input()
    data = map(int, raw_input().split())
    k = input()
    print data[n - k - 1]


if __name__ == '__main__':
    main()
