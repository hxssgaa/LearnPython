# coding=utf-8
"""
从单向链表中删除指定值的节点

输入一个单向链表和一个节点的值，从单向链表中删除等于该值的节点，删除后如果链表中无节点则返回空指针。

5
2
3 2
4 3
5 2
1 4
3
"""


def main():
    n = input()
    head_val = input()
    link_list = [head_val]
    for _ in range(n - 1):
        new_val, before_val = map(int, raw_input().split())
        link_list.insert(link_list.index(before_val) + 1, new_val)
    link_list.remove(input())
    print " ".join(map(str, link_list))


if __name__ == '__main__':
    main()
