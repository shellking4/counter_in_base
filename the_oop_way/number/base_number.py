# -*- coding: utf-8 -*-
import math

class BaseNumber:
	"""
	Un nombre dans une base donnée sur un nombre positons
	Les attributs :
		- number : le nombre en base 10
		- base : la base
		- nbp : nombre de position 

	"""

	def __init__(self, number,base,nbp):
		self.number = number
		self.base = base
		self.nbp = nbp

	def get_position_value(self,position):
		"""
		Calcule la valeur se trouvant à la position specifiée quand 
		quand on écrit dans la base self.base 
		(c'est la valeur du bit dans le cas de base 2
		 ou du chiffre des unités, dizaine, ... dans le cas de base 10 )

		On suppose que les positions sont numerotées de 0 a nbp-1
		de la droite vers la gauche

		Cette valeur s'obtient en :
			- faisant une division entière du nombre par la base 
			  élévée à la puissance la position
			- le resultat modulo la base donne la valeur
			(cette observation découle du cas base 10) 

		Exemple :
			n = 1782
			On veut récuperer le chiffre des centaines 
			qui se trouve à la position 2

			 Etape 1 : division entière :
			 	1782 / 10^2 = 1782/100 = 17 
			 Etape 2 : modulo la base
			 	17 % 10 = 7

			Le chiffre des centaines est bien 7.
		"""
		return int(self.number/math.pow(self.base,position))%self.base


	def value_to_real_forme(self,value):
		"""
			Détermine le caractère associé à la valeur de la position

			entrée :
			   - valeur (entier) : valeur de la position entre 0 et 63
			sortie :
			   - un caractère : 0-9 ou a-z ou A-Z ou @ ou /

		"""
		if value <= 9:
			# 0 to 9
			return  str(value)
		elif value <= 35:
			# a to z
			return chr(ord("a")+value-10)
		elif value <= 61:
			# A to Z
			return chr(ord("A")+value-36)
		elif value == 62:
			# @
			return "@"
		else:
			# /
		 	return "/"

	def __str__(self):
		"""
			Ecrit le nombre dans la base donnée

			sortie :
			- chaine de caractère représentant le nombre dans la base 

			Connaissant le nombre de positons (nbp), il suffit de recupérer la
			valeur des positions nbp-1, nbp-2, ... , 2,1,0 et les
			concatener dans la chaine de sortie (number_in_given_base)
		"""
		number_in_given_base=""
		position_value=0 
		position_reel_value_form="" 

		for p in range(self.nbp):
			#Recupération de la valeur entre 0 et 63
			position_value = self.get_position_value(self.nbp-1-p)

			#Détermination du caractère associée : 0-9 ou a-z ou A-Z ou @ ou /
			position_reel_value_form = self.value_to_real_forme(position_value)

			#Concatenation
			number_in_given_base += position_reel_value_form

		return number_in_given_base