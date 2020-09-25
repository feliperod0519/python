import argparse
import os
import re

def get_args():
    parser = argparse.ArgumentParser(description='Southern fry text',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', metavar='text', help='Input text or file')
    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read()
    return args

def fry(word):
    ing_word = re.search('(.+)ing$', word)
    you = re.match('([Yy])ou$', word)
    if ing_word:
        prefix = ing_word.group(1)
        if re.search('[aeiouy]', prefix, re.IGNORECASE):
           return prefix + "in'"
        elif you:
           return you.group(1) + "'all"
    return word   

def main():
    args = get_args()
    str = 'Today is sunny. I want go to the park. I want to eat ice cream.'
    print(re.split('\.',str))
    print(re.split('(\.)',str))
    myText = '<p>My Mother has <span style="color:blue">blue</span> eyes</p>'
    print(re.split('<\w+>',myText)) #not good
    print(re.split('<.>',myText))#not good
    print(re.split('<.+>',myText))#not good
    for line in args.text.splitlines():
        print(''.join(map(fry, re.split(r'(\W+)', line.rstrip()))))

if __name__ == '__main__':
    main()

#\d digits [0123456789], [0-9]
#\s whitespace [ \t\n\r\x0b\x0c], same as string.whitespace
#\w word characteres [a-zA-Z0-9_-]

#\D Not a digit [^0123456789], [^0-9]
#\S not a whitespace [^ \t\n\r\x0b\x0c]
#\W Not word characters [^a-zA-Z0-9_-]

#re.split('\W', 'abc123!') --> ['abc123', '']
#re.split(r'(\W)', 'abc123!') --> ['abc123', '!', '']
#re.split(r'(\W)', text) --> ['Father', ',', '', ' ', 'father', ',', '', ' ', 'where', ' ', 'are', ' ','you', ' ', 'going', '?', '']

#re.split('\.''Today is sunny. I want go to the park. I want to eat ice cream')-->['Today is sunny', 'I want go to the park', 'I want to eat ice cream']
#re.split('(\.)''Today is sunny. I want go to the park. I want to eat ice cream')-->['Today is sunny', '.','I want go to the park', '.','I want to eat ice cream']

#split = '.'
#[i+split for i in re.split('\.','Today is sunny. I want go to the park. I want to eat ice cream')]
#-->['Today is sunny.' ...

#myText = '<p>My Mother has <span style="color:blue">blue</span> eyes</p>'
#