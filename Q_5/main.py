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
boy_list=sorted(boy_list, key=lambda item: item.attractiveness)

print("No of Boys:")
n = int(input())
girl_list=generateGirls(n)
girl_list=sorted(girl_list, key=lambda item: item.maintenance)

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

couple_list=[]
for k in range(0, max(len(boy_list),len(girl_list))):
	if(k<len(girl_list)):
		for b in  boy_list:
			newC = 0
			for m in range(10, 0, -1):
				if girl_list[k].status == 'single' and b.status=='single' and girl_list[k].is_eligible(b, m) and b.is_eligible(girl_list[k]):
					setPartner(b,girl_list[k])
					couple_list +=[Couple(b, girl_list[k])]
					Store_Log(girl_list[k].name +' and ' + b.name + '  are commited now.')
					newC = 1
					break
				else:
					break
			if(newC):
				break
	if(k<len(boy_list)):
		for g in  girl_list:
			newC = 0
			if g.status	 == 'single' and boy_list[k].status=='single' and g.is_eligible(boy_list[k]) and boy_list[b].is_eligible(g):
				setPartner(boy_list[k],g)
				couple_list +=[Couple(boy_list[k], g)]
				Store_Log(g.name +' and ' + boy_list[k].name + '  are commited now.')
				newC = 1
				break
			else:
				break
			if(newC):
				break

girls=sorted(girl_list, key=lambda item: item.attractiveness, reverse=True)



for c in couple_list:
	Couple.Gifting(c, gift_list)
print ('\n\n\n')


print("For k happiest couple, Value of k:")
k=int(input())

def printHappyCouple(C, k):
	A = sorted(C, key=lambda item: item.happiness, reverse=True)
	print (str(k) + ' most Happy couples:')
	for i in range(k):
		print (A[i].boy.name + ' and ' + A[i].girl.name)
	print ('\n')

printHappyCouple(couple_list, k)

