import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Dictionary',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    my_set = {1, 2, 3}
    print(my_set)
    my_set = {1.0, "Hello", (1, 2, 3)}
    print(my_set)
    #1
    my_set1 = {1, 2, 3, 4, 3, 2}
    print(my_set1) #--> {1, 2, 3, 4}
    my_set1 = set([1, 2, 3, 2])
    print(my_set1) #--> {1, 2, 3}
    #dict vs set
    a = {}
    print(type(a)) # --> <class 'dict'>
    b = set()
    print(type(b)) # --> <class 'set'>
    #2
    my_set = {1, 3}
    print(my_set)
    my_set.add(2)
    print(my_set) # --> {1, 2, 3}
    my_set.update([2, 3, 4])
    print(my_set) # --> {1, 2, 3, 4}
    my_set.update([4, 5], {1, 6, 8}) # add list and set
    print(my_set)
    #3
    my_set3 = {1, 3, 4, 5, 6}
    print(my_set3)
    my_set3.discard(4)
    print(my_set3) # --> {1, 3, 5, 6}
    my_set3.remove(6)
    print(my_set3) #--> {1, 3, 5}
    #4
    my_set4 = set("HelloWorld")
    print(my_set4)
    print(my_set4.pop()) #--> random element
    #Set operations
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    print(A | B)
    print(A.union(B))
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    print(A & B) # {4, 5}
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    print(A - B) # {1, 2, 3}
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    print(A ^ B) # {1, 2, 3, 6, 7, 8}
    #Membership
    my_set5 = set("apple")
    print('a' in my_set5)
    print('p' not in my_set5)
    #FrozenSet
    A = frozenset([1, 2, 3, 4])
    B = frozenset([3, 4, 5, 6])
    

if __name__ == '__main__':
    main()