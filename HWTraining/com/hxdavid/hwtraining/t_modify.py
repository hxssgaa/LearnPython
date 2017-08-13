# coding=utf-8


class Solution(object):
    def split_str(self, s):
        if len(s) > 8:
            return '%s\n%s' % (self.split_str(s[:8]), self.split_str(s[8:]))
        return ''.join(reversed(''.join(reversed(s)).zfill(8)))


def main():
    print '\n'.join(Solution().split_str(raw_input()) for _ in xrange(2))


if __name__ == '__main__':
    main() 