import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Jump the Five",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', metavar='str', help='Input text')
    return parser.parse_args()

def main():
    args = get_args()
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}
    for char in args.text:
        print(jumper.get(char,char), end='')
    print()

if __name__ == '__main__':
    main()
    
#answers = {}
#answers = dict()
#answers['name'] = 'Sir Lancelot'
#answers --> {'name':'Sir Lancelot'}
#type(answers) --> <class 'dict'>
#answers['quest'] = 'To seek the Holy Grail'

#answers = dict(name='Sir Lancelot', quest='To seek the Holy Grail',favorite_color='blue')
#answers = {'name': 'Sir Lancelot', 'quest': 'To seek the Holy Grail','favorite_color': 'blue'}

#answers.get('quest')
#answers.get('age') --> unexisted. Returns nothing
#type(answers.get('age')) --> <class 'NoneType'>

#answers.get('age', 'NA') --> 'NA'

#answers.keys() --> dict_keys(['name', 'quest', 'favorite_color'])
#answers.values() --> dict_values(['Sir Lancelot', 'To seek the Holy Grail', 'blue'])

#for key in answers.keys():
#    print(key, answers[key])

#answers.items() --> dict_items([('name', 'Sir Lancelot'), ('quest', 'To seek the Holy Grail'),('favorite_color', 'blue')])

#for key, value in answers.items():
#    print(f'{key:15} {value}')