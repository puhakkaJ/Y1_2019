'''
Created on 22.9.2019

@author: jenni
'''

def calculate_storage_size(battery_orders_weight):
    osa = battery_orders_weight / 150
    varasto = ( osa / 0.1 )
    
    print("Required storage size is", varasto , "cubic meters.")

def calculate_emissions(storage_size):
    sähkö = storage_size * 200
    määrä = sähkö * 0.010
    print("Emissions in two weeks are", määrä ,"CO2 equivalents.")

def main():
    print("Please choose one of the options")
    print("1 - Calculate storage size")
    print("2 - Calculate emissions")
    func = input()
    
    while func != "1" and func != "2":
        print("Please choose one of the options")
        print("1 - Calculate storage size")
        print("2 - Calculate emissions")
        func = input()
        
    if func == "1":
        rivi = input("How many kilograms of batteries are being supplied each two weeks?\n")
        määrä = int(rivi)
        calculate_storage_size(määrä)
        
    elif func == "2":
        rivi = input("What is the current storage size (cubic meters)?\n")
        koko = int(rivi)
        calculate_emissions(koko)
    
main()