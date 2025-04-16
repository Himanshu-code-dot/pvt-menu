print("WELCOME TO THE FRIEND CALCULATOR")
while True:
    gender = input("Enter Gender (M/F): ").upper()
    if gender == 'M':
        name1 = input("Enter your name: ")
        name2 = input("Enter his name: ")
        break
    elif gender == 'F':
        name1 = input("Enter your name: ")
        name2 = input("Enter her name: ")
        break
    else:
        print("Please enter gender accordingly.")
        # The loop will continue automatically due to the lack of a break statement here

# The rest of your code to calculate friendship score between name1 and name2 goes here
