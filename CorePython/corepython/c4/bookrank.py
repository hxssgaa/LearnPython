from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib import request

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'https://www.amazon.com/dp/'
ISBNS = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals'
}


def getRanking(isbn):
    opener = request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open('{0}{1}'.format(AMZN, isbn))
    data = page.read()
    page.close()
    return REGEX.findall(data.decode('utf-8'))[0]


def _showRanking(isbn):
    print('- %r ranked %s' % (ISBNS[isbn], getRanking(isbn)))


def _main():  # Only executed if this module is run directly from the command-line
    print('At', ctime(), 'on Amazon...')
    for isbn in ISBNS:
        Thread(target=_showRanking, args=(isbn,)).start()

@register
def _atexit():
    print('All Done at:', ctime())


if __name__ == '__main__':
    _main()
