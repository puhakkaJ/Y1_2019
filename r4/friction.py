'''
Created on 23.9.2019

@author: jenni
'''

def calculate_maximum_friction(angle_of_incline, coefficient_of_friction, mass):
    import math

    radiaani = angle_of_incline * math.pi / 180
    g = 9.81
    maksimi = mass * g * math.cos(radiaani) * coefficient_of_friction
    return maksimi
    
def calculate_force_parallel_to_surface(angle_of_incline, mass):
    import math
    
    g = 9.81
    radiaani = angle_of_incline * math.pi / 180
    voima = mass * g * math.sin(radiaani)
    return voima
    
def does_the_block_move(friction, parallel_force):
    if (friction < parallel_force):
        return True
    if (friction > parallel_force):
        return False   
    
def main():
    done = False
    done1 = False
    done2 = False
    print("A block has been set on a tilted surface.")
    print("The program calculates whether the block will start to slide down.")
    rivi = input("What is the angle of inclination of the surface in degrees (0-45)?\n")
    kulma = float(rivi)
    if (kulma < 0) or (kulma > 45):
        while not done:
            rivi = input("What is the angle of inclination of the surface in degrees (0-45)?\n")
            kulma = float(rivi)
            if (kulma <= 45.0) and (kulma >= 0.0):
                done = True
            
    rivi = input("What is the coefficient of friction between the block and the surface (0-1)?\n")
    kerroin = float(rivi)
    if (kerroin < 0) or (kerroin > 1):
        while not done1:
            rivi = input("What is the coefficient of friction between the block and the surface (0-1)?\n")
            kerroin = float(rivi)
            if (kerroin <= 1) and (kerroin >= 0):
                done1 = True
            
    rivi = input("What is the mass of the block (kg)?\n")
    massa = float(rivi)
    if massa <= 0:
        while not done2:
            rivi = input("What is the mass of the block (kg)?\n")
            massa = float(rivi)
            if massa > 0:
                done2 = True
            
    calculate_maximum_friction(kulma,kerroin, massa)
    print("The maximum static frictional force is {:.2f} Newtons". format(calculate_maximum_friction(kulma,kerroin, massa)))
    
    calculate_force_parallel_to_surface(kulma, massa)
    print("The parallel component of the force of gravity is {:.2f} Newtons". format(calculate_force_parallel_to_surface(kulma, massa)))
    
    does_the_block_move(calculate_maximum_friction(kulma,kerroin, massa),calculate_force_parallel_to_surface(kulma, massa))
    
    if does_the_block_move(calculate_maximum_friction(kulma,kerroin, massa),calculate_force_parallel_to_surface(kulma, massa)) == True:
        print("The block will start to slide down.")
        
    if does_the_block_move(calculate_maximum_friction(kulma,kerroin, massa),calculate_force_parallel_to_surface(kulma, massa)) == False:
        print("The block will stay in place.")
        
main()