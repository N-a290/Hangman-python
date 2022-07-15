import random
from os import system

def getWords():
    with open(r'./words.txt', 'r', encoding='utf-8') as f:
        possible=[w for w in f]  
    return possible

def run():
    chosenWord=random.choice(getWords()).upper().replace('\n', '')
    indexWord=dict(enumerate(chosenWord))
    lines_list=['_']*len(chosenWord)
    life=5

    while True:
        print('----Hangman Game----\n')
        printed_lines=''
        for line in lines_list:
            printed_lines+=line+' '
        print(printed_lines)
        print(f'You have {life} attempts')
        if '_' not in lines_list:
            print('You guessed the word, Congratulations!!')
            break
        elif life == 1:
            print('You have one more try')
        elif life == 0:
            print("You didn't guess the word, Game over...")
            break
        try:
            user=input('Write a letter ==> ').upper()
            if len(user)>1 or user.isdigit():
                raise ValueError
        except ValueError:
            system('clear')
            print('!-----Put only one letter-----')
        else:
            if user in chosenWord:
                for index,letter in indexWord.items():
                    if letter == user:
                        lines_list[index] = indexWord[index]
                system('clear')
            else:
                life -= 1
                system('clear')
    

if __name__=='__main__':
    run()