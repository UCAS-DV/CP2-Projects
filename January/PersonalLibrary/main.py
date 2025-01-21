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

def showLibrary():
    num = 1
    print("Your Library:")
    for game in library:
        print(f'{num}. {game["name"]} - {game["genre"]} - {game["developer"]}')
        num += 1

def createEntry():
    name = input("What is the name of your game? ")
    
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

def search():
    query = input("Enter search query")
    search_list = []
    for letter in query:
    

def main():
    username = input("Welcome to your personal game library. Enter a username: ")
    while True:
        print(f"{username}'s Library")

        match input("What would you like to do? \n1. Go to Library \n2. Add to Library \n3. Remove from Library \n4. Search in Library \n5. Exit \n"):
            case "1":
                showLibrary()
            case "2":
                createEntry()
            case "3":
                removeEntry()
            case "4":
                search()
            case "5":
                break

        input("Press Enter to continue.")
                
main()