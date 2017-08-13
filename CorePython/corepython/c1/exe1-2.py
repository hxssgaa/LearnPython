import re

input_data = ['David Huang', 'asd', 'z x', '1 3', 'asd g', 'Miss Moe', 'John Henry Great']
for d in input_data:
    m = re.match('[a-zA-Z]+\s[a-zA-Z]+', d)
    print(d + ":", m.group() if m else d + ":", 'not matched')
