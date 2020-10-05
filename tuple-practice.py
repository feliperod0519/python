import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Dictionary',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    #1
    my_tuple = ()
    print(my_tuple)
    my_tuple = (1, 2, 3)
    print(my_tuple)
    my_tuple = (1, "Hello", 3.4)
    print(my_tuple)
    my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
    print(my_tuple)

    #2
    my_tuple = 3, 4.6, "dog"
    print(my_tuple)
    a, b, c = my_tuple
    print(a)      # 3
    print(b)      # 4.6
    print(c)      # dog

    #3
    my_tuple = ("hello")
    print(type(my_tuple))  # <class 'str'>
    my_tuple = ("hello",)
    print(type(my_tuple))  # <class 'tuple'>
    my_tuple = "hello",
    print(type(my_tuple))  # <class 'tuple'>

    #4
    my_tuple = ('p','e','r','m','i','t')
    print(my_tuple[0])   # 'p' 
    print(my_tuple[5])   # 't'
    n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
    print(n_tuple[0][3])       # 's'
    print(n_tuple[1][1])       # 4

    #5
    my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
    print(my_tuple[-1]) #'t'

    #6
    my_tuple = ('p','r','o','g','r','a','m','i','z')
    print(my_tuple[1:4]) # ('r', 'o', 'g')

    #7
    my_tuple = (4, 2, 3, [6, 5])
    my_tuple[3][0] = 9  
    print(my_tuple) # --> (4, 2, 3, [9, 5])
    print((1, 2, 3) + (4, 5, 6))
    print(("Repeat",) * 3) #--> ('Repeat', 'Repeat', 'Repeat')

    #8
    my_tuple8 = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
    del my_tuple8 #my_tuple8 ceases to exists

    #9
    my_tuple9 = ('a', 'p', 'p', 'l', 'e',)
    print(my_tuple9.count('p'))  # Output: 2
    print(my_tuple9.index('l'))  # Output: 3

    # Membership test in tuple
    my_tuple10 = ('a', 'p', 'p', 'l', 'e',)
    print('a' in my_tuple10)
    print('b' in my_tuple10)

    #10
    # Using a for loop to iterate through a tuple
    for name in ('John', 'Kate'):
        print("Hello", name)

    #11
    print(testFunction(1,2,3,4))
    #12
    print(myfunc('Hello'))

def testFunction(*args):
    return [i for i in args if i%2 == 0]

def myfunc(s):
    i=0
    news = ''
    while i<len(s):
        if i % 2 == 0:
          news += s[i].upper()
        else:
          news += s[i].lower()
        i+=1
    return news

if __name__ == '__main__':
    main()