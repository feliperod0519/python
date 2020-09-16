import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Picnic game",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('item', metavar='str', nargs='+', help='Item(s) to bring')
    parser.add_argument('-s', '--sorted', action='store_true', help='Sort the items')
    return parser.parse_args()

def main():
    args = get_args()
    items = args.item
    num = len(items)
    if args.sorted:
        items.sort()
    bringing = ''
    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)
    print('You are bringing {}.'.format(bringing))

if __name__ == '__main__':
    main()

#['salad', 'chips', 'cupcakes']
#items = list()
#items = []
#type(items) --> <class 'list'>
#len(items)
#items.append('sammiches')
#items.append(['chips', 'ice cream'])--> len=2 --> ['sammiches', ['chips', 'ice cream']]
#items.extend(['chips', 'ice cream']) --> ['sammiches', 'chips', 'ice cream']
#items.insert(0, 'soda')
#indexing 0,1,2,3 -1.-2,-3,-4
#items[0:2]
#items[2:]
#items.index('chips') --> 2
#items.index('fog machine') --> error
#'chips' in items --> T
# 'fog machine' in items --> F
# items.pop() --> 'ice cream'
# items.pop(0) --> 'soda'
# items.remove('chips')

# items = ['soda', 'sammiches', 'chips', 'ice cream']
# items.sort()
# items.reverse()

# sorted([4, 2, 10, 3, 1]) --> [1, 2, 3, 4, 10]
# sorted([1, 'two', 3, 'four']) --> error

#items.sort(reverse=True)

#idx = items.index('chips')
#items[idx] = 'apples'

#', '.join(items)  --> 'soda, sammiches, chips, ice cream'
#type(', '.join(items))  --> <class 'str'>

# age = 15
#if age < 0:
# print('You are impossible.')
#elif age < 18:
# print('You are a minor.')
#else:
# print('You can vote.')
