import countries

# Formats Output
def format_output(denomination_amounts):
    final_output = ''
    for amount in denomination_amounts:    

        if type(amount) == str:
            final_output += f'{amount}: '

        else:
            final_output += f'{amount}\n'

    return final_output

# Solves Coin Change Problem
def solve():

    # Runs menu where the user decides the country and target amount to solve for
    def solve_menu():
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
            return -1, -1
        
        # Prevents the target from being less than or equal to zero
        if target <= 0:
            print('Invalid Input')
            return -1, -1
        
        return country, target

    while True:

        user_country, user_target = solve_menu()
        if user_country == -1 and user_target == -1:
            continue
        
        denomination_amounts = []

        for denomination in user_country:

            # Adds denomination and it's amount to denomination_amounts
            if user_target // user_country[denomination] > 0:
                denomination_amounts.append(denomination)
                denomination_amounts.append(int(user_target // user_country[denomination]))

            user_target -= (user_target // user_country[denomination]) * user_country[denomination]
            user_target = round(user_target, 2)

        print(format_output(denomination_amounts))
        break
        