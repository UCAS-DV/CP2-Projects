import random as rand

# Lists containing all characters that can go into a password, divided into lowercase letters, uppercase letters, numbers, and special characters
lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '?', ';', ':', '>', '<']

password_pool = []
password_length = 1

# Adds generates a password by randomly putting together characters from the password_pool
def generate_password(length):
    password = ''
    for x in range(0, length):
        
        # A random number to select a subset of characters in the password_pool
        selected_subset = rand.randint(0, len(password_pool) - 1)

        # A random number to select a character in the previously selected subset
        selected_character = rand.randint(0, len(password_pool[selected_subset]) - 1)

        # Adds a random character from a random subset to the password
        password += password_pool[selected_subset][selected_character]
    
    return password

# Adds a list of characters to the pool of characters that can be used in the pass code
def add_characters(subset_name, subset):
    print(f'{subset_name} [x]')
    password_pool.append(subset)

# Gives the user a Yes or No prompt to determine a condition by checking whether or not the user typed "Y" or "N"
def ask_question(prompt, condition_name, condition):

    while True:
        # Sets the user's answer to be a lowercase version of the first character of the user's input
        user_input = input(prompt)[0].lower()

        if user_input == 'y':
            add_characters(condition_name, condition)
            break
    
        elif user_input == 'n':
            print(f'{condition_name} [-]')
            break
    
        else:
            print("Invalid input")
            continue
        

def main():

    while True:
        print("-~-~-~-~-~-~-Random Password Generator-~-~-~-~-~-~-")

        # Clears the pool of characters that can be used in a password
        password_pool.clear()

        # Asks user whether they want, lowercase letters, uppercases, numbers, and or special characters in their password
        ask_question('Do you want lowercase letters in your password? (Y/N) ', 'Lowercase Letters', lower_alphabet)
        ask_question('Do you want uppercase letters in your password? (Y/N) ', "Uppercase Letters", upper_alphabet)
        ask_question('Do you want numbers in your password? (Y/N) ', 'Numbers', numbers)
        ask_question('Do you want special characters in your password? (Y/N) ', 'Special Characters', special_chars)

        # Asks for a password length until a valid length is given
        while True:
            try:
                password_length = int(input('How long do you wish your password to be? '))
                break
            except:
                print("Invalid Input")
                continue
        
        # Generates 4 passwords
        print(generate_password(password_length))
        print(generate_password(password_length))
        print(generate_password(password_length))
        print(generate_password(password_length))

        # Exits program if the user chooses too after generating the password
        if input('\nIf you wish to exit, enter "exit". If not, enter anything else: ').lower() == 'exit':
            print("Exiting Program...")
            break

main()