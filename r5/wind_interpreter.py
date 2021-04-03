'''
Created on 24.9.2019

@author: jenni
'''

def speed_description(nopeus):
    WIND_SPEED_LOW_LIMITS = [0, 1, 4, 7, 11, 17, 22, 28, 34, 41, 48, 56, 64]
    WIND_SPEED_DESCRIPTIONS = ['calm', 'light air', 'light breeze', 'gentle breeze',
                           'moderate breeze', 'fresh breeze', 'strong breeze',
                           'near gale', 'gale', 'severe gale', 'strong storm',
                           'violent storm', 'hurricane']

    i = 0
    while nopeus >= WIND_SPEED_LOW_LIMITS[i]:
        i = i +1
        
        if i > 12:
            p = 12
            alaraja = WIND_SPEED_DESCRIPTIONS[p]    
            return alaraja
        
    if i <= 12:
        i = i -1
        
        alaraja = WIND_SPEED_DESCRIPTIONS[i]    
        return alaraja    

def direction_description(kulma):
    WIND_DIRECTION_LOW_LIMITS = [0] + [45 * (p + (1/2)) for p in range(8)]

    WIND_DIRECTION_DESCRIPTIONS = ["north.", "north-east.","east.","south-east.",
                                   "south.","south-west.","west.", "north-west.",
                                   "north."]
    i = 0
    while kulma >= WIND_DIRECTION_LOW_LIMITS[i]:
        i = i +1
        
        if i > 8:
            p = 8
            suunta = WIND_DIRECTION_DESCRIPTIONS[p]
            return suunta
    
    if i <= 8:
        i = i -1
        suunta = WIND_DIRECTION_DESCRIPTIONS[i]
        return suunta

def main():
    rivi = input("What is the wind speed (in knots)?\n")
    nopeus = float(rivi)
    
    if nopeus < 0:
        while nopeus < 0:
            print("The wind speed must be non-negative.")
            rivi = input("What is the wind speed (in knots)?\n")
            nopeus = float(rivi)
            
    if nopeus >= 0 and nopeus < 1:
        print("It is calm.")
        
    else:   
        rivi = input("Where is the wind blowing from (in degrees; 0-360; 0 = north; ascending clockwise)?\n")
        kulma = float(rivi)
    
        if kulma < 0 or kulma > 360:
            while kulma < 0 or kulma > 360:
                print("The wind direction must be an angle between 0 and 360.")
                rivi = input("Where is the wind blowing from (in degrees; 0-360; 0 = north; ascending clockwise)?\n")
                kulma = float(rivi)
        
        speed_description(nopeus)   
        nopeus1 = speed_description(nopeus)
        direction_description(kulma)
        suunta = direction_description(kulma)
    
        print("A", nopeus1 ,"is blowing from the", suunta ,)     
main()