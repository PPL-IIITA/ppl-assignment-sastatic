import random 
import csv
from testingUtility import *
from boy import Boy
from girl import Girl
from couple import Couple
from loggingUtility import Store_Log
from gift import Gift

print("No of Girls:")
n = int(input())
boy_list=generateBoys(n)

print("No of Boys:")
n = int(input())
girl_list=generateGirls(n)

print("No of Gifts:")
n = int(input())
gift_list=generateGifts(n)


def setPartner(b, g):
	b.partner = g
	g.partner = b
	b.status = "Committed"
	g.status = "Committed"
	b.Couple = Couple(b, g)
	g.Couple = Couple(b, g)


def Couplify(girl_list, boy_list):
	couple_list=[]
	for g in  girl_list:
		for b in  boy_list:
			newC = 0
			for m in range(10, 0, -1):
				if g.status == 'single' and b.status=='single' and g.is_eligible(b, m) and b.is_eligible(g):
					setPartner(b,g)
					couple_list +=[Couple(b, g)]
					Store_Log(g.name +' and ' + b.name + '  are commited now.')
					newC = 1
					break
				else:
					break
			if(newC):
				break
	return couple_list

couples=Couplify(girl_list, boy_list)
print ('\n\n\n')


for c in couples:
	print ('The given Gift to '+c.girl.name+' by '+c.boy.name+' are: ')
	Couple.Gifting(c, gift_list)
print ('\n\n\n')



k = random.randint(1, n/10)

def printHappyCouple(C, k):
	A = sorted(C, key=lambda item: item.happiness, reverse=True)
	print (str(k) + ' most Happy couples:')
	for i in range(k):
		print (A[i].boy.name + ' and ' + A[i].girl.name)
	print ('\n')

def printCompatibleCouple(C, k):
	B = sorted(C, key=lambda item: item.compatibility, reverse=True)
	print (str(k) + ' most Compatible couples:')
	for i in range(k):
		print (B[i].boy.name + ' and ' + B[i].girl.name)
	print ('\n')

printHappyCouple(couples, k)
printCompatibleCouple(couples, k)

