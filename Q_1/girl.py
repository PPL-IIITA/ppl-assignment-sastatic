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

	def is_eligible(self, boy, m):
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

	def setPartner(self, partner):
		self.partner = partner
		self.status = "Committed"