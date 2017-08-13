import re

cpx = [str(complex(1, 2)), str(complex(-1231, 342342)), str(complex(5, 4)),
       "(-1231231-3232j)aa cxx", "(1232-asdj)", str(complex(5, 0)), str(complex(0, -4)), "1231j"]
for d in cpx:
    m = re.match('(\([+-]?\d+[+-]\d+j\))|([+-]?\d+j)', d)
    print(d + ":", m.group() if m else d + ":", 'not matched')

