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

for c in couples:
	print ('The given Gift to '+c.girl.name+' by '+c.boy.name+' are: ')
	Couple.Gifting(c, gift_list)
print ('\n\n\n')


print ('\ntotal Genereted Couple: '+str(len(couples))+'\n')



print("Enter value of k which is less then total generated couple: ")
k = int(input())

def breakup(Cpl, k):
	Cpl = sorted(Cpl, key=lambda item: item.happiness)
	print (str(k) + ' least Happy couples:')
	for i in range(k):
		print (Cpl[0].boy.name + ' and ' + Cpl[0].girl.name + ' Are breaking up...')
		Store_Log(g.name +' and ' + b.name + '  are broke-up now.')
		Cpl[0].boy.afterBreakup()
		Cpl[0].girl.afterBreakup()
		Cpl.pop(0)
	print ('\n')

breakup(couples, k)

