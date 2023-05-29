# Ralph Maron Eda
# BSCPE-2A
#
# 1. Create an app that computes students average
# 2. The user will input the following (Name, Math, Science and English Grade)
# 3. Create a Class called Students
# 4. Use the init function to collect the student information
#       a. Name, Math, Science and English Grade
# 5. Create a function that will perform the computation of the average
# 6. Create a function that will display the result
#       a. Name: John
#       b. Math: 90
#       c. Science: 90
#       d. English: 90
#       e. Average: 90 (Passed)

class Students:
    def __init__(self, name, math, science, english):
        self.name = name
        self.math = math
        self.science = science
        self.english = english

    def get_average(self):
        average = (self.math + self.science + self.english) / 3

        return average

    # this function will return true if
    # average is greater than or equal to 75
    def is_passed(self):
        return "Passed" if self.get_average() >= 75 else "Failed"
    def display(self):
        print(f"Name: {self.name}")
        print(f"Math: {self.math}")
        print(f"Science: {self.science}")
        print(f"English: {self.english}")
        print(f"Average: {self.get_average()} ({self.is_passed()})")


def main():
    name = input("Enter name: ")
    math = float(input("Enter math: "))
    science = float(input("Enter science: "))
    english = float(input("Enter english: "))

    student = Students(name, math, science, english)
    student.display()


if __name__ == '__main__':
    main()
