import countries

def solve():

    while True:
        i = 1
        for country in countries.country_dems:
            print(f'{i}. {country}')
            i += 1

        try:
            country_index = input('Input abbrieviation of country you want to solve for: ')

            country = countries.country_dems[country_index.upper()]
            
            target = float(input('Input target amount: '))

        # Ensures that the user inputs the right inputs
        except:
            print('Invalid Input')
            continue
        
        # Prevents the target from being less than or equal to zero
        if target <= 0:
            print('Invalid Input')
            continue

        denomination_amounts = []

        for denomination in country:

            # Adds denomination and it's amount to denomination_amounts
            if target // country[denomination] > 0:
                denomination_amounts.append(denomination)
                denomination_amounts.append(int(target // country[denomination]))

            target -= (target // country[denomination]) * country[denomination]
            target = round(target, 2)

        # Formats the answer
        final_output = ''
        for amount in denomination_amounts:    

            if type(amount) == str:
                final_output += f'{amount}: '

            else:
                final_output += f'{amount}\n'

        return final_output

def main():
    while True:
        print('-~-~-~-~-~- Coin Change Problem -~-~-~-~-~-')
        match input('1. Info \n2. Solve \n3. Exit \nWhat do you want to do (Input Number): '):
            # Info
            case '1':
                input('The Coin Change Problem is a classic alogrithmic problem.\nThe problem is if given a target amount of currency, what is the minimum amount of coins and banknotes necessary to reach that target amount \nIn this program, you will enter the target currency and the type of currency and then this program will solve the problem. \n(Enter to Continue)')
            # Solve
            case '2':
                print(solve())
            # Exit
            case '3':
                print('Exiting Program...')
                break

main()