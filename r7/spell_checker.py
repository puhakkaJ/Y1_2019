'''
Created on 16.10.2019

@author: jenni
'''

def main():
    lista = open('words.txt','r')
    t = 0
    i = 0
    k = 0
    sanat = []
    tekstit = {}
    done = False
    
    for sana in lista:
        sana = sana.rstrip()
        sanat.append(sana)
     
    print("Enter the text to be spell-checked (empty line to end input).")
        
    while not done:
        rivi = input()
        
        if rivi == "":
            break
        
        teksti = str(rivi)
        teksti = teksti.split()
        tekstit[i] = teksti
        
        tarkastus = tekstit[i]
        k = 0
        
        for arvo in tarkastus:
            arvo = arvo.lower()
            if arvo not in sanat:
                arvo = "*"+arvo+"*"
                tarkastus[k] = arvo
                t +=1
            k += 1    
        
        i +=1
    
    print("Checked text, typos highlighted with '*'")  
    
    for arvo in tekstit:  
        arvo = '  '.join(tekstit[arvo])
        print(">>",arvo)
    
    if t == 0:
        print("The text was clean.")
    
    else:
        print("There were", t ,"typos.")
main()    