'''
Created on 13.9.2019

@author: jenni
'''

rivi = input("How many AB-zone trips do you make per month?\n")
ab = int(rivi)
rivi = input("How many BC-zone trips do you make per month?\n")
bc = int(rivi)
rivi = input("How many ABC-zone trips do you make per month?\n")
abc = int(rivi)
while ab < 0 or bc <0 or abc < 0:
    print("The given values cannot be negative!")
    rivi = input("How many AB-zone trips do you make per month?\n")
    ab = int(rivi)
    rivi = input("How many BC-zone trips do you make per month?\n")
    bc = int(rivi)
    rivi = input("How many ABC-zone trips do you make per month?\n")
    abc = int(rivi)
    
hinnaty = ( ( ab + bc ) * 28 + ( abc * 46 )) / 10   
abkausi = ( 328 + ( bc + abc ) * 25 ) / 10
bckausi = ( 328 + ( ab + abc ) * 25 ) / 10 
abckausi = 591 / 10
if hinnaty < abkausi and hinnaty < bckausi and hinnaty < abckausi:
    print("You should buy single tickets for each trip.")
    print("The price per month will be", ( ab + bc ) * 28 / 10  + ( abc * 46 / 10 ), "euros.")
elif abkausi <= bckausi and abkausi < abckausi:
    print("You should buy an AB-zone season ticket and C-zone extension tickets when needed.")
    print("The price per month will be", abkausi, "euros.")
elif bckausi <= abkausi and bckausi < abckausi:
    print("You should buy a BC-zone season ticket and A-zone extension tickets when needed.")
    print("The price per month will be", bckausi, "euros.")
    
else:
    print("You should buy an ABC-zone season ticket.")
    print("The price per month will be 59.1 euros.")
    