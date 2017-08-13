# coding=utf-8
"""
密码强度等级

密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。
"""


class Solution(object):
    def get_pwd_security_level(self, password_str):
        """ 密码长度分数判断 """
        score = 0
        extra_condition = [False] * 4
        if len(password_str) <= 4:
            score += 5
        elif len(password_str) <= 7:
            score += 10
        else:
            score += 25

        """ 字母分数判断 """
        if all('a' <= e <= 'z' for e in password_str) or all('A' <= e <= 'Z' for e in password_str):
            score += 10
        elif password_str.upper() != password_str and password_str.lower() != password_str:
            score += 20
            extra_condition[3] = True

        """ 是否包含字母判断 """
        extra_condition[0] = len(filter(lambda x: 'A' <= x <= 'Z', password_str.upper()))

        """ 数字判断 """
        num_count = len(filter(lambda x: '0' <= x <= '9', password_str))
        if num_count > 0:
            extra_condition[1] = True
            score += 10 if num_count == 1 else 20

        """ 符号判断 """
        symbol_count = len(filter(lambda x: not ('0' <= x <= '9' or 'A' <= x <= 'Z'), password_str.upper()))
        if symbol_count > 0:
            extra_condition[2] = True
            score += 10 if symbol_count == 1 else 25

        """ 奖励 """
        if all(extra_condition):  # 大小写字母,数字和符号
            score += 5
        if all(extra_condition[:-1]):  # 字母,数字和符号
            score += 3
        if all(extra_condition[:-2]):  # 字母和数字
            score += 2

        if score >= 90:
            return 'VERY_SECURE'
        elif score >= 80:
            return 'SECURE'
        elif score >= 70:
            return 'VERY_STRONG'
        elif score >= 60:
            return 'STRONG'
        elif score >= 50:
            return 'AVERAGE'
        elif score >= 25:
            return 'WEAK'
        else:
            return 'VERY_WEAK'


def main():
    print Solution().get_pwd_security_level(raw_input())


if __name__ == '__main__':
    main()
