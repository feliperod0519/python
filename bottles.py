import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def verse(bottle):
    #print(f"-->{bottle}")
    next_bottle = bottle -1
    s1 = '' if bottle == 1 else 's'
    s2 = '' if next_bottle == 1 else 's'
    num_next = 'No more' if next_bottle == 0 else next_bottle
    return '\n'.join([
                      f'{bottle} bottle{s1} of beer on the wall,',
                      f'{bottle} bottle{s1} of beer,',
                      f'Take one down, pass it around,',
                      f'{num_next} bottle{s2} of beer on the wall!',
                    ])

def main():
    args = get_args()
    print('\n\n'.join(map(verse, range(args.num, 0, -1))))

if __name__ == '__main__':
    main()