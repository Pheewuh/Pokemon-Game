import random
from time import sleep
import msvcrt as m

myhealth=60
opponenthealth=50
attack1=10
attack2=15
attack3=20
attackturn=0
opponentpotioncount=2
mypotioncount=2
endgame=0
opponentpokemon='a'
mypokemon='b'

print("Mainmenu options:'play','edit'"); sleep(0.5)
print("Gameplay options:'attack','potion','pokeball','flee','end'"); sleep(0.5)
print("Edit options:'attack1','attack2','attack3','myhealth','opponenthealth'"); sleep(0.5)
print('Press enter to start')

def gamestart():
	m.getch()
	mainmenu()

def mainmenu():
	global opponentpokemon
	global mypokemon
	gamechoice=input('What do you want to do? :')
	if gamechoice=='play':
		mypokemon=input("Your pokemon's name is:") ; 
		opponentpokemon=input("Opponent's pokemon's name:")
		gameplay()
	elif gamechoice=='edit':
		editmenu()
	else:
		print('Invalid')

def gameplay():
	global mypokemon
	global opponentpokemon
	global attackturn
	while attackturn<10:
		while opponenthealth>0 and myhealth>0:
			while endgame==0:
				actionchoice()
				if endgame==0 and opponenthealth>0:
					opponentaction()
				else:
					pass
				if myhealth<=0:
					print(mypokemon+' fainted')
					attackturn=10
				elif opponenthealth<=0:
					print(opponentpokemon+' fainted')
					attackturn=10
				else:
					pass
			attackturn+=1

def editmenu():
	attack1edit=input('Do you want to edit attack1?')
	if attack1edit=='yes':
		attack1=int(input('Attack1:'))
	else:
		pass
	attack2edit=input('Do you want to edit attack2?')
	if attack2edit=='yes':
		attack2=int(input('Attack2:'))
	else:
		pass
	attack3edit=input('Do you want to edit attack3?')
	if attack3edit=='yes':
		attack3=int(input('Attack3:'))
	else:
		pass
	myhealthedit=input('Do you want to edit your pokemon health?')
	if myhealthedit=='yes':
		myhealth=int(input('Myhealth:'))
	else:
		pass
	opponenthealthedit=input('Do you want to edit opponent pokemon health?')
	if opponenthealthedit=='yes':
		opponenthealth=int(input('Opponenthealth:'))
	else:
		pass

def opponentaction():
	global opponentpotioncount
	global opponenthealth
	if opponenthealth>20:
		opponentattack()
	else:
		if opponentpotioncount>0:
			opponentpotion()
			opponentpotioncount-=1
		else:
			opponentattack()


def actionchoice():
	global attackturn
	choice=input('Choose action:')
	if choice=='attack':
		myattack()
	elif choice=='potion':
		mypotion()
	elif choice=='pokeball':
		pokeball()
	elif choice=='flee':
		flee()
	elif choice=='end':
		endgame1()
	else:
		print('Invalid action')

def myattack():
    global opponenthealth
    attackcode=int(input('Attack code:'))
    if attackcode==1:
        opponenthealth-=attack1
        print(mypokemon+' used Electro Ball')
    elif attackcode==2:
        opponenthealth-=attack2
        print(mypokemon+' used Thunder Bolt')
    elif attackcode==3:
        opponenthealth-=attack3
        print(mypokemon+' used Lightning Strike')
    else:
        print('Invalid attack code')
    print(opponentpokemon+' has '+opponenthealth+' hp left')

def opponentattack():
	global opponentpokemon
	global myhealth
	randomattack=random.randint(1,3)
	if randomattack==1:
		myhealth-=attack1
		print(opponentpokemon+' used Ember')
	elif randomattack==2:
		myhealth-=attack2
		print(opponentpokemon+' used Fire Spin')
	elif randomattack==3:
		myhealth-=attack3
		print(opponentpokemon+' used Flamethrower')
	else:
	    pass
	print(mypokemon+' has'+myhealth+' hp left')

def mypotion():
	global mypotioncount
	global myhealth
	myhealth+=20
	mypotioncount-=1
	print(mypokemon+' used a potion')
	print(mypokemon+' restored 20 hp')	

def opponentpotion():
	global opponenthealth
	opponenthealth+=20
	print(opponentpokemon+' used a potion')
	print(opponentpokemon+' restored 20 hp')

def pokeball():
	global endgame
	if opponenthealth<=20:
		catchchance=random.randint(1,3)
		print(catchchance)
		if catchchance==2:
			print('Successful')
			endgame=1
		else:
			print('Unsuccessful')
	else:
		print('Unsuccessful')

def  flee():
	global endgame
	print('You successfully ran away')
	endgame=1

def endgame1():
	global endgame
	print('Program ended')
	endgame=1

#myattack()	
#opponentattack()
#mypotion()
#opponentpotion()
#pokeball()
#actionchoice()
#gameplay()
#endgame1()
#mainmenu()
#editmenu
gamestart()