#raad eens

import random


def main(rondeNummer):

    
    print(f'\nRonde {rondeNummer+1}\n')

    
    randomGetal = random.randint(1,1000)

    for i in range(10):

        
        gok = int(input(' Probeer het nummer te raden als het lukt!!\n' ))
        
        
        if gok == randomGetal:
            print('Je hebt geraden goed gedaan!!!')

            
            return True

        elif gok >= (randomGetal -50) and gok <= (randomGetal +50):
            if gok >= (randomGetal -20) and gok <= (randomGetal +20):
                print('je bent heel warm!')
            else: print('je bent warm')

        if gok == randomGetal:
            print()
        elif gok <= randomGetal:
            print('HOGER!')
        elif gok >= randomGetal:
            print('LAGER!')

    return False
    gokNummer += 1

if __name__ == "__main__":


    print('welkom bij \nRaad het getal.\n U moet een getal raden tussen 1 en 1000. \n U kunt 10 keer raden. als u het binnen 10 x goed heeft gaat u door naar de volgende ronde')
    print('u kunt maximaal 20 rondes spelen.\n als u het na 10x raden niet kunt geraden word u er uit gegooid en moet je opnieuw.\n')

    
    aantalRondes = 0

    
    while aantalRondes < 20 and main(aantalRondes):
        aantalRondes += 1
    
    print(f"Je hebt {aantalRondes} rondes gewonnen")