'''
Created on 21.10.2019

@author: jenni
'''

from string import ascii_lowercase

vokaalit = [ 'a','e','i','o','u','y']
konsonantit = [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'z','w','q','x' ]


def viiva(sanalista,p):
    for i in range(len(sanalista)-1,-1,-1):
        sana = sanalista[i]
        if sana[p] not in vokaalit:
            del sanalista[i]

def tahti(sanalista,p):
    for i in range(len(sanalista)-1,-1,-1):
        sana = sanalista[i]
        if sana[p] not in konsonantit:
            del sanalista[i]
    
def main():
    sanalista = []

    k = 0
    t = 0
    i = 0
    p = 0
    
    sanatiedosto = open('words.txt','r')
    
    for rivi in sanatiedosto:
        rivi = str(rivi.rstrip())
        sanalista.append(rivi)
     
    sanatiedosto.close()
       
    print("Welcome to the crossword generator! Discover hidden words!")
    print("_ = any letter")
    print("* = any consonant")
    print("- = any vowel")
    rivi = input("Enter the word with all the known letters (eg. 's___nt', '__-k', '***_****'):\n")
    sana = str(rivi)
    
    for kirjain in sana:
        if kirjain not in ascii_lowercase:
            if kirjain != "_" and kirjain != "*" and kirjain != "-":
                k += 1
                if k == 1:
                    print("")
                    print("Your word contains an incorrect character '{:s}'".format(kirjain))
        
    if k == 0:
        for i in range(len(sanalista)-1,-1,-1):
            if len(sanalista[i]) != len(sana):
                del sanalista[i]

        for kirjain in sana:
            if kirjain == "*":
                tahti(sanalista,p)
            elif kirjain == "-":
                viiva(sanalista,p)
        
            elif kirjain != "_":
                for i in range(len(sanalista)-1,-1,-1):
                    sana = sanalista[i]
                    if kirjain != sana[p]:
                        del sanalista[i]
            p += 1    
        
        if len(sanalista) == 0:
            print("")
            print("There were no matches :(")    
       
        else:
            for sana in sanalista:
                t += 1
                print(str(sana))     
            print("")
            print("There were",t,"matches.")
        
               
main()