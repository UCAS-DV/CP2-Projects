# How long it will take to save for a goal based on a weekly or monthly deposit []
# Compound Interest Calculator []
# Budget Allocator (use set percentages to divide an income into spending categories) []


savings_goal = 0

spending_categories = [
    {
        "name": "Food",
        "percentage": 20
    }
]

# Sale Price Calculator (apply discounts to prices) []
def salesPrice(discount, price):
    print(f"If you apply a {discount}% to a ${price} purchase, \nyou will pay: ${price * (1 - (discount / 100))}")

# Tip Calculator []
def calculateTip(tip, price):
    print(f"If you pay a {tip}% for a ${price} purchase, \nyou will pay: ${price * (1 + (tip / 100))}") 

def main():
    while True:
        print("Welcome to your Financial Calculator!")

        print("Select what you will do: \n1. Calculate Sales Price \n2. Calculate Tip \n3. Calculate Compound Interest \n4. Allocate Budget \n5. Set Goal \n6. Exit")
        choice = input("What would you like to do? (input number): ")

        match choice:
            case "1":
                salesPrice(price=int(input("What is the cost of the purchase? ")), discount=int(input("What is the discount in percentage points? ")))
            case "2":
                calculateTip(price=int(input("What is the cost of the purchase? ")), tip=int(input('How high is the tip in percentage points? ')))
            case "6":
                print("Closing Program...")
                break
            case _:
                print("Invalid Selection, please try again.")
                continue
        
        input("Press Enter to continue. ")

main()