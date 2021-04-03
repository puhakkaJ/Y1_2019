'''
Created on 17.9.2019

@author: jenni
'''

def main():

    CAFFEINE_IN_COFFEE_CUP =   120 # mg, milligrams
    CAFFEINE_IN_TEA_CUP    =    40 # mg
    MAX_RECOMMENDED_INTAKE =   400 # mg
    LETHAL_DOSE            = 10000 # mg
    i = 1
    k = 0
    s = 0
    yhteensa = 0
    
    print("The program calculates an adult's caffeine intake and gives feedback of the consumption.")
    rivi = input("How many days you wish to input?\n")
    paivat = int(rivi)
    
    if paivat == 0:
        print("No consumption data entered.")
            
    else:
        while i <= paivat:
            print("Day", i)
            rivi = input("How many cups of coffee did you drink?\n")                
            kahvit = int(rivi)
        
            if kahvit < 0:
                while kahvit < 0:
                    print("The number must be at least 0!")
                    rivi = input("How many cups of coffee did you drink?\n")
                    kahvit = int(rivi)
            
            rivi = input("And how many cups of tea?\n")
            teet = int(rivi)
            
            if teet < 0:
                while teet < 0:
                    print("The number must be at least 0!")
                    rivi = input("And how many cups of tea?\n")
                    teet = int(rivi)
                    print("\n")
            
            if ((CAFFEINE_IN_COFFEE_CUP * kahvit) + (CAFFEINE_IN_TEA_CUP * teet)) > MAX_RECOMMENDED_INTAKE:
                k = k + 1
            
            if ((CAFFEINE_IN_COFFEE_CUP * kahvit) + (CAFFEINE_IN_TEA_CUP * teet)) > LETHAL_DOSE:
                print("** Lethal dose exceeded!! **\n")
                s = s + 1
                
            else:
                print("")
            
            yhteensa += (CAFFEINE_IN_COFFEE_CUP * kahvit) + (CAFFEINE_IN_TEA_CUP * teet)
            i = i + 1
         
        h = ('%.0f'% (yhteensa / paivat))    
        print("On average, you consumed", h ,"mg of caffeine per day.")
        
        print("You exceeded the maximum recommended amount of 400 mg on", k ,"out of", paivat ,"days.")  
        
        if s > 0:
            print("You exceeded the lethal dose on", s ,"days.")

main()    