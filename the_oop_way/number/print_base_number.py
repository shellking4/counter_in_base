# -*- coding: utf-8 -*-
import math
from  number import base_number

class PrintBaseNumber:
	"""docstring for ClassName"""
	def __init__(self, base,nbp):
		self.base = base
		self.nbp = nbp
		self.max = 0

		for i in range(nbp):
			"""
			Calcule le nombre  maximal qu'on peut écrire sur 
			nbp positions dans la base "base"

			Ce max s'obtient en mettant toutes les positions à base-1

			Exemple :
				Pour base = 10 et nbp = 5, on a
				max = 99999
			"""
			self.max += int(math.pow(self.base,i))* (self.base-1)  

	def print_numbers(self):
		"""
		Affiche en base "base" les nombres de 0 à max 
		"""
		for n in range(self.max+1):
			print(base_number.BaseNumber(n,self.base,self.nbp))
