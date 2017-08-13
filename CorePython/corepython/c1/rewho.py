import os
import re

# Objects with context managers can be eligible to be used with "with"
with os.popen('who', 'r') as f:  # Using with statement would automatically call f.close() for you.
    for eachLine in f:
        print(re.split(r'\s\s+|\t', eachLine.rstrip()))