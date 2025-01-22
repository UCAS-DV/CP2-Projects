# Darius Vaiaoga - P2 - Personal Library Program

library = []

genres = (
    "Action-Adventure",
    "Fighting",
    "FPS",
    "Horror",
    "Party", 
    "Platformer",
    "Puzzle",
    "Roguelike",
    "RPG",
    "RTS",
    "Sandbox",
    "Simulator",
    "Survival",
)

# Prints out library
def showLibrary():
    num = 1
    print("Your Library:")
    for game in library:
        print(f'{num}. {game["name"]} - {game["genre"]} - {game["developer"]}')
        num += 1

# Asks for name, genre, and developer of game to add it to library
def createEntry():
    name = input("What is the name of your game? ")
    
    # Prints all possible genres and then asks user what genre they'd like
    num = 1
    for possible_genre in genres:
        print(f"{num}. {possible_genre}")
        num += 1

    try:
        genre = genres[int(input("Which genre is your game? (Input Number) ")) - 1]
    except:
        input("Invalid Input")
        return None

    developer = input("What studio or person developed or published the game? ")

    library.append({"name": name, "genre": genre, "developer": developer})

# Shows the game library, asks user what to remove, and then loops through the library to find and remove that game.
def removeEntry():
    showLibrary()
    game_to_remove = input("Which game do you want to remove? ")
    
    for game in library:
        if game['name'].lower() == game_to_remove.lower():
            library.remove(game)
            print(f"{game['name']} has been removed from your library.")
            break
    else:
        print(f'Could not find "{game_to_remove}" in your library. Please verify if you spelt the name correctly.')

# Finds and prints games based off of a criteria and a search query
def search(criteria=''):
    query = input(f"Enter Game {criteria.capitalize()}: ")
    num = 1

    for game in library:
        # If the first two letters of the query match the first two letters of the criteria, print the game info.
        if [game[criteria][0], game[criteria][1]] == [query[0], query[1]]:
            print(f'{num}. {game["name"]} - {game["genre"]} - {game["developer"]}')
            num += 1

# Main Function for handling UI
def main():
    username = input("Welcome to your personal game library. Enter a username: ")
    while True:
        print(f"{username}'s Library")

        # Asks user to input what they want to do
        match input("What would you like to do? \n1. Go to Library \n2. Add to Library \n3. Remove from Library \n4. Search in Library \n5. Exit \n"):

            # Show Library
            case "1":
                showLibrary()

            # Create Entry
            case "2":
                createEntry()

            # Remove Entry
            case "3":
                removeEntry()
            
            # Search
            case "4":
                # Asks user to input what they want to search by, and then invokes search to actually search for it
                match input("Search By: \n1. Title \n2. Genre \n3. Developer \nWhat do you want to search by? (Input Number) "):
                    case "1":
                        search("name")
                    case "2":
                        search("genre")
                    case "3":
                        search("developer")
                    case _:
                        input("Invalid Input")

            # Exists Program
            case "5":
                break

        input("Press Enter to continue.")
                
main()