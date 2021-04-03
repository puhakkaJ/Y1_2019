'''
Created on 17.9.2019

@author: jenni
'''
def main():
    rivi = input("Enter the current year:\n")
    vuosinyt = int(rivi)
    
    if vuosinyt <= 0:
        while vuosinyt <= 0:
            print("Enter a positive year!")
            rivi = input("Enter the current year:\n")
            vuosinyt = int(rivi)
        
    rivi = input("Enter the first year to be printed:\n")
    ekavuosi = int(rivi)
    
    if ekavuosi <= 0:
        while ekavuosi <= 0:
            print("Enter a positive year!")
            rivi = input("Enter the first year to be printed:\n")
            ekavuosi = int(rivi)
            
    rivi = input("Enter the last year to be printed:\n")
    vikavuosi = int(rivi)
    
    if vikavuosi <= ekavuosi:
        while vikavuosi < vuosinyt:
            print("Enter a later year than the first!")
            rivi = input("Enter the last year to be printed:\n")
            vikavuosi = int(rivi)
            
    if vikavuosi <= 0:
        while vikavuosi <= 0:
            print("Enter a positive year!")      
            rivi = input("Enter the last year to be printed:\n")
            vikavuosi = int(rivi)

    print("Leap years from",ekavuosi,"to {:>d}:". format(vikavuosi)) 
    
    if ekavuosi < vuosinyt and vikavuosi > vuosinyt:
        for i in range(ekavuosi, vuosinyt, 1):
            if ( i % 4 == 0 and i % 100 != 0) or ( i % 4 == 0 and i % 100 == 0 and i % 400 == 0 ):
                print(i,"was a leap year")    
        
        if ( vuosinyt % 4 == 0 and vuosinyt % 100 != 0) or ( vuosinyt % 4 == 0 and vuosinyt % 100 == 0 and vuosinyt % 400 == 0 ):
            print(vuosinyt,"is a leap year")
        
        for i in range((vuosinyt + 1), (vikavuosi + 1), 1):  
            if ( i % 4 == 0 and i % 100 != 0 and i <= vikavuosi ) or ( i % 4 == 0 and i % 100 == 0 and i % 400 == 0 and i <= vikavuosi):
                print(i,"will be a leap year")
     
    if ekavuosi > vuosinyt:
        for i in range(ekavuosi, (vikavuosi + 1), 1):
            if ( i % 4 == 0 and i % 100 != 0 and i <= vikavuosi) or ( i % 4 == 0 and i % 100 == 0 and i % 400 == 0 and i <= vikavuosi):
                print(i,"will be a leap year")        
                
    if ekavuosi < vuosinyt and vikavuosi < vuosinyt:
        for i in range(ekavuosi, (vikavuosi + 1), 1):
            if ( i % 4 == 0 and i % 100 != 0 and i <= vikavuosi) or ( i % 4 == 0 and i % 100 == 0 and i % 400 == 0 and i <= vikavuosi):
                print(i,"was a leap year") 
main ()               
                