import random 
import csv
from testingUtility import *
from boy import Boy
from girl import Girl
from couple import Couple
from loggingUtility import Store_Log


print("No of Girls and Boys")
n = int(input())

boy_list=generateBoys(n)

girl_list=generateGirls(n)

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

couple_list=Couplify(girl_list, boy_list)
for k in couple_list:
	print (k.boy.name+' committed with ' +k.girl.name)