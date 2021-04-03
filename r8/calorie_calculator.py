'''
Created on 27.10.2019

@author: jenni
'''

def laske_kulutus(rivi,paino,aika):
    aika = aika/60
    kalorit = float(aika * paino * float(rivi[2]))
    kalorit = round(kalorit,0)
    
    return kalorit

def etsi_sana(sana,lista):
    lista1 = []
    sana = sana.lower()
    for rivi in lista:
        k = 0
        rivi1 = rivi[1]
        rivi1 = rivi1.split(",")
        rivi2 = rivi[0]
        rivi2 = rivi2.lower()
        if sana in rivi2:
            lista1.append(rivi)
            k += 1
        for osa in rivi1:
            osa = osa.lower()
            if sana in osa and k == 0:
                lista1.append(rivi)
                k += 1

    return lista1

def main():
    k = 0
    t = 0
    p = 0
    tiedot = []
    try:
        rivi = input("Enter the file name containing the MET data:\n")
        tiedosto = str(rivi)
        tiedosto = open(tiedosto,'r')
        
        for rivi in tiedosto:
            t += 1
            rivi = rivi.rstrip()
            rivi = rivi.split(";")
            
            try: 
                if len(rivi) >= 3 and float(rivi[2]):
                    tiedot.append(rivi)
                    p += 1
                    
            except ValueError:
                k += 1
          
        done = False   
        print("File read succesfully. There were {:0d} valid lines out of {:>1d}{:<0s}".format(p,t,'.'))
        while not done:
            try:
                rivi = input("Enter your weight in kg:\n")
                paino = float(rivi)
                if paino < 0 or paino > 500:
                    print("The input must be a number in the range of 0 to 500")
                else:
                    done = True
            except ValueError:
                print("The input must be a number in the range of 0 to 500")
        
        done1 = False    
        while not done1:
            try:
                rivi = input("How long did you exercise in minutes?\n")
                aika = float(rivi)
                if aika < 0 or aika > 1440:
                    print("The input must be a number in the range of 0 to 1440")
                else:
                    done1 = True
            except ValueError:
                print("The input must be a number in the range of 0 to 1440")
                done1 = False
        
        rivi = input("Enter an activity or word to search for:\n")
        sana = str(rivi)
     
        lista = etsi_sana(sana,tiedot)
        if len(lista) == 0:
            print("None of the activities in the file match your search.")
            
        else:
            rivit = {}
            k = 0
            print("Your search produced the following results:") 
            for rivi in lista:
                k += 1
                rivit[k] = rivi
                rivi = rivi[1]
                print("{:>3.0f}{:<s} {:s}".format(k,".",rivi))
             
            print("----------------------------------------------------------------------------------------------------")   
            
            done3 = False
            while not done3:
                try:
                    rivi = input("Enter the number of the activity that is the closest to what you meant:\n")
                    luku = int(rivi) 
                    if luku < 1 or luku > k:
                        print("The input must be an integer in the range of 1 to", k)
                    else:
                        done3 = True   
                except ValueError:
                    print("The input must be an integer in the range of 1 to", k)
             
            rivi = rivit[luku]
            print("You chose the activity: {:s}".format(rivi[1]))
            kalorit = laske_kulutus(rivit[luku],paino,aika)
            print("You consumed approximately {:.0f} kcal.".format(kalorit))
            print("Hope you had a fun time with your activity!")
    
    except OSError:
        print("Error in reading the file '{:s}'".format(tiedosto))
           
main()        