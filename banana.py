import argparse
import os
import re

def get_args():
    parser = argparse.ArgumentParser('Apple and bananas', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', metavar='text', help='Input text or file')
    parser.add_argument('-v','--vowel',help='The vowel(s) allowed', metavar='vowel',type=str,default='a',choices=list('aeiou'))
    parser.add_argument('-m','--method',help='Choix methode', metavar='N', type=int, default=0)
    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args

def main():
    args = get_args()
    text = args.text 
    vowel = args.vowel
    method = args.method
    if method == 1:
       #do-something
       new_text = method1()
    elif method == 2:
        new_text = method2()
    elif method == 3:
        new_text = method3()
    elif method == 4:
        new_text = method4()
    elif method == 5:
        new_text = method5()
    elif method == 6:
        new_text = method6()
    elif method == 7:
        new_text = method7()
    elif method == 8:
        new_text = method8()
    else:
        new_text = []
        for char in text:
            if char in 'aeiuo':
                new_text.append(vowel)
            elif char in 'AEIOU':
                new_text.append(vowel.upper())
            else:
                new_text.append(char)
    print(''.join(new_text))

def method1():
    args = get_args()
    text = args.text 
    vowel = args.vowel
    new_text = []
    for c in text:
        if c in 'aeiou':
            new_text.append(vowel)
        elif c in 'AEIOU':
            new_text.append(vowel.upper())
        else:
            new_text.append(c)
    return ''.join(new_text)

def method2():
    args = get_args()
    text = args.text 
    vowel = args.vowel
    for c in 'aeiou':
        text = text.replace(c,vowel).replace(c.upper(),vowel.upper())
    return text

def method3():
    for char in 'aeiou':
        print(char,ord(char))
    for num in [97, 101, 105, 111, 117]:
        print(chr(num),num)
    args = get_args()
    vowel = args.vowel
    trans = str.maketrans('aeiouAEIOU',vowel*5 + vowel.upper() * 5)
    return args.text.translate(trans)

def method4():
    args = get_args()
    vowel = args.vowel
    text = [vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c for c in args.text]
    return ''.join(text)

def method5():
    args = get_args()
    vowel = args.vowel
    def new_char(c):
        return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
    text = ''.join([new_char(c) for c in args.text])
    return text

def method6():
    args = get_args()
    vowel = args.vowel
    text = map(lambda c: vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c, args.text)
    return ''.join(text)

def method7():
    args = get_args()
    vowel = args.vowel
    def new_char(c):
        return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
    return ''.join(map(new_char,args.text))

def method8():
    args = get_args()
    vowel = args.vowel
    text = args.text
    text = re.sub('[aeiou]', vowel, text)
    text = re.sub('[AEIOU]', vowel.upper(), text)
    return text

if __name__ == '__main__':
    main()


#text.replace('T', 'X')
#'876-5309'.translate(str.maketrans(jumper))
#choices=list('aeiou') in parameters

#List Comprehention
#h_letters = [ letter for letter in 'human' ]
#print( h_letters) --> ['h', 'u', 'm', 'a', 'n']
#Syntax: [expression for item in list]

#Map
#def calculateSquare(n):
#    return n*n
#numbers = (1, 2, 3, 4)
#result = map(calculateSquare, numbers)
#print(result)

#Map w. lambda
#numbers = (1, 2, 3, 4)
#result = map(lambda x: x*x, numbers)
#print(result)

#One line if statement
#<condition> ? <expression1> : <expression2> ===> <expression1> if <condition> else <expression2>
#age=15
#print('kid' if age<18 else 'adult') ---> 'kid'

#import re
#pattern = '[aeiou]'
#vowel = 'o'
#re.sub(pattern,vowel,'Apples and bananas!')