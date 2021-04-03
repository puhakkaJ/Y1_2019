'''
Created on 7.10.2019

@author: jenni
'''

import random

SPADE = "\u2660"
HEART = "\u2661"
DIAMOND = "\u2662"
CLUB = "\u2663"

SUITS = [SPADE,HEART,DIAMOND,CLUB]
FACES = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
FACES_AS_VALUES = {"2":2, "3":3, "4":4,"5":5,"6":6,"7":7,"8":8,\
                   "9":9,"10":10,"J":10,"Q":10,"K":10,"A":[11,1]}
pelaajak = []
jakajak = []

def initialize_random():
    seed = int(input("Give seed for random generator:\n"))
    random.seed(seed)

def initialize_deck():
    deck = []
    for face in FACES:
        for suit in SUITS:
            card = [face,suit]
            deck.append(card)
    return deck

def shuffle_and_deal(deck):
    random.shuffle(deck)
    
    pelaajak.append(deck.pop())
    jakajak.append(deck.pop())
    pelaajak.append(deck.pop())
    jakajak.append(deck.pop())
    
    return deck, pelaajak, jakajak
    
def hand_value(hand):
    done = False
    summa = 0
    summa1 = 0
    summalista = []
    
    for arvo in hand:
        if arvo[0] != "A":  
            summalista.append(FACES_AS_VALUES[arvo[0]])
            summa += FACES_AS_VALUES[arvo[0]]
        
        if arvo[0] == "A":
            summalista.append(11)
            summa += 11

    if 11 in summalista:
        if summa > 21:
            while not done:
                i = summalista.index(11)
                summalista[i] = 1
                
                summa1 = 0
                for arvo in summalista:
                    summa1 += arvo 
            
                if summa1 <= 21:
                    summa = summa1
                    break
                
                if 11 not in summalista:
                    summa = summa1
                    break
    
    return summa

def print_hand_and_value(name,hand):
    summa = hand_value(hand)

    rivi = ''
    n = 0
    
    while n != len(hand): 
        kuvio = hand[n][1]
        
        if hand[n][0] == "A" or "Q" or "J" or "K":
            luku = hand[n][0]
            osa = ("{:>s}{:<s}" .format(luku,kuvio))
        
        else:
            luku = int(hand[n][0])
            osa = ("{:>d}{:<s}" .format(luku,kuvio))
        
        rivi += osa + " "

        n += 1
    
    print("--------------")
    print(name ,"hand:")
    print(rivi)
    print("Value:", summa)
    print("--------------")
    
def print_dealer_start_hand(hand):    
    kuvio = hand[1][1]
        
    if hand[1][0] == "A" or "Q" or "J" or "K":
        luku = hand[1][0]
        
        print("--------------")
        print("Dealer hand:")
        print("XX {:>s}{:<s} ". format(luku,kuvio))
        print("--------------")
        
    else:
        luku = int(hand[1][0])
            
        print("--------------")
        print("Dealer hand:")
        print("XX {:>d}{:<s} ". format(luku,kuvio))
        print("--------------")
    
def print_dealer_whole_hand(hand,summa):
    rivi = ''
    n = 0
    
    while n != len(hand): 
        kuvio = hand[n][1]
        
        if hand[n][0] == "A" or "Q" or "J" or "K":
            luku = hand[n][0]
            osa = ("{:>s}{:<s}" .format(luku,kuvio))
        
        else:
            luku = int(hand[n][0])
            osa = ("{:>d}{:<s}" .format(luku,kuvio))
        
        rivi += osa + " "
        
        n += 1
    
    print("--------------")
    print("Dealer hand:")
    print(rivi)
    print("Value:", summa)
    print("--------------")

def main():
    done1 = False
    done2 = False
    n = 0
    p = 0
    
    print("Welcome to play the Twenty-One card Game!")
    print("Try to get closer to 21 than the dealer without going over 21.")
    initialize_random()
    deck = initialize_deck()
    deck, pelaajak, jakajak = shuffle_and_deal(deck)
    
    while not done1:
        if n == 0:
            summa1 = hand_value(pelaajak)
            print_dealer_start_hand(jakajak)
            name = 'Your'
            print_hand_and_value(name,pelaajak)
            
            if summa1 == 21:
                print("Let's continue onto draws.")
                rivi = input("You have a natural 21. Press enter to continue onto dealer draws.\n")
                rivi = str(rivi)
                break   
        
            print("Let's continue onto draws.")
        rivi = input("Do you want to draw another card? (y/n)\n")
        vastaus = str(rivi)
        
        if vastaus == "y":
            print("You draw another card.")
            pelaajak.append(deck.pop())
            summa1 = hand_value(pelaajak)
            print_hand_and_value(name,pelaajak)
    
        if summa1 == 21:
            print("You reached 21! Can't draw anymore now.")
            rivi = input("Press enter to continue.\n")
            rivi = str(rivi)
            break
            
        if summa1 > 21:
            print("You went bust. Dealer won.")
            break
            
        if vastaus == "n":   
            break   
            
        n += 1
        
    if summa1 <= 21:
        while not done2:
            if p == 0:  
                print("Dealer opens their hand.")
                summa2 = hand_value(jakajak)
                print_dealer_whole_hand(jakajak,summa2)
                
                if summa2 >= 17 and summa2 < 21:
                    rivi = input("Press enter to see final hands.\n")
                    rivi = str(rivi)
                    print("Final hands:")
                    print_dealer_whole_hand(jakajak,summa2)
                    print_hand_and_value(name,pelaajak)
            
                    if summa1 > summa2:
                        print("You won.")
            
                    if summa2 > summa1:
                        print("Dealer won.")
                        
                    if summa2 == summa1:
                        print("It's a tie.")
                
                    break

                elif summa2 == 21:
                    rivi = input("Press enter to see final hands.\n")
                    rivi = str(rivi)
                    print("Final hands:")
                    print_dealer_whole_hand(jakajak,summa2)
                    print_hand_and_value(name,pelaajak)
            
                    if summa1 > summa2:
                        print("You won.")
            
                    if summa2 > summa1:
                        print("Dealer won.")
                    
                    if summa2 == summa1:
                        print("It's a tie.")    
                
                    break
            
                elif summa2 > 21:
                    print("Dealer went bust. You won.")
                    break


            rivi = input("The dealer draws another card. Press enter to continue.\n")
            rivi = str(rivi)
            
            jakajak.append(deck.pop())
            summa2 = hand_value(jakajak)
            print_dealer_whole_hand(jakajak,summa2)
        
            if summa2 >= 17 and summa2 < 21:
                rivi = input("Press enter to see final hands.\n")
                rivi = str(rivi)
                print("Final hands:")
                print_dealer_whole_hand(jakajak,summa2)
                print_hand_and_value(name,pelaajak)
            
                if summa1 > summa2:
                    print("You won.")
            
                if summa2 > summa1:
                    print("Dealer won.")
                    
                if summa2 == summa1:
                    print("It's a tie.")
                
                break
        
            elif summa2 == 21:
                rivi = input("Press enter to see final hands.\n")
                rivi = str(rivi)
                print("Final hands:")
                print_dealer_whole_hand(jakajak,summa2)
                print_hand_and_value(name,pelaajak)
            
                if summa1 > summa2:
                    print("You won.")
            
                if summa2 > summa1:
                    print("Dealer won.")
                    
                if summa2 == summa1:
                    print("It's a tie.")    
                
                break
            
            elif summa2 > 21:
                print("Dealer went bust. You won.")
                break
      
            p += 1    
main()