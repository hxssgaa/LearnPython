from HTMLParser import HTMLParser
from cStringIO import StringIO
from urllib2 import urlopen
from urlparse import urljoin

from BeautifulSoup import BeautifulSoup, SoupStrainer

URLs = (
    'http://python.org',
    'http://www.apple.com.cn'
)


def output(x):
    print '\n'.join(sorted(x))


def simpleBS(url, f):
    """
    simpleBS() - use BeautifulSoup to parse all tags to get anchors

    The result of urljoin('http://python.org', 'http://wiki.python.org') is the latter url.
    """
    parsed = BeautifulSoup(f)  # Don't minimise the line count by sacrificing readability.
    tags = parsed.findAll('a')
    links = [urljoin(url, tag['href']) for tag in tags]
    output(links)


def fasterBS(url, f):
    """fasterBS() - use BeautifulSoup to parse only anchor tags"""
    parsed = BeautifulSoup(f, parseOnlyThese=SoupStrainer('a'))
    links = [urljoin(url, x['href']) for x in parsed]
    output(links)


def htmlparser(url, f):
    """
    htmlparser() - use HTMLParser to parse anchor tags

    **Deprecated, because it's slow to keep appending attribute data
    """

    class AnchorParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return
            if not hasattr(self, 'data'):
                self.data = []
            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])

    parser = AnchorParser()
    parser.feed(f.read())
    output(urljoin(url, x) for x in parser.data)


def process(url, data):
    print '\n*** simple BS'
    simpleBS(url, data)
    data.seek(0)
    print '\n*** faster BS'
    fasterBS(url, data)
    data.seek(0)
    print '\n*** HTMLParser'
    htmlparser(url, data)
    data.seek(0)


def main():
    for url in URLs:
        f = urlopen(url)
        data = StringIO(f.read())
        f.close()
        process(url, data)


if __name__ == '__main__':
    main()
