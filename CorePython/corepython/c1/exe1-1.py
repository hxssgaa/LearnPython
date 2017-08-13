import re

patt = '(b|h)(a|i|u)t'
input_data = ['bat', 'bit', 'but', 'hat', 'hit', 'hut', 'hzt']
for d in input_data:
    m = re.match('(b|h)(a|i|u)t', d)
    print(d + ":", m.group() if m else d + ":", 'not matched')
