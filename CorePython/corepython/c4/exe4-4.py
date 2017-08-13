from time import time


def count_byte(l, bv):
    return l.count(chr(int(bv, 16)))


def merge_iter(it, cnt):
    res = []
    lst = []
    cur = 0
    for s in it:
        if cur == cnt:
            res.append("".join(lst))
            del lst[:]
            cur = 0
        lst.append(s)
        cur += 1
    res.append("".join(lst))
    return res


def _main():
    bv = "0x61"  # raw_input('Input Byte value > ')
    fname = "m.txt"  # raw_input('Filename > ')
    st = time()
    cnt = 0
    with open(fname, 'r+') as f:
        for l in f:
            cnt += count_byte(l, bv)
    end = time()
    print('byte %s occurred %d times in %s file' % (bv, cnt, fname))
    print('costs %fs time' % (end - st))


if __name__ == '__main__':
    _main()
