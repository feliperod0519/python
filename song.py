import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser(description='Twelve Days of Christmas',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',help='Number of days to sing',metavar='days',type=int,default=12)
    parser.add_argument('-o','--outfile',help='Outfile',metavar='FILE',type=argparse.FileType('wt'),default=sys.stdout)
    args = parser.parse_args()
    if args.num not in range(1,13):
        parser.error(f'--num "{args.num}" must be between 1 and 12')
    return args

def verse(day):
    ordinal = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
                'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    gifts = ['A partridge in a pear tree.','Two turtle doves,','Three French hens,','Four calling birds,',
             'Five gold rings,','Six geese a laying,','Seven swans a swimming,','Eight maids a milking,',
             'Nine ladies dancing,','Ten lords a leaping,','Eleven pipers piping,','Twelve drummers drumming,']
    lines = [f'On the {ordinal[day - 1]} day of Christmas,','My true love gave to me,']
    lines.extend(reversed(gifts[:day]))
    if day > 1:
        lines[-1] = 'And ' + lines[-1].lower()
    return '\n'.join(lines)

def main():
    args = get_args()
    verses = map(verse, range(1, args.num + 1))
    print('\n\n'.join(verses), file=args.outfile)

if __name__ == '__main__':
    main()
#extent
#fruits = ['apple', 'banana', 'cherry']
#cars = ['Ford', 'BMW', 'Volvo']
#fruits.extend(cars)
#print(fruits) --> ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

#append
#my_list = ['geeks', 'for'] 
#my_list.append('geeks') --> ['geeks', 'for', 'geeks']

#my_list = ['geeks', 'for', 'geeks'] 
#another_list = [6, 0, 4, 1] 
#my_list.append(another_list) --> ['geeks', 'for', 'geeks', [6, 0, 4, 1]]

#reverse
#systems = ['Windows', 'macOS', 'Linux']
#systems.reverse() ---> ['Linux', 'macOS', 'Windows']

#reversed
#seqString = 'geeks'
#print(list(reversed(seqString))) --> ['s', 'k', 'e', 'e', 'g']
#seqTuple = ('g', 'e', 'e', 'k', 's')
#print(list(reversed(seqTuple))) --> ['s', 'k', 'e', 'e', 'g']
#seqRange = range(1, 5) 
#print(list(reversed(seqRange))) --> [4, 3, 2, 1]
#seqList = [1, 2, 4, 3, 5] 
#print(list(reversed(seqList))) 