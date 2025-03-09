import character_create
import battle

def choose_character():
    characters = character_create.read_characters()
    choosen_character = {}
    character_names = []

    while True:

        i = 1
        for character in characters:
            character_names.append(character['name'].lower())

            if character != characters[0]:
                print(f'{i}. {character['name']} - Lvl {character['level']}')
                i += 1

        choice = input('Choose a character to look at (Enter name): ').lower()
        if choice in character_names:

            for character in characters:
                if choice == character['name']:
                    choosen_character == character

            for stat in character:
                print(f'{stat.capitalize()}: {character[stat]}')

            if input('Do you want to select this character? If so, type "Yes": ').lower() == 'yes':
                return choosen_character

def main():
    battle.fight(choose_character(), choose_character())

main()