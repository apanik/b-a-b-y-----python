class ParentA(object):
	# __init__ is a constructor which allocates memory for class variable
	def __init__(self):
		self.strOne = " Ping from Parent A class"

class ParentB(object):
    # __init__ is a constructor which allocates memory for class variable
	def __init__(self):
		self.strTwo = " Ping from Parent B class"


class Child(ParentA,ParentB):
    # __init__ is a constructor which allocates memory for class variable
	def __init__(self):
		ParentA.__init__(self)
		ParentB.__init__(self)
	
	def sayDerived(self):
		print(f"Hello from Child class saying{self.strOne} and then{self.strTwo}")
    
    

obj = Child()

obj.sayDerived()

# UNDERSTANDING 

"""
When a child class inherits from multiple parent classes, 
it is called multiple inheritance. 
"""