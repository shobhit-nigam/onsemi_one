# even data can be imported

import sys

for line in sys.path:
    print(line, "\n")

#path = "C:Users\\Documents\\terradata\\new_folder"

new_path = "/Users/shobhit/Desktop/onsemi/day1"

sys.path.append(new_path)

for line in sys.path:
    print(line, "\n")

import first

print(first.roomTemperature)
