import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Dictionary',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    #maps
    nums = [1,2,3,4,5]
    print(map(square,nums)) # --> <map object at 0x000001F2B4D24790>

    for i in map(square,nums):
        print(i)
    
    print(list(map(square,nums)))

    names = ['JUAN','Felipe','CarolinaT']
    print(list(map(splicer,names)))

    #filter
    numbersToFilter = range(0,50)
    print(list(filter(check_even,numbersToFilter)))

    #lambda
    sq = lambda x: x**2
    print(list(map(lambda x: x**2,nums)))

    print(list(filter(lambda myStr:myStr%2 == 0,numbersToFilter)))
    

def splicer(myStr):
    if len(myStr)%2 == 0:
        return 'EVEN'
    else:
        return myStr[0]

def square(x):
    return x**2

def check_even(x):
    return x%2 == 0

if __name__ == '__main__':
    main()