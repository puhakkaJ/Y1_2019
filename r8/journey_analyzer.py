'''
Created on 26.10.2019

@author: jenni
'''

from math import pi, cos, sqrt

EARTH_RADIUS = 6371 # km
EARTH_CIRCUMFERENCE = EARTH_RADIUS * 2 * pi # km
DEGREE_EQUATOR = EARTH_CIRCUMFERENCE / 360 # km

def degrees_to_radians(deg):
    rad = deg * (pi / 180)
    return rad

def calculate_longitude_degree_length(latitude_degrees):
    return cos(degrees_to_radians(latitude_degrees)) * DEGREE_EQUATOR # km

def calculate_distance(lat1, lon1, lat2, lon2):
    latitude_degree_length = 111.2 # km, roughly constant for our purposes
    longitude_degree_length = calculate_longitude_degree_length( (lat1+lat2) / 2 ) 
    
    pituus1 = lon1 * longitude_degree_length
    pituus2 = lon2 * longitude_degree_length
    leveys1 = lat1 * latitude_degree_length
    leveys2 = lat2 * latitude_degree_length
    
    pituus = pituus1 - pituus2
    if pituus < 0:
        pituus = pituus * (-1)
                
    leveys = leveys1 -leveys2
    if leveys < 0:
        leveys = leveys * (-1)
    
    distance = ((pituus**2)+(leveys**2))**(1/2)

    if distance < 0:
        distance = distance * (-1)
        
    return distance
    
def main():
    ajat = []
    done = False
    k = 1
    summa = 0
    
    while not done:
        try:
            rivi = input("Journey file name:\n")
            tiedosto = str(rivi)
            
            tiedosto = open(tiedosto,'r')
            done = True

        except OSError:
            print("Could not open the file",tiedosto,", try again.")

    tiedosto.readline()
    tiedosto.readline()
    tiedosto.readline()
    
    for rivi in tiedosto:
        rivi = rivi.rstrip()
        rivi = rivi.split(";")
        
        aika = rivi[3]
        aika = aika.split(":")
        
        tunnit = aika[0]
        tunnit = str(tunnit[11:13])
        if tunnit[0] == 0:
            tunnit = str(tunnit[1])
        
        minuutit = str(aika[1])
        if minuutit[0] == 0:
            minuutit = str(aika[1][1])  

        sekunnit = aika[2]
        sekunnit = str(sekunnit[:-1])
        if sekunnit[0] == 0:
            sekunnit = str(sekunnit[1])
        
        aikasekuntteina = (int(tunnit)*3600) + (int(minuutit)*60) + int(sekunnit)
        ajat.append(aikasekuntteina)
        
        if k % 2 == 0:
            lat2 = float(rivi[0])
            lon2 = float(rivi[1])
            
        elif k % 2 != 0:
            lat1 = float(rivi[0])
            lon1 = float(rivi[1])    
        if k != 1:
            etaisyys = calculate_distance(lat1, lon1, lat2, lon2)
            summa += etaisyys
        
        k += 1
        
    sekunnit1 = ajat[0]
    sekunnit2 = ajat[-1]
    
    sekunnit = sekunnit2 - sekunnit1
    aika = sekunnit/60
    
    print("Your journey took {:.1f} minutes.".format(aika))
    print("You travelled {:.1f} kilometers.".format(summa))
    
main()



