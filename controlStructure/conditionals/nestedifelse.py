age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))

if age >= 18:
    if income >= 50000:
        print("You are eligible for a premium credit card.")
    elif income >= 30000:
        print("You are eligible for a standard credit card.")
    else:
        print("You are eligible for a basic credit card.")
else:
    print("You are not eligible for a credit card.")

'''The outer if checks if the person is 18 or older.
Inside the outer if, another if-elif-else checks the income level:
If income is 50,000 or more, they get a premium credit card.
If income is between 30,000 and 50,000, they get a standard credit card.
If income is less than 30,000, they get a basic credit card.
If the person's age is less than 18, they are not eligible for any credit card.'''
