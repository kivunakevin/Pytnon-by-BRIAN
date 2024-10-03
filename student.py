class Student:
    def __init__(self, name, reg_number):
        self.name = name
        self.reg_number = reg_number

    def show_details(self):
        print("Name: ", self.name)
        print("Reg Number: ", self.reg_number)


# Creating objects for two students
s1 = Student("John", "R001")
s2 = Student("Jane", "R002")

# Showing student details
s1.show_details()
s2.show_details()

