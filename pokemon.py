import random
import msvcrt
from time import sleep

class mygame:
	def __init__(self,healths,attacks,attnames,choices,bag,):
		self.healths=healths
		self.attacks=attacks
		self.bag=bag
		self.choices=choices
		self.attnames=attnames

	def myattack(self):
		self.choice=int(input('1.Thunderbolt\n2.Lightning Tail\n3.Electro Ball'))
		self.healths[1]-=self.attacks[self.choices.index(self.choice)]
		print('Pikachu used '+self.attnames[self.choices.index(self.choice)])
		print('Charizard has '+str(self.healths[1])+' HP left')
		
		self.chance=0

	def oppattack(self):
		self.choice=random.randint(1,3)
		self.healths[0]-=self.attacks[self.choices.index(self.choice)]
		print('Charizard used '+self.attnames[self.choices.index(self.choice)+3])
		print('Pikachu has '+str(self.healths[0])+' HP left')

	def mypotion(self):
		if self.bag[0]>0:
			self.potionstat=60-self.healths[0]
			self.bag[0]-=1
			if self.potionstat<20:
				self.healths[0]+=self.potionstat
			else:
				self.healths[0]+=20
			print('Pikachu used a potion')
			print('Pikachu has '+str(self.healths[0])+' HP left')
		else:
			print('No potions available')
			self.myattack()

	def opppotion(self):
		if self.bag[1]>0:
			self.bag[1]-=1
			self.potionstat=50-self.healths[1]
			if self.potionstat<20:
				self.healths[1]+=self.potionstat
			else:
				self.healths[1]+=20
			print('Charizard used a potion')
			print('Charizard has '+str(self.healths[1])+' HP left')
		else:
			self.oppattack()

	def pokeballaction(self):
		if self.chance==2:
			print('Pokemon Caught!')
			quit()
		else:
			print('The pokemon escaped the pokeball')

	def pokeball(self):
		if self.bag[2]>0:
			if self.healths[1]<20:
				self.chance=random.randint(1,5)
				self.pokeballaction()
			else:
				self.chance=random.randint(1,10)
				self.pokeballaction()
		self.bag[2]-=1


	def oppactions(self):
		if self.healths[1]>20:
			self.oppattack()
		else:
			self.opppotion()

	def myactions(self):
		self.choice=input('Attack,Potion,Pokeball,Flee')
		if self.choice.lower()=='attack':
			self.myattack()
		elif self.choice.lower()=='potion':
			self.mypotion()
		elif self.choice.lower()=='pokeball':
			self.pokeball()
		elif self.choice.lower()=='flee':
			print('You ran away')
			quit()

	def gameplay(self):
		while self.healths[0]>0 and self.healths[1]>0:
			self.myactions()
			if self.healths[1]>0:
				self.oppactions()
			else:
				print('Opponent fainted')
			if self.healths[0]<=0:
				print('You fainted')

Game=mygame([60,50],[10,15,20],['Thunder Bolt','Lightning Tail','Electro Ball','Fire Ball','Flamethrower','Amber burst'],[1,2,3],[2,2,2])

Game.gameplay()
