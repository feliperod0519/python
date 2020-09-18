import argparse
import random

def get_args():
    parser = argparse.ArgumentParser('Apple and bananas', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-a','--adjectives',help='Number of adjectives',metavar='adjectives',type=int,default=2)
    parser.add_argument('-n','--number',help='Number of insults',type=int,default=3)
    parser.add_argument('-s','--seed',help='Random seed',type=int,default=None)
    args = parser.parse_args()
    if args.adjectives<1:
        parser.error('--adjectives "{}" must be >0'.format(args.adjectives))
    if args.number<1:
        parser.error('--number "{}" must be >0'.format(args.number))
    return args

def main():
    args = get_args()
    random.seed(args.seed)
    adjectives = "bankrupt base caterwauling corrupt cullionly detestable dishonest false filthsome filthy foolish foul gross heedless indistinguishable infected insatiate irksome lascivious lecherous loathsome lubbery old peevish rascaly rotten ruinous scurilous scurvy slanderous sodden-witted thin-faced toad-spotted unmannered vile wall-eyed".strip().split()
    nous = "Judas Satan ape ass barbermonger beggar block boy braggart butt carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool gull harpy jack jolthead knave liar lunatic maw milksop minionratcatcher recreant rogue scold slave swine traitor varlet villain worm".strip().split()
    for _ in range(args.number):
        adjs = ', '.join(random.sample(adjectives,k=args.adjectives))
        print(f'You {adjs} {random.choice(nous)}!')

if __name__ == '__main__':
    main()