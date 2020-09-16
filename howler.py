
import argparse
import os
import sys

def get_args():
    parser = argparse.ArgumentParser(description='Howler (upper-case input)', 
                                     formatter_class= argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', metavar='text', type=str, help='Input string or file')                                
    parser.add_argument('-o', '--outfile', help='Output file', metavar='str', type=str, default='')
    args = parser.parse_args()
    d = os.path.dirname(args.text)
    print(d)
    if os.path.isfile(args.text):
        args.text = open(args.text).read.rstrip()
    return args

def main():
    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + '\n')
    out_fh.close()

if __name__ == '__main__':
    main()

#import os
#os.path.isfile('inputs/fox.txt')--> F
#os.path.basename()
#os.path.dirname()

#file = '/var/lib/db.txt'
#os.path.dirname(file) --> /var/lib
#os.path.basename(file) --> 'db.txt'

#file-handles
#fh = open(file)

#open(file).read() --> 'The quick brown fox jumps over the lazy dog.\n'
#text = open(file).read().rstrip() --> rtrim()

# r,w,a
# t,b --> text, bytes

#out_fh.write('this is some text\n')

#print('this is some more text', file=out_fh)
#out_fh.close()

#print("I am what I am an' I'm not ashamed.", file=open('hagrid.txt', 'wt'))

#C:\AutoFormation\python\projects-felipeRod