import random
from os import system

def getWords():
    with open(r'/home/garrick/personalProjects/hangmanpy/words.txt', 'r', encoding='utf-8') as f:
        possible=[w for w in f]
        
    return possible

def run():
    chosenWord=random.choice(getWords()).upper().replace('\n', '')
    indexWord=dict(enumerate(chosenWord))
    lines_list=['_']*len(chosenWord)
    
    while True:
        print('----El juego del ahorcado----\n')
        printed_lines=''
        for line in lines_list:
            printed_lines+=line+' '
        print(printed_lines)
        if '_' not in lines_list:
            print('Adivinaste la palabra, Ganaste')
            break
        try:
            user=input('Escribe una letra ==> ').upper()
            if len(user)>1 or user.isdigit():
                raise ValueError
        except ValueError:
            system('clear')
            print('Coloca solo una letra')
        else:
            if user in chosenWord:
                for index,letter in indexWord.items():
                    if letter == user:
                        lines_list[index] = indexWord[index]
                system('clear')
            else:
                system('clear')
    



if __name__=='__main__':
    run()