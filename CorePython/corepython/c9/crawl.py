import cStringIO
import formatter
import httplib
import os
import sys
import urllib
import urlparse
from htmllib import HTMLParser


class Retriever(object):
    """
    This means this class only have url and file attributes.

    It's a method that can speeds up the accessing of these attributes.
    Because by default, object saves attributes in the __dict__, it has other costs, and many memory occupy.
    It's only useful if there are more than thousands of instances of this class.
    """
    __slots__ = ('url', 'file')

    def __init__(self, url):
        self.url, self.file = self.get_file(url)

    def get_file(self, url, default='index.html'):
        """Create usable local filename from URL"""

        parsed = urlparse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        file_path = '%s%s' % (host, parsed.path)
        # if there isn't any tailing file extensions, then choose the default index.html path.
        if not os.path.splitext(parsed.path)[1]:
            file_path = os.path.join(file_path, default)
        link_dir = os.path.dirname(file_path)
        if not os.path.isdir(link_dir):  # Plain file or directory not exist
            if os.path.exists(link_dir):  # Overwrite plain file.
                os.unlink(link_dir)
            os.makedirs(link_dir)
        return url, file_path

    def download(self):
        """Download URL to specific named file"""

        try:
            ret_val = urllib.urlretrieve(self.url, self.file)
        except (IOError, httplib.InvalidURL) as e:
            ret_val = (('*** ERROR: bad URL "%s": %s' % (self.url, e)),)
        return ret_val

    def parse_links(self):
        """Parse out the links found in downloaded HTML file"""

        f = open(self.file, 'r')
        data = f.read()
        f.close()
        # The parser class doesn't do I/O, so it takes a formatter object to handle that.
        parser = HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))
        parser.feed(data)
        parser.close()
        return parser.anchorlist


class Crawler(object):
    count = 0

    def __init__(self, url):
        self.q = [url]
        self.seen = set()
        parsed = urlparse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        self.dom = '.'.join(host.split('.')[-2:])

    def get_page(self, url, media=False):
        """Download page & parse links, add to queue if nec"""

        r = Retriever(url)
        fname = r.download()[0]
        if fname[0] == '*':
            print fname, '... skipping parse'
            return
        Crawler.count += 1
        print '\n(', Crawler.count, ')'
        print 'URL:', url
        print 'FILE:', fname
        self.seen.add(url)
        ftype = os.path.splitext(fname)[1]
        if ftype not in ('.htm', '.html'):
            return

        for link in r.parse_links():
            if link.startswith('mailto:'):
                print '... discarded, mailto link'
                continue
            if not media:
                ftype = os.path.splitext(link)[1]
                if ftype in ('.mp3', '.mp4', '.m4v', '.wav'):
                    print '... discarded, media file'
                    continue
            if not link.startswith('http://'):
                link = urlparse.urljoin(url, link)
            print '*', link,
            if link not in self.seen:
                if self.dom not in link:
                    print '... discarded not in domain'
                else:
                    if link not in self.q:
                        self.q.append(link)
                        print '... new, added to Q'
                    else:
                        print '... discarded, already in Q'
            else:
                print '... discarded, already processed'

    def go(self, media=False):
        """Process next page in queue (if any)"""
        while self.q:
            url = self.q.pop()
            self.get_page(url, media)


def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        try:
            url = raw_input('Enter starting URL: ')
        except (KeyboardInterrupt, EOFError):
            url = ''
    if not url:
        return
    if not url.startswith('http://') and \
            not url.startswith('ftp://'):
        url = 'http://%s/' % url
    robot = Crawler(url)
    robot.go(True)


if __name__ == '__main__':
    main()
