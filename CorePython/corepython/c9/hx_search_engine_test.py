import urllib
import urllib2
import urlparse


def get_baidu_search_url(s_word):
    return 'http://www.baidu.com/s?wd=%s&rsv_spt=1&rsv_iqid=0xfeeab34800026dd4&issp=1&f=8&rsv_bp=0&' \
           'rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=3&rsv_sug2=0&inputT=553&rsv_sug4=553' % s_word


def main():
    urllib.urlretrieve(get_baidu_search_url('hello'), "asd.html")
    # request = urllib2.Request(get_baidu_search_url('hello'), headers={"Accept": "text/html",
    #                                                                   "User-agent": "Mozilla/5.0"})
    # contents = urllib2.urlopen(request).read()
    # print contents

if __name__ == '__main__':
    main()