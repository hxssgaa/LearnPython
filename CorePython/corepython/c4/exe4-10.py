# Download a set of html pages.
import re

import requests

from corepython.c4.mythread import MyThread

PAGES = ["www.baidu.com", "www.apple.com", "bbs.feng.com", "www.ttmeiju.com", "www.163.com", "www.zju.edu.cn"]
SEND_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Content-Type': 'text/html; charset=UTF-8',
    'Connection': 'keep-alive'
}
META_ENCODED_PATT = re.compile('<meta .*charset=["\']?([\w-]+)["\']?.+>')


def download_page(page):
    response = requests.get("http://%s" % page, headers=SEND_HEADERS)

    m = META_ENCODED_PATT.search(response.content)
    meta_encode = m.group(1) if m else 'utf-8'

    response.encoding = meta_encode
    with open("%s.html" % page.replace('.', ''), 'w') as f:
        f.write(response.text.encode(meta_encode))


def _main():
    threads = [MyThread(download_page, (p,), download_page.__name__) for p in PAGES]
    for t in threads:
        t.start()
    for i, t in enumerate(threads):
        t.join()


if __name__ == '__main__':
    _main()
