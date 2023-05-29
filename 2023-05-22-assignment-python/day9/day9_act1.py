# Ralph Maron Eda
# BSCPE-2A
#
# 1. Create a Record Keeping App
# 2. The will display the following options
#       a. Add Record
#       b. View Records
#       c. Clear All Records
#       d. Exit
# 3. If A: The user will input the following information (name,email,address)
# 4. The app will save the information in a text file.
# 5. If B, display the saved records
# 6. If C, clear the text file and display “No records found.”
# 7. If D, display “Thank you”
class RecordKeepingApp:
    FILE_NAME = "my_record_keeping_app"
    def choices(self):
        print("A - Add Record")
        print("B - View Records")
        print("C - Clear All Records")
        print("D - Exit")

    def create_file(self):
        file = open(self.FILE_NAME, "w")

        file.close()

    def add_record(self):
        file = open(self.FILE_NAME, "a")

        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")

        # writing the data to the file
        file.write(f"Name: {name}\nEmail: {email}\nAddress: {address}\n\n")

        file.close()

    def view_records(self):
        file = open(self.FILE_NAME, "r")

        print(file.read())
        file.close()

    def clear_all_records(self):
        import os
        os.remove(self.FILE_NAME)
        print("Clear records")

    def exit(self):
        print("Thank you")
        self.create_file()
        exit(0)


def main():
    record_keeping_app = RecordKeepingApp()
    # record_keeping_app.create_file()

    while True:
        record_keeping_app.choices()
        choice = input("Choice ~$ ")

        if choice.upper() == "A":
            record_keeping_app.add_record()
        elif choice.upper() == "B":
            record_keeping_app.view_records()
        elif choice.upper() == "C":
            record_keeping_app.clear_all_records()
        elif choice.upper() == "D":
            record_keeping_app.exit()


if __name__ == '__main__':
    main()
