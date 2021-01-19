class SoftwareEngineer:
	# class variable
    motto = "Class Variable"
    # __init__ method(constructor) allocates memory for variable
    def __init__(self,name,age,level):
    	self.name = name
    	self.age = age
    	self.level = level

    # Instance Method
    def get_name(self):
        print(f"Employee Name is {self.name}") 
    
    # Static Method
    @staticmethod
    def languages(language):
    	print(f"code in {language}")
    
    # Specail Dunder Method
    def __eq__(self,other):
    	return True if self.name == other.name and self.age==other.age and self.level == other.level else False

# new object/constructor of SoftwareEngineer Class 
obj1 = SoftwareEngineer("Anik",25,"Jr Software Engineer")
obj2 = SoftwareEngineer("Anik",25,"Jr Software Engineer")


obj1.languages("Python")
print(obj1.__eq__(obj2))   

