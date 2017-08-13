# coding=utf-8
"""
判断两个IP是否属于同一子网

子网掩码是用来判断任意两台计算机的IP地址是否属于同一子网络的根据。
子网掩码与IP地址结构相同，是32位二进制数，其中网络号部分全为“1”和主机号部分全为“0”。利用子网掩码可以判断两台主机是否中同一子网中。
若两台主机的IP地址分别与它们的子网掩码相“与”后的结果相同，则说明这两台主机在同一子网中。
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

    def check_net_segment(self, musk, ip1, ip2):
        if not self.is_valid_ip(musk.split(".")) or not self.is_valid_ip(ip1.split(".")) \
                or not self.is_valid_ip(ip2.split(".")):
            return 1
        musk, ip1, ip2 = map(int, musk.split(".")), map(int, ip1.split(".")), map(int, ip2.split("."))
        ip1 = [e & musk[i] for i, e in enumerate(ip1)]
        ip2 = [e & musk[i] for i, e in enumerate(ip2)]
        return 0 if ip1 == ip2 else 2


def main():
    print Solution().check_net_segment(raw_input(), raw_input(), raw_input())


if __name__ == '__main__':
    main()
