from atexit import register
from concurrent.futures import ThreadPoolExecutor
from re import compile
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
    with opener.open('{0}{1}'.format(AMZN, isbn)) as page:
        return REGEX.findall(page.read().decode('utf-8'))[0]


def _main():  # Only executed if this module is run directly from the command-line
    print('At', ctime(), 'on Amazon...')
    """
    For I/O application for which threads are more useful.
    For CPU-bound application we could use ProcessPoolExecutor instead.

    executor.map() function basically maps the given iterable collection into the given value. (map onlys maps its' key)
    and zip() functions merges two iterable collection to the tuple.
    for example zip({1:4,2:5,3:6}, {7:8,9:10,11:12})=(1,7),(2,9),(3,11)
    """
    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(ISBNS, executor.map(getRanking, ISBNS)):
            print('- %r ranked %s' % (ISBNS[isbn], ranking))


@register
def _atexit():
    print('All Done at:', ctime())


# if __name__ == '__main__':
#     _main()