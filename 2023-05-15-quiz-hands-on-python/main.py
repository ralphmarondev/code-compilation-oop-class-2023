# Ralph Maron Eda
# BSCPE-2A
# May 15, 2023
# Quiz Hands-On OOP [Python]
def encrypt(word: str, key: int):
    encrypted_message = ""
    my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for char in word:
        if char in my_list:
            position = my_list.index(char)
            new_position = position + key
            encrypted_message += my_list[new_position]
        else:
            encrypted_message += char
    print(f"Encrypted message: {encrypted_message}")


def decrypt(word: str, key: int):
    decrypted_message = ""
    my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    key *= -1

    for char in word:
        if char in my_list:
            position = my_list.index(char)
            new_position = position + key
            decrypted_message += my_list[new_position]
        else:
            decrypted_message += char
    print(f"Decrypted message: {decrypted_message}")


def choices():
    print("[E] Encryption")
    print("[D] Decryption")
    print("[Q] Exit program")
    # alam ko naman na kahit naman ilagay ko sarili ko
    # dito sa choices, d mo parin ako pipiliin :(


def main():
    while True:
        choices()
        choice = input("Choice ~$ ")

        if choice.upper() == "Q":
            break

        string = input("Enter string: ")
        key = int(input("Enter key: "))

        if choice.upper() == "E":
            encrypt(string, key)
        elif choice.upper() == "D":
            decrypt(string, key)

    print("Bye")


if __name__ == '__main__':
    main()
