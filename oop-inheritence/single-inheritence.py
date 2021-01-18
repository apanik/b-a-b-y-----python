class Car(object):
	# __init__ is a constructor which allocates memory for class variable
	def __init__(self,name):
		self.name = name

	def get_name(self):
		return self.name

	def is_SportsCar(self):
		print(False)

class SportsCar(Car):

	def is_SportsCar(self):
		print(True)

car_obj = Car("Toyota")
sports_car_obj = SportsCar("Lumborgini")

car_obj.is_SportsCar()
sports_car_obj.is_SportsCar()

#UNDERSTANDING 


"""
Single inheritance: When a child class inherits from only one parent class, 
it is called single inheritance. We saw an example above.
"""