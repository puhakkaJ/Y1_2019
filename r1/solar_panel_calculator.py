'''
Created on 11.9.2019

@author: jenni
'''

rivi = input("How many solar panels' energy yield do you want to calculate?\n")
määrä = int(rivi)
print("That number of panels gives", (määrä * 175) / 1000, "kWh of energy each day.")
print("That is equal to watching the TV for", (määrä * 175) / 80, "hours")
print("or having", (määrä * 175) / 18, "led bulbs on for 10 hours per day.")

