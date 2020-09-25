import argparse
import re

def get_args():
    parser = argparse.ArgumentParser(description='Tic-Tac-Toe',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-b','--board',help='State of the board',metavar='board',type=str,default='.' * 9)
    parser.add_argument('-p','--player',help='Player',choices='XO',metavar='player',type=str,default=None)
    parser.add_argument('-c','--cell',help='Cell 1-9',metavar='cell',type=int,choices=range(1,10),default=None)
    args = parser.parse_args()
    if any([args.player,args.cell]) and not all([args.player,args.cell]):
        parser.error('Must provide both --player and --cell')
    if not re.search('^[.XO]{9}$',args.board):
        parser.error (f'--board "{args.board}" must be 9 characters of ., X, O')
    if args.player and args.cell and args.board[args.cell - 1] in 'XO':
        parser.error(f'--cell "{args.cell}" already taken')
    return args

def format_board(board):
    cells = [str(i) if c == '.' else c for i,c in enumerate(board,1)]
    print(cells)

def main():
    args = get_args()
    board = list(args.board)
    print(board)

if __name__ == '__main__':
    main()

#lis1 = any([10, 20, 30, 40]) --> T
#lis2 = any([0, False]) --> F all values are F
#lis3 = [0, 10, 5, 15] --> T 1 value is F, the others T
#lis4 = [10, 0, False] --> T 1 is T
#lis5 = [] --> F

#l1 = ["eat","sleep","repeat"] 
#s1 = "geek" 
#obj1 = enumerate(l1) 
#obj2 = enumerate(s1) 
#print "Return type:",type(obj1) --> < type 'enumerate' >
#print list(enumerate(l1)) --> [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
#print list(enumerate(s1,2)) --> [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

#l1 = ["eat","sleep","repeat"] 
#for ele in enumerate(l1): 
#    print ele 
#print                         --->(0, 'eat')
#                                  (1, 'sleep')
#                                   (2, 'repeat')

#for count,ele in enumerate(l1,100): 
#    print count,ele 
#---------------------------> 100 eat
#                             101 sleep
#                             102 repeat
