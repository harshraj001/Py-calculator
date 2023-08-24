print("Welcome to the two number calculator made by Harsh!")

while True:
    try:
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    while True:
        print("What would you like to do with these numbers?")
        print("1) Add these numbers\n2) Subtract second number from first")
        print("3) Multiply these numbers\n4) Divide first number by second")
        print("5) Find remainder")
        print("6) Do all of the above")

        c = input("Make your choice (1, 2, 3, 4, 5 or 6): ")

        if c == '1':
            print("The addition of", a, "and", b, "is:", a + b)
        elif c == '2':
            print("The subtraction of", b, "from", a, "is:", a - b)
        elif c == '3':
            print("The multiplication of", a, "and", b, "is:", a * b)
        elif c == '4':
            if b != 0:
                div = round(a / b, 3)
                print("The division of", a, "by", b, "is:", div)
            else:
                print("Cannot divide by zero.")
        elif c == '5':
            if b != 0:
                print("5)The remainder left when", a, "divided by", b, "is:", a % b)
            else:
                print("5)Cannot divide by zero.")
        elif c == '6':
            print("1)The addition of", a, "and", b, "is:", a + b)
            print("2)The subtraction of", b, "from", a, "is:", a - b)
            print("3)The multiplication of", a, "and", b, "is:", a * b)
            if b != 0:
                div = round(a / b, 3)
                print("4)The division of", a, "by", b, "is:", div)
            else:
                print("4)Cannot divide by zero.")
            if b != 0:
                print("5)The remainder left when", a, "divided by", b, "is:", a % b)
            else:
                print("5)Cannot divide by zero.")
        else:
            print("Invalid choice. Please select a valid operation.")
            continue

        break

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        print("Thanks for using the Calculator.\nHave a nice day.")
        break

# The End