class Girl:
	def __init__(self, name, attractiveness, intelligence, maintenance, criteria, type):
		self.name = name
		self.attractiveness = attractiveness
		self.intelligence = intelligence
		self.maintenance = maintenance
		self.criteria = criteria
		self.type = type
		self.status = "single"
		self.happiness = 0

	def is_eligible(self, boy, m=1):
		if (self.maintenance <= boy.budget):
			if(self.criteria == 'Rich'):
				if(boy.budget >= m):
					return True
			if(self.criteria == 'Attractive'):
				if(boy.attractiveness >= m):
					return True
			if(self.criteria == 'Intelligent'):
				if(boy.intelligence >= m):
					return True

		else:
			return False

	def setHappy(girl,gift):
		if(girl.types == 'Choosy'):
			girl.happiness(gift)
		if(girl.types == 'Normal'):
			girl.happinessNormal(gift)
		if(girl.types == 'Desperate'):
			girl.happinessDesperate(gift)
