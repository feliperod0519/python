import argparse
import os
import re

def get_args():
    parser = argparse.ArgumentParser(description='Word2Num',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', metavar='text', help='Input text or file')
    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args

def word2num(word):
    s = re.sub('[^A-Za-z0-9]','',word)
    s = str(sum(map(ord,s)))
    return s

def main():
    args = get_args()
    print(word2num(args.text))

if __name__ == '__main__':
    main()   