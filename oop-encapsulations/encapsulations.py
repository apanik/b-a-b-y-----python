class SoftwareEngineer:
    # constructor
    def __init__(self, name):
        self.name = name
        # protected variable
        self._no_of_bugs_solved = None
        # private variable
        self.__salary = 0

    # instance method
    def get_name(self):
        return self.name

    # getter
    def get_salary(self):
        return self.__salary

    # setter
    def set_salary(self, value):
        if value in range(1, 10):
            self.__salary = value * 1.5
        else:
            self.__salary = value * 2


new_obj = SoftwareEngineer("Anik")
new_obj.set_salary(50)
print(new_obj.get_salary())