import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Crow's nest -- chose the correct article",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word', metavar='word', help='A word')
    return parser.parse_args()

def main():
    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')

if __name__ == '__main__':
    main()

# word = 'narwhal'
# word[0]  --> 'n'
# 'narwhal'[0] --> 'n'
# word[6] --> 'l'
# word[-1] --> 'l'
# [start:stop] 
# word[:3] --> 'nar'
# word[3:] --> 'whal'
# word.upper()
# word.isupper() --> F
# word.upper().isupper() --> T
# len('narwhal') --> 7

# word = 'octopus'
# char = word[0] --> 'o'

# type(char) --> <class 'str'>

# char == 'a' --> F
# char == 'o' --> T
# word = "hola" --> nothing ; word == "hola" --> T or F

# word = 'OCTOPUS'
# char = word[0]
# char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' --> F
# char = word[0].lower()
# char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' --> F

# 'a' in 'aeiou' --> T;  'b' in 'aeiou' --> F

#article = ''
#if word[0].lower() in 'aeiou':
#article = 'an'
#else:
#article = 'a'

#'Ahoy, Captain, {} {} off the larboard bow!'.format(article, word)
#f'Ahoy, Captain, {article} {word} off the larboard bow!'

#Positional:parser.add_argument('word', metavar='word', help='Word')

#word[0] in 'aeiouAEIOU'