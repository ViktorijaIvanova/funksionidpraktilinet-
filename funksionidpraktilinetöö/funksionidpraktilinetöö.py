from random import *
from math import *
from Omamoodul import *
#1
vastus=arithmetic(float(input("arv1:")), input("tehe:"), float(input("arv2:"))) 
print(vastus)
#2
while True:
	
	def is_year_leap(x):
		
		if x%4 == 0:
			if x%400 == 0:
				print('True')
			elif x%100 != 0:
				print('True')
			else:
				print('False')
		else:
			print('False') 
			
	is_year_leap(int(input('Введите год: '))) 
	#3

