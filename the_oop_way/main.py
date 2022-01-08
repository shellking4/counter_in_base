# -*- coding: utf-8 -*-
import sys
from  number import base_number, print_base_number

args = sys.argv[1:]
get = False

if len(args) == 0:
	#Pas d'argument en ligne de commande, on recupère
	base = input("The base: ")
	nbp = input("Number of positions: ")

	#Conversion en entier
	try :
		base = int(base)
		nbp = int(nbp)
		get = True
	except :
		print("Please, give integers as arguments")


elif len(args) == 2 :
	#Presence de deux argument en ligne de commande, conversion en entier
	try :
		base = int(args[0])
		nbp = int(args[1])
		get = True
	except :
		print("Please, give integers as arguments")
else :
	#Présence d'un nombre incorrect d'arguments
	print("Program needs 2 arguments")


#Bien récuperés
if get :
	if  2 <= base and base <= 64 :
		#On affiche les nombres
		print_base_number.PrintBaseNumber(base,nbp).print_numbers()
	else:
		print("Please, give a base between 2 and 64.")