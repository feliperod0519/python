import argparse
import re
import string

def get_args():
    parser = argparse.ArgumentParser(description='Make rhyming "words"', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word', metavar='word', help='A word to rhyme')
    return parser.parse_args()

def stemmer(word):
    word = word.lower()
    consonants = ''.join([v for v in string.ascii_lowercase if v not in 'aeiou'])
    vowels = 'aeiou'
    pattern = ('([' + consonants + ']+)?'
               '([' + vowels + '])'
               '(.*)'
              )
    match = re.match(pattern, word)
    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return(p1,p2+p3)
    else:
        return (word,'')

def main():
    args = get_args()
    l = [c for c in string.ascii_lowercase if c not in 'aeiou']
    print(l)
    lConsonants = list('bcdfghjklmnpqrstvwxyz')
    lPrefixes = ('bl br ch cl cr dr fl fr gl gr pl pr sc '
                 'sh sk sl sm sn sp st sw th tr tw thw wh wr '
                 'sch scr shr sph spl spr squ str thr').split()
    start, rest = stemmer(args.word)
    if rest:
        print('\n'.join(sorted([p + rest for p in lPrefixes if p != start])))
    else:
        print(f'Cannot rhyme "{args.word}"')
    start, rest = stemmer(args.word)
    print(start)
    print(rest)

if __name__ == '__main__':
    main()