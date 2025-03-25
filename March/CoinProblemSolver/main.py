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

            target -= round((target // country[denomination]) * country[denomination],2)
            print(target)

        print(denomination_amounts)

def main():
    while True:
        print('-~-~-~-~-~- Coin Change Problem -~-~-~-~-~-')
        match input('1. Info \n2. Solve \n3. Exit \nWhat do you want to do (Input Number): '):
            case '1':
                print('Info')
            case '2':
                solve()
            case '3':
                print('Exiting Program...')
                break

main()