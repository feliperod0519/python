import argparse
import csv
import io
import random
#import tabulate

def get_args():
    parser = argparse.ArgumentParser(description='WOD',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f','--file',help='CSV input file of exercises',metavar='FILE',type=argparse.FileType('rt'),default=r'C:\AutoFormation\python\projects-felipeRod\wod.csv')
    parser.add_argument('-s','--seed',help='Random seed',metavar='seed',type=int,default=1)
    parser.add_argument('-n','--num',help='Number of exercises',metavar='exercises',type=int,default=4)
    parser.add_argument('-e','--easy',help='Halve the reps',action='store_true')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def read_csv(fh):
    exercises = []
    for row in csv.DictReader(fh):
        low, high = map(int,row['reps'].split('-'))
        exercises.append((row['exercise'],low,high))
    return exercises

def main():
    args = get_args()
    print(random.seed(args.seed))
    wod = []
    exercises = read_csv(args.file)
    print(exercises)

if __name__ == '__main__':
    main()