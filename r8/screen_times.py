'''
Created on 19.10.2019

@author: jenni
'''

import datetime

def print_file_contents(name_of_the_file):
    "Prints the contents of the file with the name 'name_of_the_file'. Make sure the file is not still open elsewhere before calling this function."
    file = open(name_of_the_file, 'r')
    line = file.readline()
    while line != '':
        print(line, end='')
        line = file.readline()
    file.close()

def main():
    n = 0
    summa = 0
    filename = input("Enter the name of the file to be created for your screen time data:\n")
    file = open(filename, 'w') 
    date_text = input("Enter the start date in format 'DD.MM.YYYY':\n")
    
    date_as_list = date_text.split(".")
    day, month, year = [int(part) for part in date_as_list]
    date1 = datetime.date(year, month, day) 
    
    print("Enter your screen watching time for each day (in minutes) in the format '[Phone minutes] [PC minutes] [TV minutes] [other minutes]'")
    rivi = input("Enter your screen time on {}{:<s} ".format(date1,":"))
    
    if rivi != "":
        arvot = rivi.split()
        summa = summa + int(arvot[0]) + int(arvot[1]) + int(arvot[2]) + int(arvot[3])
        arvot = str('/'.join(arvot))
        file.write("{}{:<s} {:s}\n".format(date1,":",arvot))
        n += 1
    
        while rivi != "":
            date = date1 + datetime.timedelta(days = n)
            rivi = input("Enter your screen time on {}{:<s} ".format(date,":"))
        
            if rivi == "":
                break
            arvot = rivi.split()
            summa = summa + int(arvot[0]) + int(arvot[1]) + int(arvot[2]) + int(arvot[3])
            arvot = str('/'.join(arvot))
            file.write("{}{:<s} {:s}\n".format(date,":",arvot))
            n += 1
    
        file.close()
    
        summa1 = summa / 60
        summa = round(summa1,1)
        keskiarvo = summa1 / n
        keskiarvo = round(keskiarvo,1)
        print("-" * 100)
        print("Screen times saves succesfully in the file '{:s}'".format(filename))
        print("Saved the screen times of", n ,"days.")
        print("Total screen time from this period is {:.1f} hours and daily average is {:.1f} hours.".format(summa,keskiarvo))
    
        print()
        print("Let's look inside the file. It looks as follows:")
        print("-" * 100)
        print_file_contents(filename)
        
    else:
        print("-" * 100)
        print("Screen times saves succesfully in the file '{:s}'".format(filename))
        print("Saved the screen times of", n ,"days.")
        print("")

        print("Let's look inside the file. It looks as follows:")
        print("-" * 100)

main() 