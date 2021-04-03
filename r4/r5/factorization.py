'''
Created on 24.9.2019

@author: jenni
'''

def prime_factorize(number):
    alkutekijat = []
    tekija = 2
    while tekija <= number:
        while (number % tekija == 0):
            number /= tekija
            alkutekijat.append(tekija)
        tekija += 1
        
    return alkutekijat    
          

def main():
    num = int(input("Enter the number to be prime-factorized:\n"))
    result = prime_factorize(num)
    print("prime_factorize({:d}) returned {}".format(num, result))
    print("Meaning that the prime factorization of {number:d} is\n{number:d} == {factors_string}."
          .format(number = num, factors_string = " * ".join( str(factor) for factor in result) ))
    
main()