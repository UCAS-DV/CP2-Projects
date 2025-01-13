# Darius Vaiaoga - P2 - Financial Calculator

import math

# Budget Allocator (use set percentages to divide an income into spending categories) []

def floatInput(prompt):
    try:
        return float(input(prompt))
    except:
        return None

def checkInputs(inputs):
    if None in inputs:
        print("Invalid Input. Returning to main menu...")
        return None

# Sale Price Calculator (apply discounts to prices) [x]
def salesPrice(price, discount):

    checkInputs([price, discount])

    print(f"If you apply a {discount}% to a ${price:.2f} purchase, \nyou will pay: ${price * (1 - (discount / 100)):.2f}")

# Tip Calculator [x]
def tip(price, tip):

    checkInputs([price, tip])
    print(f"If you pay a {tip}% for a ${price:.2f} purchase, \nyou will pay: ${price * (1 + (tip / 100)):.2f}") 

# Compound Interest Calculator [x]
def compoundInterest(principle, rate, compound, time):

    checkInputs([principle, rate, compound, time])

    print(f'Your investment of ${principle:.2f} with an annual interest rate of {rate}%, compounded {compound} times a year for {time}')
    # Equation: P(1 + r/c)^nt
    # P = Principle
    # r = Rate
    # c = Compound
    # t = Time (in years)
    print(f'will be worth: ${principle * ((1 + ((rate/100) / compound ))**(compound * time)):.2f}')

# How long it will take to save for a goal based on a weekly or monthly deposit [x]
def savingsGoal():
    time = -1
    goal = floatInput("How much is your savings goal? ")   

    frequency = input("Do add money to your savings weekly or monthly? (Input Number): \n1. Weekly \n2. Monthly \n")
    if frequency == "1":
        frequency = 7
    elif frequency == "2":
        frequency = 30
    else:
        print("Invalid Frequency")
        return None
    
    amountSaved = math.floor(floatInput("How much do you save every time you add to your savings? "))

    checkInputs([amountSaved, frequency, goal])

    time = math.ceil(goal * frequency / (amountSaved))

    if frequency == 7:
        print(f"If you save ${amountSaved} every week, you will reach your goal of ${goal} in {time} days, \nor {math.ceil(time / 7)} weeks")
    if frequency == 30:
        print(f"If you save ${amountSaved} every month, you will reach your goal of ${goal} in {time} days \nor {math.ceil(time / 30)} months")



def main():
    while True:
        print("Welcome to your Financial Calculator!")

        print("Select what you will do: \n1. Calculate Sales Price \n2. Calculate Tip \n3. Calculate Compound Interest \n4. Allocate Budget \n5. Set Goal \n6. Exit")
        choice = input("What would you like to do? (Input Number): ")

        match choice:
            case "1":
                salesPrice(price = floatInput("What is the cost of the purchase? "), discount = floatInput("What is the discount in percentage points? "))
            case "2":
                tip(price = floatInput("What is the cost of the purchase? "), tip = floatInput('How high is the tip in percentage points? '))
            case "3":
                compoundInterest(principle = floatInput('How much did you initially invest? '), 
                                 rate = floatInput('What is your annual interest rate in percentage points? '),
                                 compound = floatInput('How many times does your investment compound per year? '),
                                 time = floatInput('How many years has your investment compounded? '))
            case "5":
                savingsGoal()
            case "6":
                print("Closing Program...")
                break
            case _:
                print("Invalid Selection, please try again.")
                continue
        
        input("Press Enter to continue. ")

main()