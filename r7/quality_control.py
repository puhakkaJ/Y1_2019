'''
Created on 16.10.2019

@author: jenni
'''

def main():
    p = 0
    k = 0
    s = 0
    maara = 0
    
    filename = input("Enter the name of the file to be read:\n")
    try:
        product_file = open(filename,'r')
        for line in product_file:
            line = line.rstrip()
            measure = float(line)
            maara += 1
            
            if measure >= 4.52 and measure <= 4.58:
                p += 1
                
            elif measure >= 4.50 and measure <= 4.60:
                k += 1
                
            else:
                s += 1
                    
        product_file.close()
        pprosentti = p/maara * 100
        kprosentti = k/maara * 100
        sprosentti = s/maara * 100

        print("File read succesfully.")
        print("The batch contained:")
        print("{:d} optimal ({:>.1f}%)".format(p, pprosentti))
        print("{:d} allowed ({:>.1f}%)".format(k, kprosentti))
        print("{:d} faulty ({:>.1f}%)".format(s, sprosentti))
        
        if sprosentti >= 3.0:
            print("The batch didn't pass the quality inspection.")
            
        else:
            print("The batch passed the quality inspection.")    



    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))
    except ValueError:
        print("Incorrect number in the file '{:s}'. Program ends.".format(filename))

main()