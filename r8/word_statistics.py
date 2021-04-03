'''
Created on 28.10.2019

@author: jenni
'''

import re

N = 70 # how many chars to print.
CHARS_TO_STRIP= "[., \!?:;_\n\t\—\'\[\]\/\(\)\"@$+<>|^=]+"

def is_alpha_or_hyphened(word):
    alpha_found = False
    parts = word.split("-")
    for w in parts:
        if w.isalpha():
            alpha_found = True
        elif not w.isdigit():
            return False
    return alpha_found

def main():
    kaikkisanat = 0
    luku = 1
    kaikkisanatlista = []
    maarat = []
    kaytetytsanat = []
    sanojenpituus = {}
    sanojenmaara = {}
    k = 0
    
    try:
        rivi = input("Enter the name of the file to be read:\n")
        tiedosto = str(rivi)
        tiedosto1 = open(tiedosto,'r')
        data = tiedosto1.read()
        tiedosto1.close()
            
        data_list = filter(None, re.split(CHARS_TO_STRIP, data)) # helps to split data into list
        for word in data_list:
            is_alpha_or_hyphened(word)
            if is_alpha_or_hyphened(word):
                kaikkisanat += 1
                kaikkisanatlista.append(word)
        
        while luku != 0:
            print("Choose one of the options:")
            print("0 - Exit")
            print("1 - Print statistics")
            print("2 - Print vertical graph")
            print("3 - Print most common words")
            luku = int(input())
                
            if k == 0:
                summa = 0    
                for sana in kaikkisanatlista:
                    summa += int(len(sana))
                
                pituus = round(summa / kaikkisanat,1)
                erisanat = 0
                for sana in kaikkisanatlista:
                    sana = sana.lower()
                    if sana not in kaytetytsanat:
                        kaytetytsanat.append(sana)
                            
                erisanat = len(kaytetytsanat) 
                
                for sana in kaikkisanatlista:
                    avain = len(sana)
                    if avain not in sanojenpituus:
                        sanojenpituus[avain] = 1
                    else:
                        sanojenpituus[avain] += 1 
                    sana = sana.lower()
                    if sana not in sanojenmaara:
                        sanojenmaara[sana] = 1
                    else: 
                        sanojenmaara[sana] += 1    
                
                maksimi = 0
                suurin = 0
                for avain in sanojenpituus:
                    if sanojenpituus[avain] > maksimi:
                        maksimi = sanojenpituus[avain]
                        yleisin = avain
                    if avain > suurin:
                        suurin = avain
                        
            k += 1       
            if luku == 1:   
                print("Word statistics from the file:", tiedosto)
                print("----------------------------------------------------------------------------------------------------")
                          
                print("Total number of words: {:.0f}".format(kaikkisanat)) 
                print("Total number of distinct words: {:.0f}".format(erisanat))
                print("Average word length: {:.1f}".format(pituus))
                print("Most common word length: {:.0f}".format(yleisin))     
                print("----------------------------------------------------------------------------------------------------")
        
            if luku == 2:
                risuaita = round(sanojenpituus[yleisin] / N,0)
                if risuaita < 1:
                    risuaita = 1
                
                print("Distribution of words from the file:", tiedosto)
                print("----------------------------------------------------------------------------------------------------")
   
                print("Distribution of words")
                print("-------------------------")
                print("  Word| no of|  # = {:.0f}".format(risuaita))
                print("length| words|  word(s)")
                print("-------------------------")
                for i in range(suurin+1):
                    if i in sanojenpituus:
                        k = int(sanojenpituus[i] // risuaita)
                        print("{:>6.0f}|{:>6.0f}|{:<s}".format(i,sanojenpituus[i],"#"*k))    
                print("----------------------------------------------------------------------------------------------------")
            
            if luku == 3:
                print("Most common words from the file:", tiedosto)
                print("----------------------------------------------------------------------------------------------------")
                rivi = input("Enter the minimum length for most common words:\n")
                raja = int(rivi)
                k = 0
                
                for avain in sanojenmaara:
                    if sanojenmaara[avain] >= 3:
                        if len(avain) >= raja:
                            luku = int(sanojenmaara[avain])
                            maarat.append(luku)
               
                maarat.sort()
                maarat.reverse() 
                avaimet = []
                for avain in sanojenmaara:
                    avaimet.append(avain)
                
                avaimet.sort()
                kielletyt = []
                
                if len(maarat) < 10:
                    t = len(maarat)
                else:
                    t = 10
                      
                for i in range(t):
                    luku = maarat[i]
                    for avain in avaimet:
                        if len(avain) >= raja and sanojenmaara[avain] == luku and avain not in kielletyt and k != 10:
                            maara = int(sanojenmaara[avain])
                            sana = str(avain)
                            kielletyt.append(avain)
                            k += 1
                if k == 0:
                    print("Not enough data for most common words.") 
                    print("----------------------------------------------------------------------------------------------------")
             
                else:
                    print("The most common {:>.0f}-letter or longer words".format(raja))
                    print("-------------------------------")
                    print("word                      count")
                    print("-------------------------------")
                    maarat = []
                    for avain in sanojenmaara:
                        if sanojenmaara[avain] >= 3:
                            if len(avain) >= raja:
                                luku = int(sanojenmaara[avain])
                                maarat.append(luku)
               
                    maarat.sort()
                    maarat.reverse() 
                    avaimet = []
                    for avain in sanojenmaara:
                        avaimet.append(avain)
                
                    avaimet.sort()
                    kielletyt = []
                
                    if len(maarat) < 10:
                        t = len(maarat)
                    else:
                        t = 10
                        
                    k = 0
                    for i in range(t):
                        luku = maarat[i]
                        for avain in avaimet:
                            if len(avain) >= raja and sanojenmaara[avain] == luku and avain not in kielletyt and k != 10:
                                maara = int(sanojenmaara[avain])
                                sana = str(avain)
                                print("{:<25s} {:>5.0f}".format(sana,maara))
                                kielletyt.append(avain)
                                k += 1
                    print("----------------------------------------------------------------------------------------------------")
        
    except OSError:
        print("Error in reading the file '{:s}'.".format(tiedosto))    
main()