import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Dictionary',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    my_dict = {}
    my_dict = {1: 'apple', 2: 'ball'}
    my_dict = {'name': 'John', 1: [2, 4, 3]}
    my_dict = dict({1:'apple', 2:'ball'})
    my_dict = dict([(1,'apple'), (2,'ball')])
    print(my_dict)
    #1
    my_dict1 = {'name': 'Jack', 'age': 26}
    print(my_dict1['name'])
    print(my_dict1.get('address'))
    #print(my_dict['address'])   --> Error
    #2
    my_dict2 = {'name': 'Jack', 'age': 26}
    my_dict2['age'] = 27
    print(my_dict2)
    my_dict2['address'] = 'Downtown'
    print(my_dict2)
    #3
    squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    print(squares.pop(4))
    print(squares)
    print(squares.popitem())
    print(squares)
    squares.clear()
    print(squares)
    del squares

    #4
    marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
    print(marks)
    for item in marks.items():
        print(item) # --> ['English', 'Math', 'Science']
    print(list(sorted(marks.keys())))

    #comprehension dict
    squares = {x: x*x for x in range(6)}
    print(squares)
    squares = {}
    for x in range(6):
        squares[x] = x*x
    print(squares)
    print(2 not in squares)

    #comprehension w/if cond
    odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
    print(odd_squares)
    
    #5
    squares5 = {0: 0, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}# Output: False
    print(all(squares5)) # Output: F
    print(any(squares5)) # Output: True
    print(len(squares)) # Output: 6
    print(sorted(squares)) # Output: [0, 1, 3, 5, 7, 9]

if __name__ == '__main__':
    main()