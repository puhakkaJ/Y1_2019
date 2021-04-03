'''
Created on 27.9.2019

@author: jenni
'''

def enter_values(dictionary, name, step_input):
    askeleet = step_input.split(",")  
    askeleetl = []
    
    for osat in askeleet:
        osalukuna = int(osat)
        askeleetl.append(osalukuna)
    if name in dictionary:
        dictionary[name] += askeleetl
    
    else:
        dictionary[name] = askeleetl
           

def search_by_name(dictionary, name):
    summa = 0
    tyhja = []
    if name in dictionary:
        for arvo in dictionary[name]:
            summa += int(arvo)
    
        return dictionary[name], summa
    
    else:
        return tyhja, -1

def main():
    dictionary = {}

    name = input("Enter the name of the person. Stop with an empty line.\n")
    while name != "":
        step_input = input("Enter the different day's steps on one line.\n")
        enter_values(dictionary, name, step_input)
        name = input("Enter the name of the person. Stop with an empty line.\n")

    name = input("Enter name to search. Stop with an empty line.\n")
    while name != "":
        step_list, total_steps = search_by_name(dictionary, name)
        if total_steps == -1:
            print("No information on that person.")
        else:
            print("{:s}'s steps in a list: {}".format(name,step_list))
            print("{:s}'s total steps: {:d}".format(name,total_steps))
        name = input("Enter name to search. Stop with an empty line.\n")

    #print(dictionary)
    '''
    Remove the hash character from the line above if you want to see
    the contents of the dictionary while testing your program.
    Comment it back when you return your program.
    '''
    print("Program ends.")

main()