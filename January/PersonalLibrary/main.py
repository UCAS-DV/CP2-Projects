# Darius Vaiaoga - P2 - Personal Library Program
# 
library = []

genres = (
    "FPS",
    "Puzzle",
    "RPG",
    "Platformer",
    "Tower Defense",
    "Action-Adventure",
    "Co-op",
    "Fighting",
    "Party",
    "Survival",
    "Sandbox"
)

def showLibrary():
    num = 1
    for game in library:
        print(f'{num}. {game["name"]} - {game["genre"]} - {game["developer"]}')
        num += 1

def createEntry():
    name = input("What is the name of your game? ")
    
    num = 0
    for genre in genres:
        print(f"{num}. {genres[num]}")

    try:
        choosen_genre = genres[int(input("Which genre is your game? (Input Number)"))]
    except:
        print()

    developer = input("What studio or person developed or published the game? ")

    library.append({"name": name, "genre": genre, "developer": developer})

def removeEntry():
    showLibrary()
    gameToRemove = input("Which game do you want to remove? ")
    
    for game in library:
        if game['name'].lower() == gameToRemove.lower():
            library.remove(game)
            print(f"{game['name']} has been removed from your library.")
            break
    else:
        print(f'Could not find "{gameToRemove}" in your library. Please verify if you spelt the name correctly.')
    

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

        input("Press Enter to continue.")
                
main()