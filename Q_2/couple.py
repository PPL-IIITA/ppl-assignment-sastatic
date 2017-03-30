from loggingUtility import Store_Log

from math import exp, log10

class Couple:
	def __init__(self, boy, girl):
		self.boy = boy
		self.girl = girl
		self.Gifts = []
		self.happiness = 0
		self.compatibility = 0

	def setHappy(self):
		self.happiness = self.boy.happiness + self.girl.happiness

	def setCompatibility(self):
		self.compatibility = self.boy.budget - self.girl.maintenance + abs(self.boy.attractiveness - self.girl.attractiveness) + abs(self.boy.intelligence - self.girl.intelligence)

	def Gifting(self, GFT) :
		if(self.boy.type == 'Miser'):
			self.boyMiser(GFT)
		if(self.boy.type == 'Generous'):
			self.boyGenerous(GFT)
		if(self.boy.type == 'Geeks'):	
			self.boyGeek(GFT)

	def boyMiser(self, GFT):
		v1 = 0
		v2 = 0
		for g in GFT:
			if (g.price == self.girl.maintenance) or (g.price-self.girl.maintenance<= 100) and (self.boy.budget >= 0) and (self.boy.budget - g.price > 0):
				if (g.type == 'Luxury'):
					v2 = v2 + 2*g.price
				else:
					v2 = v2 + g.price
				v1 = v1 + g.price
				G = {'Type': g.type, 'Price':g.price, 'Value': g.value}
				self.Gifts.append(G)
				print ('type of gift:  ' + G['Type'] + 'Gift Of price: ' + str(G['Price']))
				self.boy.budget = self.boy.budget - g.price
				msg = 'Boy: ' + self.boy.name + '  gave his Girlfriend: ' + self.girl.name + ' a Gift of price = ' + str(g.price) + ' rupees'
				Store_Log(msg)

		if (self.girl.type == 'Choosy'):
			self.girl.happiness = log10(v2)
		elif (self.girl.type == 'Normal'):
			self.girl.happiness = v1
		else:
			self.girl.happiness = exp(v1)
		self.happiness = self.boy.budget
		self.setHappy()
		self.setCompatibility()

	def boyGenerous(self, GFT):
		v1 = 1
		v2 = 1
		for g in GFT:
			if ((g.price == self.boy.budget) or (self.boy.budget-g.price <= 300)) and (self.boy.budget >= 0) and (self.boy.budget - g.price > 0):
				if (g.type == 'Luxury'):
					v2 = v2 + 2*g.price
				else:
					v2 = v2 + g.price
				v1 = v1 + g.price
				G = {'Type': g.type, 'Price':g.price, 'Value': g.value}
				self.Gifts.append(G)
				print ('type of gift:  ' + G['Type'] + 'Gift Of price: ' + str(G['Price']))
				self.boy.budget = self.boy.budget - g.price
				msg = 'Boy: ' + self.boy.name + '  gave his Girlfriend: ' + self.girl.name + ' a Gift of price = ' + str(g.price) + ' rupees'
				Store_Log(msg)

		if (self.girl.type == 'Choosy'):
			self.girl.happiness = log10(v2)
		elif (self.girl.type == 'Normal'):
			self.girl.happiness = v1
		else:
			self.girl.happiness = exp(v1)
		self.happiness = self.boy.budget
		self.setHappy()
		self.setCompatibility()

	def boyGeek(self, GFT):
		v1 = 0
		v2 = 0
		for g in GFT:
			if (g.price == self.self.girl.maintenance) or (g.price-self.self.girl.maintenance <= 100) and (self.boy.budget >= 0) and (self.boy.budget - g.price > 0):
				if (g.type == 'Luxury'):
					v2 = v2 + 2*g.price
				else:
					v2 = v2 + g.price
				v1 = v1 + g.price
				G = {'Type': g.type, 'Price':g.price, 'Value': g.value}
				self.Gifts.append(G)
				print ('type of gift:  ' + G['Type'] + 'Gift Of price: ' + str(G['Price']))
				self.boy.budget = self.boy.budget - g.price
				msg = 'Boy: ' + self.boy.name + '  gave his Girlfriend: ' + self.girl.name + ' a Gift of price = ' + str(g.price) + ' rupees'
				Store_Log(msg)

		for i in GFT:
			if (i not in self.Couple.Gifts) and (i.type == 'luxury') and (i.price <= self.boy.budget):
				v2 = v2 + 2*i.price
				v1 = v1 + i.price
				G = {'Type': g.type, 'Price':g.price, 'Value': g.value}
				self.Gifts.append(G)
				print ('type of gift:  ' + G['Type'] + 'Gift Of price: ' + str(G['Price']))
				self.boy.budget = self.boy.budget - g.price
				msg = 'Boy: ' + self.boy.name + '  gave his Girlfriend: ' + self.girl.name + ' a Gift of price = ' + str(g.price) + ' rupees'
				Store_Log(msg)
				break


		if (self.girl.type == 'Choosy'):
			self.girl.happiness = log10(v2)
		elif (self.girl.type == 'Normal'):
			self.girl.happiness = v1
		else:
			self.girl.happiness = exp(v1)
		self.happiness = self.boy.budget
		self.setHappy()
		self.setCompatibility()
