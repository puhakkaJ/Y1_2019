'''
Created on 12.9.2019

@author: jenni
'''
rivi = input("How many times per week do you eat student lunch?\n")
lviikossa = int(rivi)
rivi = input("What is the price of one student lunch (eur)?\n")
hinta = float(rivi)
rivi = input("How much do you spend on other groceries weekly (eur)?\n")
muu = float(rivi)
print("Your food expenses are", (lviikossa * hinta) + muu, "euros per week")
print("which is on average", ((lviikossa * hinta) + muu) / 7, "euros per day")
print("and", ((lviikossa * hinta) + muu) / 7 * 30, "euros per month.")



