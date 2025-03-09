import random
import character_create

# Takes one turn
def take_turn(turn_taker, turn_taker_stats, victim, victim_stats):

    while True:

        print(f"-!-!-!-!- {turn_taker['name']}'s Turn -!-!-!-!-")
        print('1. Check Stats \n2. Select Attack')
        
        match input('What do you want to do (Enter Number): '):

            # Check Stats
            case '1':
                # Prints Turn Taker's Stats
                print(f"-~-~-~-~- {turn_taker['name']}'s Stats")
                print(f'{turn_taker['health']}/{turn_taker_stats['health']} Health')
                print(f'{turn_taker['bravery']}/{turn_taker_stats['bravery']} Nerves')
                print(f'x{turn_taker['strength']} Damage Multipler')
                print(f'x{turn_taker['defense']} Damage Resistance')

                # Prints Victim's Stats
                print(f"-~-~-~-~- {victim['name']}'s Stats -~-~-~-~-")
                print(f"{victim['health']}/{victim_stats['health']} Health")
                print(f"{victim['bravery']}/{victim_stats['bravery']} Nerves")
                print(f"x{victim['strength']} Damage Multiplier")
                print(f"x{victim['defense']} Damage Resistance")

def fight(character_1, character_2):

    turn = 0

    player_1_stats = {}
    
    player_2_stats = {}

    # Determines which player goes first
    def determine_order(choice_1, choice_2):

        # Whatever player has the higher speed goes first
        if choice_1['speed'] > choice_2['speed']:
            return choice_1, choice_2
        elif choice_2['speed'] > choice_1['speed']:
            return choice_2, choice_1
        
        # If both players have the same speed, randomly choose between either one
        elif choice_1['speed'] == choice_2['speed']:

            if random.randint(1,10) <= 5:
                return choice_1, choice_2
            else:
                return choice_2, choice_1
            
    # Sets player 1 and 2 to the player that goes first and player that goes second
    player_1_stats, player_2_stats = determine_order(character_1, character_2)

    # Sets players to base stats
    player_1 = player_1_stats
    player_2 = player_2_stats

    while True:

        # If the turn is even, player 1 goes, if it's odd, player 2 goes
        if turn % 2 == 0:
            take_turn(player_1, player_1_stats, player_2, player_2_stats)
        else:
            take_turn(player_2, player_2_stats, player_1, player_1_stats)

fight(character_create.read_characters()[1], character_create.read_characters()[2])