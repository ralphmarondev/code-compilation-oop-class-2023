# Ralph Maron Eda
# BSCPE-2A
#
# Create a class called Car. The Car class has the following
# fields:
#   color
#   model
#   Manufacturer
# Instantiate the Car class 3 times and display all properties
# Modify the properties

class Car:
    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer

    def display(self):
        print(f"Color: {self.color}")
        print(f"Model: {self.model}")
        print(f"Manufacturer: {self.manufacturer}")


def main():
    car1 = Car("Blue", "Model 1", "Company 1")
    car2 = Car("Red", "Model 2", "Company 2")
    car3 = Car("Yellow", "Model 3", "Company 3")

    car1.display()
    car2.display()
    car3.display()


if __name__ == '__main__':
    main()
