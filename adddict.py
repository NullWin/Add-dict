import argparse

parser = argparse.ArgumentParser(description='usage: python3 dictadd.py -f txtfile -w new word to append ')
parser.add_argument('-f')
parser.add_argument('-w')
args = parser.parse_args()
  

with open(args.f) as f:
    lines = f.readlines()
new_lines = [''.join([x.strip(), (args.w), '\n']) for x in lines]
with open('new.txt', 'w') as f:
    f.writelines(new_lines)