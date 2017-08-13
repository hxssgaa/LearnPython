import re
from collections import defaultdict

month_count = defaultdict(int)
with open('redata.txt', 'r') as f:
    for l in f.readlines():
        week = re.search('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec', l).group()
        month_count[week] += 1

# You can sort the map by values like this, it's preferred.
for k in sorted(month_count, key=month_count.get, reverse=True):
    print("%s: %d" % (k, month_count[k]))
