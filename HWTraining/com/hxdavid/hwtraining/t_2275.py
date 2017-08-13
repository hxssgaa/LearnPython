# coding=utf-8
"""
识别有效的IP地址和掩码并进行分类统计

请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。

str.zfill(width)函数是一个非常有用的技巧, 可以在指定宽度前面补0

10.70.44.68~255.254.255.0
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0
"""


class Solution(object):
    def is_valid_ip(self, ip_es):
        if not ip_es or len(ip_es) != 4:
            return False
        try:
            ip_es = map(int, ip_es)
            for e in ip_es:
                if e < 0 or e > 255:
                    return False
            return True
        except ValueError:
            return False

    def is_valid_musk(self, musk_es):
        if not self.is_valid_ip(musk_es):
            return False
        musk_es = map(int, musk_es)
        bin_str = "".join(str(bin(e))[2:].zfill(8) for e in musk_es)
        prev = bin_str[0]
        for i in range(1, len(bin_str)):
            now = bin_str[i]
            if prev == "0" and now == "1":
                return False
            prev = now
        return True

    def statistic_ip(self, e):
        """
        :type e: str
        :return: int
        """
        ip, musk = e.split("~")
        if not ip or not musk:
            return [5]
        ip, musk = ip.strip(), musk.strip()
        ip_es, musk_es = ip.split("."), musk.split(".")
        if not self.is_valid_ip(ip_es) or not self.is_valid_musk(musk_es):
            return [5]
        ip_es, musk_es = map(int, ip_es), map(int, musk_es)
        for i in range(len(ip_es)):
            ip_es[i] &= musk_es[i]
        if ip_es[0] == 10:
            return [0, 6]
        if ip_es[0] == 172 and 16 <= ip_es[1] <= 31:
            return [1, 6]
        if ip_es[0] == 192 and ip_es[1] == 168:
            return [2, 6]
        if 1 <= ip_es[0] <= 126:
            return [0]
        if 128 <= ip_es[0] <= 191:
            return [1]
        if 192 <= ip_es[0] <= 223:
            return [2]
        if 224 <= ip_es[0] <= 239:
            return [3]
        if 240 <= ip_es[0] <= 255:
            return [4]
        return [5]

    def statistic_ips(self, ips):
        """
        :type ips: [str]
        :rtype: str
        """
        sta_res = [0] * 7
        for e in ips:
            for w in self.statistic_ip(e):
                sta_res[w] += 1
        return " ".join(map(str, sta_res))


def main():
    ips = []
    for i in range(4):
        ip = raw_input()
        if not ip:
            break
        ips.append(ip.strip())
    print Solution().statistic_ips(ips)


if __name__ == '__main__':
    main()
