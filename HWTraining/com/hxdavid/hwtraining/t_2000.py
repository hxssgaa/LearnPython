# coding=utf-8
"""
二维数组操作

有一个数据表格为二维数组（数组元素为int类型），行长度为ROW_LENGTH,列长度为COLUMN_LENGTH。对该表格中数据的操作可以在单个单元内，也可以对一个整行或整列进行操作，操作包括交换两个单元中的数据；插入某些行或列。
    请编写程序，实现对表格的各种操作，并跟踪表格中数据在进行各种操作时，初始数据在表格中位置的变化轨迹。

详细要求:

1.数据表规格的表示方式为“行*列”, 数据表元素的位置表示方式为[行,列]，行列均从0开始编号
2.数据表的最大规格为9行*9列，对表格进行操作时遇到超出规格应该返回错误
3.插入操作时，对m*n表格，插入行号只允许0~m，插入列号只允许0~n。超出范围应该返回错误
4.只需记录初始表格中数据的变化轨迹，查询超出初始表格的数据应返回错误
例如:  初始表格为4*4，可查询的元素范围为[0,0]~[3,3]，假设插入了第2行，数组变为5*4，查询元素[4,0]时应该返回错误
5.查询数据要求返回一个链表，链表中节点的顺序即为该查询的数据在表格中的位置变化顺序（需包含初始位置）
3 4
1 1 0 1
2
1
2 2
"""


def main():
    res = [0] * 5
    n, m = map(int, raw_input().split())
    if n < 0 or m < 0 or n > 9 or m > 9:
        res[0] = -1
    i1, j1, i2, j2 = map(int, raw_input().split())
    if i1 < 0 or i2 < 0 or j1 < 0 or j2 < 0 or i1 >= n or i2 >= n or j1 >= m or j2 >= m:
        res[1] = -1
    insert_i, insert_j = input(), input()
    if insert_i < 0 or insert_i > n:
        res[2] = -1
    if insert_j < 0 or insert_j > m:
        res[3] = -1
    cell_i, cell_j = map(int, raw_input().split())
    if cell_i < 0 or cell_i >= n or cell_j < 0 or cell_j >= m:
        res[4] = -1
    print " ".join(map(str, res))

if __name__ == '__main__':
    main()
