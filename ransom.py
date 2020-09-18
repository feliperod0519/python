import argparse
import os
import random

def get_args():
    parser = argparse.ArgumentParser(description='Ransom Note',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', metavar='text', help='Input text or file')
    parser.add_argument('-s','--seed',help='Random seed',metavar='int',type=int,default=None)
    args = parser.parse_args()
    if os.path.isfile(args.text):
       args.text = open(args.text).read().rstrip()
    return args

def choose(char):
    return char.upper() if random.choice([0, 1]) else char.lower()

def main():
    args = get_args()
    text = args.text
    #random.seed(args.seed)
    ransom = []
    for char in text:
        ransom.append(choose(char))
    print(''.join(ransom))
    ransom = []
    for char in text:
        ransom += choose(char)
    print(''.join(ransom))
    ransom = []
    ransom = map(choose,args.text)
    print(''.join(ransom))
    ransom = []
    ransom = map(lambda c:c.upper() if random.choice([0, 1]) else c.lower(),args.text)
    print(''.join(ransom))

if __name__ == '__main__':
    main()

#Map
#def calculateSquare(n):
#    return n*n
#numbers = (1, 2, 3, 4)
#result = map(calculateSquare, numbers)
#print(result)

#Map w. lambda
#numbers = (1, 2, 3, 4)
#result = map(lambda x: x*x, numbers)
#print(result)