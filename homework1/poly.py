class Polynomial:

	def __init__(self, coefficients): #have to pass self as a parameter
		self.coefficients = coefficients

	def __str__(self):
		result = ""
		for (e, c) in self.coefficients.items(): #have to iterate thru items
			result += "+({})x^{}".format(c, e)
		return result

	def evaluate(self, x):
		if not self.coefficients: # check if input is empty
			return False

		result = 0
		max_key = max(self.coefficients)

		for d in range(max_key + 1, -1, -1):
			
			if d - 1 in self.coefficients:
				next_degree_c = self.coefficients[d - 1]
			else:
				next_degree_c = 0
			
			if (d - 1 > 0):
				result = (result + next_degree_c) * x
			else:
				result += next_degree_c

		return result

		


