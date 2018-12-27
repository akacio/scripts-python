#!/usr/bin/python

import sys
# by acassiO
# comverte hexadecimal em texto limpo.
# sujestao de perm de exec ao script e mova p/ /bin assim podera executar de qualquer diretorio.

if len(sys.argv) < 3:
    print('uso:')
    print('     hex2text.py -e[encode] -d[decode] "hexa/string"')

else:
    if sys.argv[1] == '-e':
        e = sys.argv[2]
        e = e.encode("HEX")
        print(e)
    elif sys.argv[1] == '-d':
        e = sys.argv[2]
        e = e.decode('HEX')
        print(e)
