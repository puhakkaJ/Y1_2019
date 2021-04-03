# Y1 AUTUMN 2019
# Basic Course in Programming Y1
# Author: Joel Lahenius
# Template for Exercise 9.2 Coffee containers

from container import LiquidContainer

def main():
    print("Press enter to continue in the story.")
    input()
    rivi = input("Big coffee cup name and volume: ")
    rivi = str(rivi)
    rivi = rivi.split("/")
    isokuppi = str(rivi[0])
    tilavuus1 = float(rivi[1])
    isokahvikuppi = LiquidContainer(isokuppi,tilavuus1,False)
    
    rivi = input("Small coffee cup name and volume: ")
    rivi = str(rivi)
    rivi = rivi.split("/")
    pikkukuppi = str(rivi[0])
    tilavuus2 = float(rivi[1])
    pienikahvikuppi = LiquidContainer(pikkukuppi,tilavuus2,False)
    
    rivi = input("Coffee jug name and volume: ")
    rivi = str(rivi)
    rivi = rivi.split("/")
    kahvipannu1 = str(rivi[0])
    tilavuus3 = float(rivi[1])
    kahvipannu = LiquidContainer(kahvipannu1,tilavuus3,True)
    print("Created the following containers:")
    print(isokahvikuppi)
    print(pienikahvikuppi)
    print(kahvipannu)
    input()
    print("Filling {:s}...".format(kahvipannu1))
    kahvipannu.fill()
    print("Jug status after filling:")
    print(kahvipannu)
    input()
    amount_to_be_served = float(input("How many litres of coffee should be served?\n"))
    print("Trying to pour {:.2f} litres from {:s} into {:s} and {:s}".format(amount_to_be_served,kahvipannu1,isokuppi,pikkukuppi))
    maara1 = kahvipannu.pour_to_another(isokahvikuppi,amount_to_be_served)
    
    maara2 = kahvipannu.pour_to_another(pienikahvikuppi,amount_to_be_served)
    print("Managed to pour {:.2f} litres to {:s}".format(maara1,isokuppi))
    print("Managed to pour {:.2f} litres to {:s}".format(maara2,pikkukuppi))
    input()
    print("Cup and jug statuses after pouring:")
    print(isokahvikuppi)
    print(pienikahvikuppi)
    print(kahvipannu)
    input()
    if isokahvikuppi.get_liquid_volume() == pienikahvikuppi.get_liquid_volume():
        print("Both were happy for having the same amount of coffee and lived happily everafter.")
    else:
        print("The holder of {:s} became angry for having less coffee and flipped their coffee cup!".format(pikkukuppi))
        pienikahvikuppi.flip()
        print("All of their coffee poured out:")
        print(pienikahvikuppi)
        input()
        print("They also flipped the jug!")
        kahvipannu.flip()
        print("However, it had a lid, so the liquid stayed inside:")
        print(kahvipannu)
        input()
        print("So they had to force flip to the jug!")
        kahvipannu.force_flip()
        print("Now it's empty and no longer has a lid:")
        print(kahvipannu)
        input()
        print("Next they got mad and nicked all the coffee they could from {:s}".format(isokuppi))
        maara = isokahvikuppi.pour_to_another(pienikahvikuppi, tilavuus2)
        print("{:.2f} litres were stolen.".format(maara))
        input()
        print("Cup statuses after the theft:")
        print(isokahvikuppi)
        print(pienikahvikuppi)
        input()
        print("Now finally the holder of {:s} can drink their coffee:".format(pikkukuppi))
        pienikahvikuppi.flip()
        print(pienikahvikuppi)
    
main()