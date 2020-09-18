import argparse
import re
import string

def get_args():
    parser = argparse.ArgumentParser(description='Make rhyming "words"', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word', metavar='word', help='A word to rhyme')
    return parser.parse_args()

def main():
    args = get_args()
    lConsonants = list('bcdfghjklmnpqrstvwxyz')
    lPrefixes = ('bl br ch cl cr dr fl fr gl gr pl pr sc '
                 'sh sk sl sm sn sp st sw th tr tw thw wh wr '
                 'sch scr shr sph spl spr squ str thr').split()
    #start, rest = stemmer(args.word)
    #print(start)
    #print(rest)

if __name__ == '__main__':
    main()