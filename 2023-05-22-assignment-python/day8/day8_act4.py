# Ralph Maron Eda
# BSCPE-2A
#
# 1. Create House Class with the following properties and methods
#       a. floorSize
#       b. noOfFloors
#       c. noOfDoors
#       d. switchOn()
#       e. lightOpen()
#       f. ovenOpen()
# 2. Create TownHouse Class inherit the House class
# 3. Modify the value of the following(noOfFloors and noOfDoors)
# 4. Instantiate the TownHouse Class once
# 5. Display all the properties
# 6. Calling the switchOn() will automatically execute lightOpne() and ovenOpen()

class House:
    floor_size= 0
    no_of_floors = 0
    no_of_doors = 0

    def __init__(self, floor_size, no_of_floors, no_of_doors):
        self.floor_size = floor_size
        self.no_of_doors = no_of_doors
        self.no_of_floors = no_of_floors

    def switch_on(self):
        print("Switch on")
        self.light_open()
        self.oven_open()

    def light_open(self):
        print("Light open")

    def oven_open(self):
        print("Even open")


# how to do inheritance in python
class TownHouse(House):

    def __init__(self):
        pass

    def display(self):
        print(f"Floor size: {self.floor_size}")
        print(f"No of Floors: {self.no_of_floors}")
        print(f"No of Doors: {self.no_of_doors}")



def main():
    town_house = TownHouse()
    town_house.no_of_doors = 10
    town_house.no_of_floors = 20
    town_house.floor_size = 30

    town_house.display()
    town_house.switch_on()


if __name__ == '__main__':
    main()
