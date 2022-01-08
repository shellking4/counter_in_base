# -*- coding: utf-8 -*-
from  number import base_number, print_base_number

nb1=base_number.BaseNumber(number=25,base=2,nbp=8)
nb2=base_number.BaseNumber(63,64,8)
nb3=base_number.BaseNumber(62,64,2)
nb4=base_number.BaseNumber(111,16,4)

print("{} in base {}: {}".format(25,2,nb1))
print("{} in base {}: {}".format(63,64,nb2))
print("{} in base {}: {}".format(62,64,nb3))
print("{} in base {}: {}".format(111,16,nb4))

print("______________\nBase 2, 4 positions")
print_base_number.PrintBaseNumber(base=2,nbp=4).print_numbers()
