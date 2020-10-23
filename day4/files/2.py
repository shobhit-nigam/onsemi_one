# files
import os

name = 'datab.txt'

if os.path.exists(name):
    fa = open(name, 'r')
    stra = fa.read(5)
    print(stra)
else:
    print("file not found")
