'''
Created on 25.9.2019

@author: jenni
'''

GRADES = [4,5,6,7,8,9,10]
GRADES_DESCRIPTIONS = ["fail", "tolerable", "decent", "satisfactory", "good", "excellent", "outstanding"]
grade_average_list = []
course_amount_list = []
subject_list = []

def input_course_grades_and_calculate_average(subject, number_of_courses):
    i = 0
    summa = 0
    while i != number_of_courses:
        i += 1
        rivi = input("Grade received for the course {:^0s} {:0.0f}{:<0s} ". format(subject,i,':'))
        arvosana = int(rivi)
        summa += arvosana
        
    keskiarvo = summa / number_of_courses
    grade_average_list.append(keskiarvo)
    return keskiarvo

def calculate_averages(grade_average_list, course_amount_list):
    summa = 0
    jakaja = 0
    jaettava = 0
    i = 0
    
    for arvo in grade_average_list:
        summa += arvo
        jaettava += (arvo * course_amount_list [i]) 
        i += 1
        
    for arvo in course_amount_list:
        jakaja += arvo
    
    kurssikeskiarvo = jaettava / jakaja
    lukumaara = len(grade_average_list)
    ainekeskiarvo = summa / lukumaara
  
    return ainekeskiarvo, kurssikeskiarvo
    
def describe_grade_average(grade_average):
    luku = round(grade_average, 0)
    i = 0
    
    while GRADES[i] != luku:
        i += 1
     
        
    return GRADES_DESCRIPTIONS[i]    
    
def find_strongest_and_weakest_subject(subject_list, grade_average_list):
    muuttuja1 = 1
    muuttuja2 = 11
    i = 0
    p = 0
    done = False
    done2 = False
    
    for arvo in grade_average_list:
        if arvo > muuttuja1:
            muuttuja1 = arvo
    
    for arvo in grade_average_list:
        if arvo < muuttuja2:
            muuttuja2 = arvo
            
    while not done:
        if grade_average_list[i] == muuttuja1:
            done = True           
         
        i += 1
                
    while not done2:
        if grade_average_list[p] == muuttuja2:
            done2 = True           
         
        p += 1
            
    if i != 0:
        i = i - 1
        
    if p != 0:
        p = p - 1
    
    return muuttuja1, muuttuja2, subject_list[i], subject_list[p]       
    
def main():
    print("The program calculates averages and analyzes your school performance.")
            
    print("Enter the next subject:") 
    aine = str(input())   
    subject_list.append(aine)
    
    while aine.strip() != '':
        
        print("How many courses of {:^0s} did you attend?". format(aine))
        kurssit = int(input())
        course_amount_list.append(kurssit)
        
        input_course_grades_and_calculate_average(aine, kurssit)
        
        print("Enter the next subject:") 
        aine = str(input())   
        subject_list.append(aine)
        
    calculate_averages(grade_average_list, course_amount_list)
    find_strongest_and_weakest_subject(subject_list, grade_average_list)   
    ainekeskiarvo, kurssikeskiarvo = calculate_averages(grade_average_list, course_amount_list)
    vahvinkeski, heikoinkeski, vahvinaine, heikoinaine = find_strongest_and_weakest_subject(subject_list, grade_average_list) 
    kurssikeskiarvo1 = round(kurssikeskiarvo, 1)
    ainekeskiarvo1 = round(ainekeskiarvo, 1)
    vahvinkeski1 = round(vahvinkeski, 1)
    heikoinkeski1 = round(heikoinkeski, 1)
    
        
    print("Average of all subjects is", ainekeskiarvo1, "({:^0s})". format(describe_grade_average(ainekeskiarvo)))
    print("Average of all courses is", kurssikeskiarvo1,"({:^0s})". format(describe_grade_average(kurssikeskiarvo)))
    print("The strongest subject is", vahvinaine , "with average", vahvinkeski1,"({:^0s})". format(describe_grade_average(vahvinkeski)))
    print("The weakest subject is", heikoinaine ,"with average", heikoinkeski1 ,"({:^0s})".format(describe_grade_average(heikoinkeski)))
  
main()  
            