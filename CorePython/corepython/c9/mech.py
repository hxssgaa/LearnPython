"""
Create a simple mech browser to imitate the behaviour of filling username and password in the browser.
"""

from BeautifulSoup import BeautifulSoup as BS, SoupStrainer
from mechanize import Browser

URL_HOME = 'http://us.pycon.org/2017/'

br = Browser()

# home page
rsp = br.open(URL_HOME)
print '\n***', rsp.geturl()
print "Confirm home page has 'Log in' link; click it"
page = rsp.read()
assert 'Log in' in page, 'Log in not in page'
rsp = br.follow_link(text_regex='Log in')

# login page
print '\n***', rsp.geturl()
print 'Confirm at least a login form; submit invalid creds'
assert len(list(br.forms())) > 1, 'no forms on this page'
br.select_form(nr=0)
br.form['email'] = 'ipodtouch11@126.com'
br.form['password'] = '686713'
rsp = br.submit()

# login page, with error
print '\n***', rsp.geturl()
print 'Error due to invalid creds; resubmit w/valid creds', rsp.geturl()
assert rsp.geturl() == 'https://us.pycon.org/2017/account/login/', rsp.geturl()
page = rsp.read()
err = str(BS(page).find('div', {"class": "alert alert-error"}).text)
assert err == 'The email address and/or password you specified are not correct.', err

br.select_form(nr=0)
br.form['email'] = 'ipodtouch11@126.com'
br.form['password'] = '686713'
rsp = br.submit()
