import argparse
import os
import re
import random

def get_args():
    parser = argparse.ArgumentParser(description='Scramble the letters of words',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', metavar='text', help='Input text or file')
    parser.add_argument('-s', '--seed', help='Random seed', metavar='seed', type=int, default=None)
    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args

def scramble(word):
    if len(word) > 3 and re.match(r'\w+', word):
        middle = list(word[1:-1])
        random.shuffle(middle)
        word = word[0] + ''.join(middle) + word[-1]
    return word

def main():
    args = get_args()
    random.seed(args.seed)
    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    for line in args.text.splitlines():
        print(''.join(map(scramble, splitter.split(line))))

if __name__ == '__main__':
    main()