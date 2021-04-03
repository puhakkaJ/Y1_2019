'''
Created on 6.10.2019

@author: jenni
'''

def compare_words(word1, word2):
    p = 0
    k = 0
    s = 0
    h = 0
    sana1 = word1
    sana1 = sana1.lower()
    sana2 = word2
    sana2 = sana2.lower()
    
    suuruus = len(sana1)-1
    kielletyt = []
    
    if len(sana1) != len(sana2):
        s = (-1)
        p = (-1)
        
    else:
        while k != len(sana1):
            if sana1[k] == sana2[k]:
                s += 1
                kielletyt.append(sana1[k])
            k += 1
        
        for arvo in kielletyt:
            if arvo in sana1:
                paikka = sana1.index(arvo)
                sana1 = sana1[:paikka] + sana1[(paikka+1):]
        
        for arvo in kielletyt:
            if arvo in sana2:
                paikka = sana2.index(arvo)
                sana2 = sana2[:paikka] + sana2[(paikka+1):]
        
        if s == 0:
            for kirjain in sana1:
                if kirjain in sana2:
                    p += 1
                    luku1 = sana2.index(kirjain)
                    luku2 = luku1 + 1
                    sana2 = sana2[:luku1] + sana2[luku2:]
                     
        if s != 0:      
            while h != len(sana1):
                if sana1[h] in sana2:
                    p += 1
                    luku11 = sana2.index(sana1[h])
                    luku22 = luku11 + 1
                    sana2 = sana2[:luku11] + sana2[luku22:]
                h += 1       
    return s, p

def main():
    print("Let's compare some words!")
    cont = True
    while cont:
        first_word = input("First word:\n")
        second_word = input("Second word:\n")
        matching_letters_same_place, matching_letters_diff_place = compare_words(first_word, second_word)
        print("compare_words('{:s}', '{:s}') returned the values {:d}, {:d}".format(first_word, second_word, matching_letters_same_place, matching_letters_diff_place))
        print("Enter to continue, Q+Enter to quit")
        if input().upper().startswith('Q'):
            cont = False


main()