'''
Created on 23.9.2019

@author: jenni
'''

def main():
    
    days = int(input("How many sales will you input?\n"))
    sales = [0.0] * days
    for i in range(days):
        sales_day = float(input("Enter the next amount.\n"))
        sales[i] = sales_day

    print("Commissions")

    LIMIT = 250             # euros
    NORMAL_COMMISSION = 8   # %
    BONUS_COMMISSION = 12.5 # %
    k = 0
    summa = 0

    while k < days:
        if sales [k] >= 250.0:
            provikka = sales[k] * 0.125
            print("{:.2f} eur". format(provikka))
            summa += provikka
            k = k + 1
            
        elif sales [k] < 250.0:
            provikka = sales [k] * 0.08
            print("{:.2f} eur". format(provikka))
            summa += provikka
            k = k + 1
         
    print("Total commissions {:.2f} eur.". format(summa))
 
main()    