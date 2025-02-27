import csv

# Returns the items in the txt file as a list.
def read_list():

    with open('February/ToDoList/to_do.txt', 'r') as to_do_file:
        to_do_string = to_do_file.read()
        to_do_list = to_do_string.split(',')
        to_do_list.pop()
        return to_do_list

# Adds item to the txt file
def add_item(new_item):

    with open('February/ToDoList/to_do.txt', 'a') as to_do_file:
        to_do_file.write(f'[-]{new_item},')

def mark_item(item_to_mark, mark_complete):

    to_do_list = read_list()

    # Converts the item_to_mark into a format to add to the txt file
    if mark_complete:
        formatted_item_to_mark = f'[-]{item_to_mark}'
    else:
        formatted_item_to_mark = f'[x]{item_to_mark}'

    item_index = 0
    
    # IF the item to mark is actually in the to-do list
    if formatted_item_to_mark in to_do_list:

        item_index = to_do_list.index(formatted_item_to_mark)

        # Determines whether to mark or unmark the item
        if mark_complete:
            to_do_list[item_index] = f'[x]{item_to_mark}'
        else:
            to_do_list[item_index] = f'[-]{item_to_mark}' 

        # Writes the to-do list to the txt file
        with open('February/ToDoList/to_do.txt', 'w') as to_do_file:
            for item in to_do_list:
                to_do_file.write(f'{item},')

    else:
        input('That item is not in the To-Do List or has already been checked off/unchecked off')
        return None

# Prints every item in the list
def print_list():

    to_do_list = read_list()

    for item in to_do_list:
        print(item)

def main():

    input('-~-~-~-~-~- To-Do List -~-~-~-~-~-')

    while True:

        match input('What do you want to do? \n1. View List \n2. Add Item \n3. Mark Item \n4. Exit \nChoose a number: '):
            
            # View List
            case '1':
                print_list()
            
            # Add Item
            case '2':
                add_item(input('What item do you want to add to your To-Do List? '))
            
            # Mark Item
            case '3':

                match input('Do you want to check off or uncheck off an item? \n1. Check off \n2. Uncheck off \nChoose a number: '):
                    
                    # Check Off
                    case '1':
                        print_list()

                        mark_item(input('What item do you want to check off? (Answer is case sensitive): '), True)

                    # Uncheck Off
                    case '2':
                        print_list()

                        mark_item(input('What item do you want to check off? (Answer is case sensitive): '), False)

            # Exit
            case '4':
                break

            # Invalid Input
            case _:
                input('Invalid Input')

main()