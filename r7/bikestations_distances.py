'''
Created on 18.10.2019

@author: jenni
'''

def find_shortest_and_longest(lista):
    LONGITUDE_DEGREE_LENGTH = 55.26 # km
    LATITUDE_DEGREE_LENGTH = 111.2 # km
    isoin = 0.0
    pienin = 1000.0
    
    
    for avain in lista:
        lista1 = lista[avain]
        pituus1 = float(lista1[0] * LONGITUDE_DEGREE_LENGTH)
        leveys1 = float(lista1[1] * LATITUDE_DEGREE_LENGTH)
        
        for avain2 in lista:
            lista2 = lista[avain2]
            pituus2 = float(lista2[0] * LONGITUDE_DEGREE_LENGTH)
            leveys2 = float(lista2[1] * LATITUDE_DEGREE_LENGTH)
            
            pituus = pituus1 - pituus2
            if pituus < 0:
                pituus = pituus * (-1)
                
            leveys = leveys1 -leveys2
            if leveys < 0:
                leveys = leveys * (-1)
    
            etaisyys = ((pituus**2)+(leveys**2))**(1/2)
            
            if etaisyys < 0:
                etaisyys = etaisyys * (-1)
            
            if etaisyys > isoin and avain != avain2:
                isoin = etaisyys
                paikka1 = avain
                paikka2 = avain2
        
            if etaisyys < pienin and avain != avain2:
                pienin = etaisyys
                paikka3 = avain
                paikka4 = avain2
    
    return pienin, isoin, paikka1, paikka2, paikka3, paikka4
    

def calculate_station_distance(coordinate_dictionary, station1, station2):
    """
    Calculates the distance between 2 stations in kilometers.
    A simplified formula based on Pythagorean theorem and rectangular coordinates
    that only works around Helsinki capital area.

    parameters: coordinate_dictionary: dict
                             station1: str
                             station2: str

    returns the distance in kilometers (float)
    """
    LONGITUDE_DEGREE_LENGTH = 55.26 # km
    LATITUDE_DEGREE_LENGTH = 111.2 # km

    koordinaatit1 = coordinate_dictionary[station1]
    koordinaatit2 = coordinate_dictionary[station2]
    
    pituus1 = float(koordinaatit1[0]) * LONGITUDE_DEGREE_LENGTH
    pituus2 = float(koordinaatit2[0]) * LONGITUDE_DEGREE_LENGTH
    leveys1 = float(koordinaatit1[1]) * LATITUDE_DEGREE_LENGTH
    leveys2 = float(koordinaatit2[1]) * LATITUDE_DEGREE_LENGTH
    
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
    coordinate_dictionary = {}
    k = 0
    p = 0
    done = False
    done1 = False
    
    rivi = input("Enter the filename containing the station data:\n")
    filename = str(rivi)
    
    try:
        lahtotiedosto = open(filename,"r")

        for rivi in lahtotiedosto:
            rivi = rivi.rstrip()
            rivi1 = rivi.split(";")
            
            if p != 0:
                try:
                    leveys = float(rivi1[0])
                    pituus = float(rivi1[1])
                    avain = str(rivi1[3])  
                    k += 1 
                    coordinate_dictionary[avain] = leveys,pituus
                except ValueError:
                    print("Invalid coordinates in line:",rivi)                    
                
            p += 1

        lahtotiedosto.close()
        print("File read succesfully!", k ,"valid stations found.\n")  
        
        if k >= 2:
            lyhin, pisin, paikka1, paikka2, paikka3, paikka4 = find_shortest_and_longest(coordinate_dictionary)
         
            print("Shortest distance was {:.3f} km between the stations {:s} and {:s}.".format(lyhin,paikka3,paikka4))
            print("Longest distance was {:.1f} km between the stations {:s} and {:s}.\n".format(pisin,paikka1,paikka2))
         
            print("Find a distance between any 2 stations!")
        
            print("First station:")
            eka = input()
            if eka not in coordinate_dictionary:  
                while not done:    
                    print("Station not found, try again:")
                    eka = input()
                    if eka in coordinate_dictionary:
                        break
        
            print("Second station:")
            toka = input()
            if toka not in coordinate_dictionary:
                while not done1:
                    print("Station not found, try again:")
                    toka = input()
                    if toka in coordinate_dictionary:
                        done1 = True      
                        break     
            
            etaisyys = calculate_station_distance(coordinate_dictionary,eka,toka)
            etaisyys = round(etaisyys,2)
            
            print("The distance is {:.2f} km between {:s} and {:s}.".format(etaisyys,eka,toka))
        else:
            print("Insufficient data for distance calculations.")
    
    except OSError:  
        print("Error in reading the file ",filename,".")   
        
main()