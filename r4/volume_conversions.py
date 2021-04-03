'''
Created on 22.9.2019

@author: jenni
'''

def convert_tablespoons(tablespoons):
    tilavuusmilli = tablespoons * 14.79
    return tilavuusmilli
    
def convert_fluid_ounces(fl_oz):
    tilavuusmilli = fl_oz * 29.57
    return tilavuusmilli

def convert_cups(cups):
    tilavuusmilli = cups * 236.59
    return tilavuusmilli

def convert_pints(pints):
    tilavuusmilli = pints * 473.18
    return tilavuusmilli
       
def print_volume(millilitres):
    if millilitres >= 1000:
        litroissa = millilitres / 1000
        print("The equivalent volume in metric units is {:.1f} l.". format(litroissa))
    
    elif millilitres >= 100:
        desilitra = millilitres / 100
        print("The equivalent volume in metric units is {:.1f} dl.". format(desilitra))
        
    else: 
        print("The equivalent volume in metric units is {:.1f} ml.". format(millilitres))   
    

def main():
    print("The program converts US volume units into metric volume units.") 
    print("Choose the starting unit.")
    print("1 - Tablespoon")
    print("2 - Fluid ounce")
    print("3 - Cup")
    print("4 - Pint")
    yksikko = int(input())
    
    if yksikko < 1:
        while (yksikko < 1) or (yksikko > 4):
            print("Choose the starting unit.")
            print("1 - Tablespoon")
            print("2 - Fluid ounce")
            print("3 - Cup")
            print("4 - Pint")
            yksikko = int(input())
            
    if yksikko > 4:
        while (yksikko < 1) or (yksikko > 4):
            print("Choose the starting unit.")
            print("1 - Tablespoon")
            print("2 - Fluid ounce")
            print("3 - Cup")
            print("4 - Pint")
            yksikko = int(input())        
                                          
    if yksikko == 1:
        rivi = input("What is the volume in tablespoons?\n")
        tilavuus = float(rivi)
        convert_tablespoons(tilavuus)
        print_volume(convert_tablespoons(tilavuus))  
       
    if yksikko == 2:
        rivi = input("What is the volume in fluid ounces?\n")
        tilavuus = float(rivi)
        convert_fluid_ounces(tilavuus)
        print_volume(convert_fluid_ounces(tilavuus))  
         
    if yksikko == 3:
        rivi = input("What is the volume in cups?\n")  
        tilavuus = float(rivi)
        convert_cups(tilavuus)
        print_volume(convert_cups(tilavuus))   
        
    if yksikko == 4:
        rivi = input("What is the volume in pints?\n")  
        tilavuus = float(rivi)
        convert_pints(tilavuus)
        print_volume(convert_pints(tilavuus))  
                     
main()        
        