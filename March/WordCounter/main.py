import file_handling

def main():
    print('Word Counter')

    while True:
        
        choice = input('Do you want to count the amount of words in your text file?\nIf so, type "y".\nIf you want to leave, type "e": ').lower()

        if choice == 'y':
            file_handling.add_timestamp()
        elif choice == 'e':
            print("Exiting program...")
            break

main()