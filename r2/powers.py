'''
Created on 13.9.2019

@author: jenni
'''
 
rivi = input("Base number:\n")
kantaluku = int(rivi)
kantaluku >= 2
rivi = input("Upper limit for the powers:\n")
yläraja = int(rivi)
yläraja >= 2
i = 1
print("Powers:")
while kantaluku ** i < yläraja:
    print(kantaluku ** i)
    i = i + 1
    
    
