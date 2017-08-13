import re

m = re.match('foo', 'seafood')  # match() attempts to match the pattern to the string from the beginning.
if m:
    print("match():" + m.group())

m = re.search('foo', 'seafood')  # search() looks for the first occurrence of the pattern within the string(left-right)
if m:
    print("search():" + m.group())

m = re.search('bat|bet|bit', 'd bet a bat bit')
if m:
    print("Matching More than One String:" + m.group())

m = re.match('.end', 'bend')
if m:
    print("Matching Any Single Character (.):" + m.group())

m = re.match('[cr][23][dp][o2]', 'c3po')
if m:
    print("Creating Character Classes ([]):" + m.group())

print("Matching email:" + re.match('\w+@(\w+\.)*\w+\.com', 'nobody@www.xxx.yyy.zzz.com').group())

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print("Entire group matching:" + m.group())
print("Groups matching:" + str(m.groups()))

# This is convenient because we don't need to escape '\'
print("Use raw strings:" + re.search(r'\bthe', 'bite the dog').group())

print("findall():%s" % re.findall('car', 'carry the barcardi to the car'))

print([e.groups() for e in re.finditer(r'(th\w+) and (th\w+)', 'This and that.', re.I)])
