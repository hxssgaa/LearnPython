# coding=utf-8
"""
坐标移动

开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，
从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
"""


class Point(object):
    def __init__(self, x=None, y=None):
        self.x = x if x else 0
        self.y = y if y else 0

    def __str__(self):
        return "%s,%s" % (str(self.x), str(self.y))


class Solution(object):
    def move_coordinate(self, ops):
        p = Point()
        for op in ops:
            if not op:
                continue
            op = op.strip()
            if op[0] not in ('A', 'S', 'W', 'D'):
                continue
            try:
                direction = op[0]
                distance = int(op[1:])
                if distance >= 100 or distance <= 0:
                    continue
                if direction == 'A':
                    p.x -= distance
                elif direction == 'S':
                    p.y -= distance
                elif direction == 'W':
                    p.y += distance
                else:
                    p.x += distance
            except ValueError:
                continue
        return p


def main():
    print Solution().move_coordinate(raw_input().split(";"))


if __name__ == '__main__':
    main()
