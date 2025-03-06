import csv

def modify_stat(stat, stat_name, points):

    while True:

        match input(f'Do you want to increase or decrease the stat? \nTotal Points: {points} \n1. Increase \n2. Decrease \n3. Back \nEnter Number: '):

            case '1':

                if points != 0:

                    print(f'Total Points: {points}')
                    print(f'{stat_name.capitalize()}: {stat}')

                    try:
                        change = int(input(f'How much do you want to increase {stat_name}? '))

                    except:
                        input('You need to enter a number. (Enter to continue)')
                        continue

                    if points - change < 0:
                        input('You do not have enough points. (Enter to continue)')
                        continue

                    elif points - change > 0:
                        print(f'{stat_name.capitalize()} = {stat + change}')

                        return stat + change, points - change
                    
            case '2':

                print(f'Total Points: {points}')
                print(f'{stat_name.capitalize()}: {stat}')

                try:
                    change = int(input(f'How much do you want to decrease {stat_name}? '))

                except:
                    input('You need to enter a number. (Enter to continue)')
                    continue

                print(f'{stat_name.capitalize()}: {stat - change}')

                return stat - change, points + change
            
            case '3':
                return stat, points
            
            case _:
                continue

def save_character(character):
    with open('characters.csv', 'a', newline='') as character_file:
        character_writer = csv.writer(character_file)

        character_writer.writerow(character)
                
def create_character():
    total_points = 25

    name = input('Name your character: ')

    health_points = 0
    strength_points = 0
    defense_points = 0
    speed_points = 0
    bravery_points = 0

    character_class = ''
    
    while True:

        print('\033c')

        match input(f'How do you wish to modify {name}? \nTotal Points: {total_points} \n1. Name - {name} \n2. Health - {health_points} \n3. Strength - {strength_points} \n4. Defense - {defense_points} \n5. Speed - {speed_points} \n6. Bravery - {bravery_points} \n7. Class \n8. Finish Character \nEnter Number: '):

            case '1':
                name = input("Name your character: ")

            case '2':
                health_points, total_points = modify_stat(health_points, "health", total_points)

            case '3':
                strength_points, total_points = modify_stat(strength_points, "strength", total_points) 

            case '4':
                defense_points, total_points = modify_stat(defense_points, "defense", total_points)

            case '5':
                speed_points, total_points = modify_stat(speed_points, "speed", total_points)

            case '6':
                bravery_points, total_points = modify_stat(bravery_points, "bravery", total_points)

create_character()