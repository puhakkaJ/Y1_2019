'''
Created on 13.9.2019

@author: jenni
'''
def main():

    print("Welcome to the fair cookie distribution calculator!")
    rivi = input("How many cookies are there?\n")
    keksit = int(rivi)
    rivi = input("How many children eating?\n")
    lapset = int(rivi)
    rivi = input("How many adults eating?\n")
    aikuiset = int(rivi)
    aikuisille = keksit // aikuiset
    kaikille = keksit // ( aikuiset + lapset )
    lapsille = keksit // lapset
    i = 1   
    done = False
    done1 = False
    
    if keksit % lapset == 0:
        print("The cookies can be evenly distributed for the children -", lapsille , "each!")
        done1 = True
        
    if keksit % aikuiset == 0:
        print("The cookies can be evenly distributed for the adults -", aikuisille , "each!")
        done1 = True 
        
    if keksit % ( aikuiset + lapset ) == 0:
        print("The cookies can be evenly distributed for everybody -", kaikille , "each!")
        done1 = True
        
    if ( keksit -  aikuiset ) % lapset  == 0 and aikuiset + lapset != keksit:
        print ("The cookies can be distributed so that each adult gets 1 cookies and each child gets", int((keksit - aikuiset) / lapset) , "cookies!")
        done1 = True
        
    elif ( keksit -  aikuiset ) % lapset  != 0:
        done = False
        while  (i * aikuiset <= keksit) and not done:
            i = i + 1
            k = int(( keksit - i * aikuiset ) / lapset)      


            if ( keksit -  i * aikuiset ) % lapset == 0 and i != k and i > 0 and k > 0:

                done = True
                
                
              
                print("The cookies can be distributed so that each adult gets", i ,"cookies and each child gets", k ,"cookies!")
                
            
    if not done and not done1:  
        print("The cookies cannot be distributed evenly in any way :(")

main()   
    
        