# /usr/bin/env python3
# hello
import argparse

def main():
    parser = argparse.ArgumentParser(description='say hello')
    parser.add_argument('-n','--name', metavar='name', default='World', help='Nameto greet')
    args = parser.parse_args()
    print('Hello ' + args.name + '!')

if __name__ == '__main__':
    main()