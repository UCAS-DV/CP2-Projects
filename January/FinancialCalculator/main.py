# Darius Vaiaoga - P2 - Financial Calculator

import math

# How long it will take to save for a goal based on a weekly or monthly deposit []
# Budget Allocator (use set percentages to divide an income into spending categories) []

spending_categories = [
    {
        "name": "Food",
        "percentage": 20
    }
]

def floatInput(prompt):
    try:
        return float(input(prompt))
    except:
        return None

# Sale Price Calculator (apply discounts to prices) [x]
def salesPrice():
    price = floatInput("What is the cost of the purchase? ")
    discount = floatInput("What is the discount in percentage points? ")

    if None in [price, discount]:
        print("Invalid Input in either price or tip. Returning to main menu...")
        return None

    print(f"If you apply a {discount}% to a ${price} purchase, \nyou will pay: ${price * (1 - (discount / 100))}")

# Tip Calculator [x]
def tip():

    price = floatInput("What is the cost of the purchase? ")
    tip = floatInput('How high is the tip in percentage points? ')

    if None in [price, tip]:
        print("Invalid Input in either price or tip. Returning to main menu...")
        return None

    print(f"If you pay a {tip}% for a ${price} purchase, \nyou will pay: ${price * (1 + (tip / 100))}") 

# Compound Interest Calculator []
def compoundInterest():

    principle = floatInput('How much did you initially invest? ')
    rate = floatInput('What is your annual interest rate in percentage points? ') / 100
    compound = floatInput('How many times does your investment compound per year? ')
    time = floatInput('How many years has your investment compounded? ')

    if None in [principle, rate, compound, time]:
        print("Invalid Input in either price or tip. Returning to main menu...")
        return None

    print(f'Your investment of ${principle} with an annual interest rate of {rate}%, compounded {compound} times a year for {time}')
    # Equation: P(1 + r/c)^nt
    # P = Principle
    # r = Rate
    # c = Compound
    # t = Time (in years)
    print(f'will be worth: ${principle * ((1 + (rate / compound ))**(compound * time)):.2f}')

def savingsGoal():
    time = -1
    goal = floatInput("How much is your savings goal? ")   

    frequency = input("Do add money to your savings weekly or monthly? (Input Number): \n1. Weekly \n2. Monthly \n")
    if frequency == "1":
        frequency = 7
    elif frequency == "2":
        frequency = 30
    else:
        frequency = None
    
    amountSaved = math.floor(floatInput("How much do you save every time you add to your savings? "))

    if frequency == 7:
        time = math.ceil(goal / (frequency * amountSaved))
        print(f"If you save ${amountSaved} every week, you will reach your goal of ${goal} in {time} days \nor {math.ceil(time / 7)} weeks \nor {math.ceil(time / 30)} months")


def main():
    while True:
        print("Welcome to your Financial Calculator!")

        print("Select what you will do: \n1. Calculate Sales Price \n2. Calculate Tip \n3. Calculate Compound Interest \n4. Allocate Budget \n5. Set Goal \n6. Exit")
        choice = input("What would you like to do? (Input Number): ")

        match choice:
            case "1":
                salesPrice()
            case "2":
                tip()
            case "3":
                compoundInterest()
            case "4":
                savingsGoal()
            case "6":
                print("Closing Program...")
                break
            case _:
                print("Invalid Selection, please try again.")
                continue
        
        input("Press Enter to continue. ")

main()