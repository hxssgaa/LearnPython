import base64


def main():
    s = []
    with open('/Users/hxssg/Desktop/a.txt') as f:
        for l in f:
            s.append(l)
    with open('/Users/hxssg/Desktop/b.txt', 'w') as f:
        f.write(base64.decodestring(''.join(s)))


if __name__ == '__main__':
    main()
