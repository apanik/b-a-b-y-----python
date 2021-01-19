class SoftwareEngineer:
    # constructor
    def __init__(self, name):
        self.name = name
        # protected variable
        self._no_of_bugs_solved = None
        # private variable
        self.__salary = None

    # instance method
    def get_name(self):
        return self.name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value in range(1, 10):
            self.__salary = value * 2
        else:
            self.__salary = value * 3

    @salary.deleter
    def salary(self):
        del self.__salary


new_obj = SoftwareEngineer("Anik")
new_obj.salary = 30000
del new_obj.salary
print(new_obj.salary)

