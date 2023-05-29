# Ralph Maron Eda
# BSCPE-2A
#
# Day 7, Act 1
# Create a Name Generator App
# Create a lists for first name, middle name, and last name
#       with 10 items per list
# The application will ask the user to generate a new name.
# If yes, use a random number between 0 - 9 to randomly select
#       items in the list
# Display the generated name 'Congratulations! Your new name is ___'
# If no, display the word 'Thank you! and display all the names the
# user generated
import random

def get_random_number():
    min_num = 0
    max_num = 9
    return (random.randint(min_num, max_num))


def main():
    new_name = ""
    user_generated_names = []
    # random names are from "https://www.randomlists.com/"
    first_names = ["Linda", "Aryana", "Adriana", "Mattie", "Kristen",
                   "Denisse", "Micaela", "Micah", "Cheyanne", "Shea"]
    middle_names = ["Beck", "Blake", "Jeremy", "Hollyn", "Rebecca",
                    "Judd", "Matilda", "Susannah", "Rene", "Kathryn"]
    last_names = ["Mendez", "Rivera", "Mccann", "Meadows", "Roth", "Dean",
                  "Levine", "Ortega", "Dodson", "Welch"]

    while True:
        choice = input("Do you want to generate a new name? [Y/N]: ")

        if choice.upper() == "Y":
            index = get_random_number()
            new_name += first_names[index]
            new_name += " "
            index = get_random_number()
            new_name += middle_names[index]
            new_name += " "
            index = get_random_number()
            new_name += last_names[index]

            user_generated_names.append(new_name)
            print(f"Congratulations! Your new name is {new_name}")
        else:
            print("Thank you!")
            print("All user generated names are as follows:")
            print(user_generated_names)
            break

        new_name = "" # clear the name

    print("Bye")


if __name__ == '__main__':
    main()
