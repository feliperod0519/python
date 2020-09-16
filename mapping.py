import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Gashlycrumb', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('letter', help='Letter(s)', metavar='letter', nargs='+', type=str)
    parser.add_argument('-f','--file', help='Input file', metavar='FILE', 
                        type = argparse.FileType('rt'), default='C:\AutoFormation\python\projects-felipeRod\lines.txt')
    return parser.parse_args()

def main():
    args = get_args()
    lookup = {}
    for line in args.file:
        lookup[line[0].upper()] = line.rstrip()
    for letter in args.letter:
        if letter.upper() in lookup:
            print(lookup[letter.upper()])
        else:
            print(f'I do not know "{letter}".')

if __name__ == '__main__':
    main()

#list(range(1, 5)) --> [1, 2, 3, 4]

#List Comprehention
#h_letters = [ letter for letter in 'human' ]
#print( h_letters) --> ['h', 'u', 'm', 'a', 'n']
#Syntax: [expression for item in list]
