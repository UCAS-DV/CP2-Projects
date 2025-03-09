import csv
import gameAssets
import os

character_names = []

def modify_stat(stat, stat_name, points):

    while True:

        os.system('cls')

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

def show_attacks(character_class): 

    os.system('cls')

    print(f'Class: {character_class['name']}')
    print(f'Archetype: {character_class['brief']}')
    print(f'Description: {character_class['description']}')
    print(f'Alligence: {character_class['alligence']}')

    # Prints all attack information
    print('Attacks:')
    for attack in character_class['attacks']:
        print(f'    Attack: {attack['name']}')
        print(f'        Damage: {attack['damage']}')
        print(f'        Nerves: {-attack['discomfort']}')

    if input('Do you want to select this class? If so, type "Yes": ').lower() == 'yes':
        return character_class

def choose_class():
    
    while True:

        i = 1
        # Prints all class informatiom
        for character_class in gameAssets.classes:
            print(f'{i}. Class: {character_class['name']}')
            print(f'   Archetype: {character_class['brief']}')
            print(f'   Description: {character_class['description']}')
            i += 1

        choice = input('Which class do you want to look at? ').lower()
        
        match choice:

            # Elf
            case '1':
                return show_attacks(gameAssets.classes[0])

            # Skeleton
            case '2':
                return show_attacks(gameAssets.classes[1])

            # North Dakotan Mage
            case '3':
                return show_attacks(gameAssets.classes[2])

            # Vorlean
            case '4':
                return show_attacks(gameAssets.classes[3])



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
                    'class': character[6],
                    'level': character[7],
                    'wins': character [8]
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

    character_class = ''

    while True:
        try:    
            character_class = choose_class()['name']
            break
        except:
            pass
    
    while True:

        os.system('cls')

        match input(f'How do you wish to modify {name}? \nTotal Points: {total_points} \n1. Name - {name} \n2. Health - {health_points} \n3. Strength - {strength_points} \n4. Defense - {defense_points} \n5. Speed - {speed_points} \n6. Bravery - {bravery_points} \n7. Class - {character_class} \n8. Show Stats \n9. Finish Character \nEnter Number: '):

            # Change Name
            case '1':
                name = input("Name your character: ")

            # Modify Health
            case '2':
                health_points, total_points = modify_stat(health_points, "health", total_points)

            # Modify Strength
            case '3':
                strength_points, total_points = modify_stat(strength_points, "strength", total_points) 

            # Modify Defense
            case '4':
                defense_points, total_points = modify_stat(defense_points, "defense", total_points)

            # Modify Speed
            case '5':
                speed_points, total_points = modify_stat(speed_points, "speed", total_points)

            # Modify Bravery
            case '6':
                bravery_points, total_points = modify_stat(bravery_points, "bravery", total_points)
            
            # Choose Class
            case '7':

                os.system('cls')

                try:    
                    character_class = choose_class()['name']
                except:
                    pass
            
            # Print Stats
            case '8':
                os.system('cls')

                print(f"{name}'s Stats")
                print(f'Health: {25 + (health_points * 15)}')
                print(f'Nerves: {75 + (bravery_points * 5)}')
                print(f'Strength: {0.25 + (strength_points * 0.15)}')
                print(f'Defense: {0.25 + (defense_points * 0.15)}')
                print(f'Speed: {speed_points}')
                input('Press enter to continue')

            # Save Character
            case '9':

                os.system('cls')

                # Readds all names to character_names
                read_characters()

                if total_points == 0 and name not in character_names:
                    print(f'Saving {name}...')
                    save_character([name,health_points,strength_points,defense_points,speed_points,bravery_points,character_class,0,0])
                    
                    # Prints the stats of the character
                    characters = read_characters()
                    for stat in characters[-1]:
                        print(f'{stat.capitalize()} - {characters[-1][stat]}')
                    
                    break
                elif total_points != 0:
                    input('Oops! All of your points have not been spent. You need to spend all of your points! (Enter to continue)')
                elif name in character_names:
                    input("Oops! It seems like you already have a character with that name! Please change your character's name! (Enter to continue)")