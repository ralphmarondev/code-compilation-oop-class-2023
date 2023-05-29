# Ralph Maron Eda
# BSCPE-2A
#
# Create a class called employee
# Use the init function the collec the employee information
#   a. Name, email, and mobile number
# Instantiate the Employee class two times with different
#   information
# Display all the properties of the object

class Employee:
    def __init__(self, name, email, mobile_number):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number

    def display(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Mobile number: {self.mobile_number}")
        print() # new line


def main():
    employee1 = Employee("Employee 1", "Email 1", "Mobile Num 1")
    employee2 = Employee("Employee 2", "Email 2", "Mobile Num 2")
    employee3 = Employee("Employee 3", "Email 3", "Mobile Num 3")

    # displaying all the properties
    employee1.display()
    employee2.display()
    employee3.display()
    

if __name__ == '__main__':
    main()
