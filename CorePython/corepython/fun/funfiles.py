import os

print os.path.exists('redata.txt')
with open('redata.txt', 'w') as f:
    f.write('hello, world')
print os.path.exists('redata.txt')
with open('redata.txt', 'r') as f:
    for l in f:
        print l
