# files
# create a folder
import os

os.mkdir("thursday")


name = 'datab.txt'
if os.path.exists(name):
    fa = open(name, 'r')
    stra = fa.read(5)
    print(stra)
else:
    print("file not found")
