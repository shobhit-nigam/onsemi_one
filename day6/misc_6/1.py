import argparse

parser = argparse.ArgumentParser()
parser.add_argument("monday")

args = parser.parse_args()

if args.monday == 'today':
    print("in phoneix")
else:
    print("in Asia")

