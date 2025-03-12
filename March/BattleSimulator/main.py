import character_create
import battle
import gameAssets
import os
import random

def choose_characters(preview):
    characters = character_create.read_characters()
    
    character_names = []

    # Determines which player goes first
    def determine_order(choice_1, choice_2):

        # Whatever player has the higher speed goes first
        if choice_1['speed'] > choice_2['speed']:
            input(f"{choice_1['name']}'s {choice_1['speed']} Speed > {choice_2['name']}'s {choice_2['speed']} Speed \n{choice_1['name']} goes first! (Enter to Continue)")
            return choice_1, choice_2
        elif choice_2['speed'] > choice_1['speed']:
            input(f"{choice_2['name']}'s {choice_2['speed']} Speed > {choice_1['name']}'s {choice_1['speed']} Speed \n{choice_2['name']} goes first! (Enter to Continue)")
            return choice_2, choice_1
        
        # If both players have the same speed, randomly choose between either one
        elif choice_1['speed'] == choice_2['speed']:

            if random.randint(1,10) <= 5:
                input(f'Tied Speed \n {choice_1['name']} goes first! (Enter to Continue)')
                return choice_1, choice_2
            else:
                input(f'Tied Speed \n {choice_2['name']} goes first! (Enter to Continue)')
                return choice_2, choice_1
            
    # Chooses character based on user input
    def choose_character():

        choosen_character = {}

        while True:

            i = 1
            for character in characters:
                character_names.append(character['name'].lower())

                print(f'{i}. {character['name']} - Lvl {character['level']} - {character['wins']} Wins')
                i += 1

            choice = input('Choose a character to look at (Enter name): ').lower()
            if choice in character_names:

                for character in characters:
                    if choice == character['name'].lower():
                        choosen_character = character

                for stat in choosen_character:
                    print(f'{stat.capitalize()}: {choosen_character[stat]}')

                if input('Do you want to select this character? If so, type "Yes": ').lower() == 'yes':
                    return choosen_character

    if not preview:   
        character_1, character_2 = determine_order(choose_character(), choose_character())
        return character_1, character_2
    else:
        return choose_character()
            
def main():
    
    while True:

        os.system('Cls')

        print('-~-~-~-~- Battle for the Country -~-~-~-~-')

        print(len(character_create.read_characters()))
        if len(character_create.read_characters()) >= 2:
            match input('1. Backstory \n2. Create Fighter \n3. Fighter List \n4. Battle \n5. Exit \nEnter the number of the option you want to select: '):
                # Backstory
                case '1':
                    battle.Dialogue(gameAssets.intro)
                
                # Create Character
                case '2':
                    character_create.create_character(0, 0)

                # Choose Character
                case '3':
                    choose_characters(True)

                # Battle
                case '4':

                    while True:

                        os.system('Cls')

                        match input('-!-!-!-!- Battle -!-!-!-!- \n1. Tutorial \n2. Battle \n3. Back \nEnter the number of the option you want to select: '):

                            # Tutorial
                            case '1':
                                battle.Dialogue(gameAssets.tutorial)

                            # Battle
                            case '2':
                                player_1, player_2 = choose_characters(False)


                                if player_1 != player_2:
                                    # Determine winner of battle by having battle
                                    winner = battle.fight(player_1, player_2)

                                    # Converts wins and level to integers
                                    winner['wins'] = int(winner['wins'])
                                    winner['level'] = int(winner['level'])

                                    # Whoever wins gets one extra win on their character
                                    input(f'{winner['name']} has {winner['wins'] + 1} wins (Enter to Continue)')

                                    if winner['wins'] == winner['level'] * 2:
                                        
                                        winner['level'] += 1

                                        character_create.remove_character(winner)
                                        input(f'{winner['name']} has leveled up to level {winner['level']} (Enter to Continue)')

                                        input(f'Remaking {winner['name']}...')
                                        character_create.create_character(winner['level'], winner['wins'] + 1)
                                    else:
                                        print('here')
                                        character_create.update_value(winner, 'wins', winner['wins'] + 1)

                            # Back
                            case '3':
                                break

                # Exit
                case '5':
                    print('Exiting Game...')
                    break
        else:
            input('No fighters found. (Enter to Continue)')
            input('Creating First Fighter... (Enter to Continue)')
            character_create.create_character(0, 0)
            input('Creating Second Fighter... (Enter to Continue)')
            character_create.create_character(0, 0)



main()