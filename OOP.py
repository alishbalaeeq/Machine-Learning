class University:
    campuses = 5

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display(self):
        print(f"The uni name is {self.name} and location is {self.location}")

    def _campus(self):
        print(f"Campuses are {self.campuses}")

class Department(University):
    def __init__(self, name, HOD, U_name, U_loc):
        super().__init__(U_name, U_loc)
        self.name = name
        self.HOD = HOD

    def display(self):
        print(f"The department name is {self.name} and Head of Department is {self.HOD}")

    def _display1(self):
        print(f"The department name is {self.name} and Head of Department is {self.HOD}")

    def __display2(self):
        print(f"The department name is {self.name} and Head of Department is {self.HOD}")


obj1 = University("fast", 'Islamabad')
obj1.display()
obj1._campus()
obj2 = University("IIUI", "Islamabad")
# obj2.display()

child = Department("AI", "Dr.Omar", "Fast Nuces", "Islamabad")
child.display()
child._display1()
