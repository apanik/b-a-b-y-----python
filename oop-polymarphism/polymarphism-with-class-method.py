"""
Below code shows how
python can use two different class types, 
in the same way. 
We create a for loop 
that iterates through a tuple of objects. 
Then call the methods without being concerned about
which class type each object is. 
We assume that these methods actually exist in each class.
"""

class Bangladesh():

	def get_capital(self):
		print("Dhaka is the Captial of Bangladesh")

	def get_language(self):
		print("Bangla is the Mother tounge of Bangladesh")

class India():

	def get_capital(self):
		print("Delhi is the Captial of India")

	def get_language(slef):
		print("Hindi is the Mother tounge of India")

bd_obj =  Bangladesh()
ind_obj = India()

for element in (bd_obj,ind_obj):
	element.get_capital()
	element.get_language()
