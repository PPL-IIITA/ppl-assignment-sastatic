class Boy:
	def __init__(self, name, attractiveness, intelligence, budget, requirements, type):
		self.name = name
		self.attractiveness = attractiveness
		self.intelligence = intelligence
		self.budget = budget
		self.type = type
		self.requirements = requirements
		self.status = "single"
		self.happiness = 0


	def is_eligible(self, girl):
		if (self.budget >= girl.maintenance):
			if(self.requirements!=0):
				if(self.requirements <= girl.attractiveness):
					return False
			return True
		else:
			return False
