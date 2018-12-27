#!/usr/bin/python

import base64
import sys

if len(sys.argv) < 3:
    print('uso:')
    print('     script -e[encode] -d[decode] "string"')
else:
    if sys.argv[1] == '-e':
        e = sys.argv[2]
        e = base64.b64encode(e)
        print(e)
    elif sys.argv[1] == '-d':
            d = sys.argv[2]
            d = base64.b64decode(d)
            print(d)
