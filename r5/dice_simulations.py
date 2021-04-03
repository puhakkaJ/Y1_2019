'''
Created on 24.9.2019

@author: jenni
'''

import random

RED = [3,3,3,3,3,6]
BLUE = [2,2,2,5,5,5]
OLIVE = [1,4,4,4,4,4]
DICE_NAMES = ["Red", "Blue", "Olive"]

def init_die():
    siemenluku = int(input("Give a seed for the dice.\n"))
    random.seed(siemenluku)

def roll(die):
    if die == 0:
        numero = random.randint(0,5)
        luku = RED[numero]
        return luku
    elif die == 1:
        numero = random.randint(0,5)
        luku = BLUE[numero]
        return luku
    elif die == 2:
        numero = random.randint(0,5)
        luku = OLIVE[numero]
        return luku

def simulate_singles(die1, die2, rolls):
    i = 0
    p = 0
    k = 0
    s = 0
    
    while i != rolls:
        if die1 == 0:
            numero = random.randint(0,5)
            luku1 = RED[numero]
            
        elif die1 == 1:
            numero = random.randint(0,5)
            luku1 = BLUE[numero]
            
        elif die1 == 2:
            numero = random.randint(0,5)
            luku1 = OLIVE[numero]
            
        if die2 == 0:
            numero = random.randint(0,5)
            luku2 = RED[numero]
            
        elif die2 == 1:
            numero = random.randint(0,5)
            luku2 = BLUE[numero]
            
        elif die2 == 2:
            numero = random.randint(0,5)
            luku2 = OLIVE[numero]
            
        if luku1 > luku2:
            p += 1
            
        if luku1 < luku2:
            k += 1
            
        elif luku1 == luku2:
            s += 1

        i += 1
            
    return p, k, s
   
def simulate_doubles(die1, die2, rolls):
    i = 0
    t = 0
    r = 0
    g = 0
    
    while i != rolls:
        if die1 == 0:
            numero1 = random.randint(0,5)
            numero2 = random.randint(0,5)
            luku3 = RED[numero1]
            luku4 = RED[numero2]
            summa1 = luku3 + luku4
            
        elif die1 == 1:
            numero1 = random.randint(0,5)
            numero2 = random.randint(0,5)
            luku3 = BLUE[numero1]
            luku4 = BLUE[numero2]
            summa1 = luku3 + luku4
            
        elif die1 == 2:
            numero1 = random.randint(0,5)
            numero2 = random.randint(0,5)
            luku3 = OLIVE[numero1]
            luku4 = OLIVE[numero2]
            summa1 = luku3 + luku4
            
        if die2 == 0:
            numero3 = random.randint(0,5)
            numero4 = random.randint(0,5)
            luku5 = RED[numero3]
            luku6 = RED[numero4]
            summa2 = luku5 + luku6
            
        elif die2 == 1:
            numero3 = random.randint(0,5)
            numero4 = random.randint(0,5)
            luku5 = BLUE[numero3]
            luku6 = BLUE[numero4]
            summa2 = luku5 + luku6
            
        elif die2 == 2:
            numero3 = random.randint(0,5)
            numero4 = random.randint(0,5)
            luku5 = OLIVE[numero3]
            luku6 = OLIVE[numero4]
            summa2 = luku5 + luku6
            
        if summa1 > summa2:
            t += 1
            
        if summa1 < summa2:
            r += 1
            
        elif summa1 == summa2:
            g += 1

        i += 1
            
    return t, r, g

def simulate_and_print_result(die1, die2, rolls, simulation_function, header):
    wins1, wins2, draws = simulation_function(die1, die2, rolls)
    print(header)
    print("Player 1 used {:s} die and won {:d} times, so {:.1f}% of the rolls.".format(DICE_NAMES[die1],wins1,wins1/rolls*100))
    print("Player 2 used {:s} die and won {:d} times, so {:.1f}% of the rolls.".format(DICE_NAMES[die2],wins2,wins2/rolls*100))
    if draws != 0:
        print("{:d} draws, so {:.2f}% of the rolls.".format(draws, draws/rolls*100))

def main():
    print("Welcome to a non-transitive dice simulation.")
    init_die()
    print("The dice:")
    print("{:d} for {:s}: {:}".format(0 ,DICE_NAMES[0], RED))
    print("{:d} for {:s}: {:}".format(1 ,DICE_NAMES[1], BLUE))
    print("{:d} for {:s}: {:}".format(2 ,DICE_NAMES[2], OLIVE))

    choice1 = int(input("Choose a die for player 1:\n"))
    choice2 = int(input("Choose a die for player 2:\n"))
    rolls  = int(input("How many rolls to simulate?\n"))
    simulate_and_print_result(choice1, choice2, rolls, simulate_singles, "Singles:")
    simulate_and_print_result(choice1, choice2, rolls, simulate_doubles, "Doubles:")

main()