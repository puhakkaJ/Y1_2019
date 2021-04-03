'''
Created on 18.9.2019

@author: jenni
'''

def main():
    print("This program calculates and summarizes the estimated profits from an investment.")

    initial_investment    = float(input("Initial investment sum (eur):\n"))
    annual_profit_percent = float(input("Expected annual growth / return rate (including expenses) (%):\n"))
    per_month_investment  = float(input("Monthly investment (+) or withdrawal (-) (eur):\n"))
    years                 = float(input("For how many years are you planning to hold the investment?\n"))
    i = 1
    k = 1
    p = 0
    kuukaudet = (int(years * 12))
    done = False
    
    e = "eur"
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('Year','Month','Start','Monthly', 'End', 'Cumulative'))
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('','','balance','Profit', 'balance','Profit'))
    print('{:>5s} | {:>5s} | {:>10s} | {:>10s} | {:>10s} | {:>10s}'.format('','',e,e,e,e))
    print('-' * 65)

    annual_profit_multiplier = 0.01 * annual_profit_percent
    # There are 12 months in a year; let's divide the exponential growth to them expecting it to be constant:
    monthly_profit_multiplier = (1 + annual_profit_multiplier) ** (1 / 12) - 1
    tuottok = monthly_profit_multiplier * initial_investment
    uusisumma = initial_investment + ( tuottok + per_month_investment )
    tuottoyhteensa = tuottok
    a = initial_investment
    
        
    while not done:
        print('{:>5.0f} | {:>5.0f} | {:>10.2f} | {:>10.2f} | {:>10.2f} | {:>10.2f}'.format(i,k,initial_investment,tuottok,uusisumma,tuottoyhteensa))   
        p += 1
        k += 1    
        
        if k == 13:
            print('-' * 65)

            i += 1
            k -= 12  
        
        if p == kuukaudet:
            done = True
        
        initial_investment = initial_investment + ( tuottok + per_month_investment )
        tuottok = monthly_profit_multiplier * initial_investment
        uusisumma += (tuottok + per_month_investment)
        tuottoyhteensa += tuottok
        
        if (uusisumma or initial_investment) <= 0:
            done = True
                                       
    if done:
        if (uusisumma or initial_investment) <= 0:
            talletukset = a + (p * per_month_investment)

            print("")
            print("Stopped printing as balance cannot go negative.")
            print("End balance:{:>18.2f} eur". format(uusisumma - (tuottok + per_month_investment)))   
            print("Total profit:{:>17.2f} eur". format(tuottoyhteensa - tuottok)) 
            print("Total net deposit:{:>12.2f} eur". format (talletukset,))      
        
            
        else:
            talletukset = a + (p * per_month_investment)

            print("")
            print("End balance:{:>18.2f} eur". format (uusisumma - tuottok - per_month_investment))   
            print("Total profit:{:>17.2f} eur". format (tuottoyhteensa - tuottok)) 
            print("Total net deposit:{:>12.2f} eur". format (talletukset))      
        
main()   