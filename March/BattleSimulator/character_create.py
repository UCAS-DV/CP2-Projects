import csv
import gameAssets

character_names = []

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

def choose_class():
    
    while True:

        # Prints all attack information
            print('Attacks:')
            for attack in character_class['attacks']:
                print(f'    Attack: {attack['name']}')
                print(f'        Description: {attack['description']}')
                print(f'        Damage: {attack['damage']}')
                print(f'        Nerves: {-attack['discomfort']}')

        i = 1
        # Prints all class informatiom
        for character_class in gameAssets.classes:
            print(f'{i}. Class: {character_class['name']}')
            print(f'   Archetype: {character_class['brief']}')
            print(f'   Description: {character_class['description']}')

        choice = input('Which class do you want to look at? ').lower()
        
        match choice:

            # Elf
            case '1'
        
        

        

        


def read_characters():

    with open('March/BattleSimulator/characters.csv', 'r') as character_file:

        character_reader = csv.reader(character_file)

        characters = []

        for character in character_reader:

            # Checks if character is header
            if character != ['name','health','strength','defense','speed','bravery','class']:

                # Adds character with stats
                characters.append({
                    'name': character[0],
                    'health': character[1],
                    'strength': character[2],
                    'defense': character[3],
                    'speed': character[4],
                    'bravery': character[5],
                    'class': character[6]
                })

                character_names.append(character[0])

        return characters

def save_character(character):

    with open('March/BattleSimulator/characters.csv', 'a', newline='') as character_file:
        character_writer = csv.writer(character_file)

        character_writer.writerow(character)
              
def create_character():
    total_points = 0

    name = input('Name your character: ')

    health_points = 5
    strength_points = 5
    defense_points = 5
    speed_points = 5
    bravery_points = 5

    character_class = 'Elf'
    
    while True:

        match input(f'How do you wish to modify {name}? \nTotal Points: {total_points} \n1. Name - {name} \n2. Health - {health_points} \n3. Strength - {strength_points} \n4. Defense - {defense_points} \n5. Speed - {speed_points} \n6. Bravery - {bravery_points} \n7. Class - {character_class} \n8. Finish Character \nEnter Number: '):

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
            
            case '7':
                choose_class()

            case '8':

                # Readds all names to character_names
                read_characters()

                if total_points == 0 and name not in character_names:
                    print(f'Saving {name}...')
                    save_character([name,health_points,strength_points,defense_points,speed_points,bravery_points,character_class])
                    
                    # Prints the stats of the character
                    characters = read_characters()
                    for stat in characters[-1]:
                        print(f'{stat.capitalize()} - {characters[-1][stat]}')
                    
                    break
                elif total_points != 0:
                    input('Oops! All of your points have not been spent. You need to spend all of your points! (Enter to continue)')
                elif name in character_names:
                    input("Oops! It seems like you already have a character with that name! Please change your character's name! (Enter to continue)")


create_character()