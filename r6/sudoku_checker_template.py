# Y1 AUTUMN 2019
# Basic Course in Programming Y1
# Author: Vilma Kahri
# Template for exercise 6.X

from grids import GRID_NAMES, GRID_RETURNS, GRIDS, GRIDS_BIG, GRIDS_SMALL

GRID_SIZE = 9 # Length of one side of the sudoku
SUBGRID_SIZE = 3 # Length of one side of a cell of the sudoku

def check_sudoku_grid(grid):
    for rivi in range(0,9):
            d = {}
            for pysty in range(0,9):
                tarkistus = grid[rivi][pysty]
                if tarkistus != 0 and tarkistus in d and tarkistus != None:
                    return False
                d[tarkistus] = 1
             
    for pysty in range(0,9):
        d = {}    
        for rivi in range(0,9):
            tarkistus = grid[rivi][pysty] 
            if tarkistus != 0 and tarkistus in d and tarkistus != None:
                return False
            d[tarkistus] = 1
                
    for i in range(0,3):
        for j in range(0,3):
            d = {}
            for ii in range(0,3):
                for jj in range(0,3):  
                    rivi = (3*i)+ii
                    pysty = (3*j)+jj 
                    tarkistus = grid[rivi][pysty]
                    if tarkistus !=0 and tarkistus in d and tarkistus != None:
                        return False
                    d[tarkistus] = 1
                        
    return True                
            
def print_grid(grid):
    for i in range(GRID_SIZE):
        row = ""
        for j in range(GRID_SIZE):
            try:
                val = int(grid[i][j])
            except TypeError:
                val = "_"
            except ValueError:
                val = grid[i][j]
            row += "{} ".format(val)
            if j % SUBGRID_SIZE == SUBGRID_SIZE - 1:
                row += " "
        print(row)
        if i % SUBGRID_SIZE == SUBGRID_SIZE - 1:
            print()

def main():
    i = 0
    for grid in GRIDS:
        is_valid = check_sudoku_grid(grid)
        print("This grid {:s}.".format(GRID_NAMES[i]))
        print("Your function should return:  {:s}".format(GRID_RETURNS[i]))
        print("Your function returns:        {}".format(is_valid))
        print_grid(grid)
        i += 1
    
main()