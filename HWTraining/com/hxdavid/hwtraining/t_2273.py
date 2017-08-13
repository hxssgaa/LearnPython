# coding=utf-8
"""
密码验证合格程序
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度超2的子串重复

如果符合要求输出：OK，否则输出NG
每行输出对应一组输入的结果；

012x01223
"""


class Solution(object):
    def is_password_ok(self, pwd):
        if not pwd or len(pwd) <= 8:
            return False
        cnt = [False] * 4
        for c in pwd:
            if 'a' <= c <= 'z':
                cnt[0] = True
            elif 'A' <= c <= 'Z':
                cnt[1] = True
            elif '0' <= c <= '9':
                cnt[2] = True
            else:
                cnt[3] = True
        if sum(int(e) for e in cnt) < 3:
            return False
        for i in range(0, len(pwd) - 5):
            for j in range(i + 3, len(pwd) - 2):
                if pwd[i:i + 3] == pwd[j:j + 3]:
                    return False
        return True


def main():
    while True:
        try:
            print "OK" if Solution().is_password_ok(raw_input()) else "NG"
        except EOFError:
            break


if __name__ == '__main__':
    main()
