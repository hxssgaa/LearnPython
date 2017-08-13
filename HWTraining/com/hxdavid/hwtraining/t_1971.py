# coding=utf-8
"""
输入整型数组和排序标识，对其元素按照升序或降序进行排序

描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序
接口说明
原型：
void sortIntegerArray(Integer[] pIntegerArray, int iSortFlag);
输入参数：
    Integer[] pIntegerArray：整型数组
int  iSortFlag：排序标识：0表示按升序，1表示按降序
输出参数：
    无
返回值：
    void

"""


class Solution(object):
    def sort_data(self, data, flag):
        return sorted(data, reverse=(flag == 1))


def main():
    input()
    data = map(int, raw_input().split())
    flag = input()
    print " ".join(map(str, Solution().sort_data(data, flag)))


if __name__ == '__main__':
    main()
