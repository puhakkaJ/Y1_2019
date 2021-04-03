# Y1 AUTUMN 2019
# Basic Course in Programming Y1
# Author: Joel Lahenius
# Template for Exercise 3.X Geostationary Orbit

G = 6.6741e-11 # (N * m ** 2) / (kg ** 2)  ==  (m ** 3) / (kg * s ** 2)
from math import pi # = 3.14159265358979...

"""
Needed equations:

v == w * r

w == (2*pi) / sidereal_day_length_in_seconds

a_c == (w ** 2) * r == (v ** 2) / r

a_g == (m * G) / (r ** 2)

a_c == a_g

a_c == a_g in solved form:

r == ((m * G) / (w ** 2)) ** (1/3)
  
Explanations:
w == angular velocity, 1 / s (rad / s) - short symbol for "omega"
v == orbital velocity, m / s
r == radius of the orbit, m
m == mass of the planet, kg

a_g == gravitational acceleration, m / (s**2)
a_c == centripetal acceleration, m / (s**2)

G == gravitational constant (value and units given above)


Calculate:
- v (in km/s)
- r (in km)

"""

# Float function is able to read numbers in exponential format as well, for instance:
# thousand = float("1e3") # == 1 * 10 ** 3 == 1000
# very_small_number = float("5.9e-9")   # == 5.9 * 10 ** -9

def main():
    rivi = input("Enter the mass of the planet (kg):\n")
    m = float(rivi)
    rivi = input("Enter the length of the (sidereal) day of the planet (hours):\n")
    siideri = float(rivi)
    w = ( 2 * pi ) / ( siideri * 3600 )
    r = ( ( m * G) / ( w ** 2 )) ** ( 1/3 )
    print("The radius of the geostationary orbit is {:.0f} km.". format( r / 1000 ))
    v = w * r    

    print("The orbital speed is{:.2f} km / s.". format( v / 1000 ))
    
    rivi = input("Enter the equatorial radius of the planet (km):\n")
    säde = float(rivi)
    d = ( r / 1000 ) - säde
    print("The height of the orbit above the equator is {:.0f} km". format(d))
    

main()