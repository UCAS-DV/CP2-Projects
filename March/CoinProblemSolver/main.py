import countries
import solve

def main():
    while True:
        print('-~-~-~-~-~- Coin Change Problem -~-~-~-~-~-')
        match input('1. Info \n2. Solve \n3. Exit \nWhat do you want to do (Input Number): '):
            # Info
            case '1':
                input('The Coin Change Problem is a classic alogrithmic problem.\nThe problem is if given a target amount of currency, what is the minimum amount of coins and banknotes necessary to reach that target amount \nIn this program, you will enter the target currency and the type of currency and then this program will solve the problem. \n(Enter to Continue)')
            # Solve
            case '2':
                print(solve.solve())
            # Exit
            case '3':
                print('Exiting Program...')
                break

main()