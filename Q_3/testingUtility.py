import random 
import csv
from couple import Couple
from boy import Boy
from girl import Girl
from gift import Gift

def generateBoys(n):
	boy_types = ['Miser','Generous','Geek']
	boys=[]
	fd1 = open('./Boys.csv','w')
	writer = csv.writer(fd1, delimiter = ',')
	for i in range(0,n):
		b=[Boy('Boy'+str(i), random.randint(1, 11), random.randint(1, 11), random.randint(1, 11), random.randint(1, 11), boy_types[random.randint(0,2)])]
		boys+=b
		writer.writerow(b)
	fd1.close()
	return boys

def generateGirls(n):
	girl_types = ['Choosy','Normal','Desperate']
	criteria = ['Attractive', 'Rich', 'Intelligent']
	girls=[]
	fd2 = open('./Girls.csv','w')
	writer = csv.writer(fd2, delimiter = ',')
	for i in range(0,n):
		g=[Girl('Girl'+str(i), random.randint(1, 11), random.randint(1, 11), random.randint(1, 11), criteria[random.randint(0,2)], girl_types[random.randint(0,2)])]
		girls+=g
		writer.writerow(g)
	fd2.close()
	return girls

def generateGifts(n):
	gift_types = ['Essential','Luxury','Utiltiy']
	gifts = []
	fd3 = open('./Gifts.csv', 'w')
	writer = csv.writer(fd3, delimiter = ',')
	for i in range(0,n):
		g=[Gift(random.randint(1, 11), random.randint(1, 11), gift_types[random.randint(0,2)])]
		gifts+=g
		writer.writerow(g)
	fd3.close()
	return gifts
