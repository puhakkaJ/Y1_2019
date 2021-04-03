'''
Created on 22.9.2019

@author: jenni
'''

def calculate_and_print(muoto, kanta, korkeus):
    if muoto == 'r':
        ala = kanta * korkeus
        print("The area is", ala ,"square meters.")
        
    if muoto == 't':  
        ala = ( kanta * korkeus ) / 2
        print("The area is", ala ,"square meters.") 

def main():
    print("Choose a shape:")
    print("r - rectangle")
    print("t - triangle")
    shape = input()
    base = float(input("Enter the length of the base (m):\n"))
    height = float(input("Enter the height (m):\n"))
    calculate_and_print(shape, base, height)

main()