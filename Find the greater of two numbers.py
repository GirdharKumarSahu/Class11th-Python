
while True:  # Re-run program
    # main program
    # Q1: Find the greater of two numbers
    A = int(input("Enter the first number (A): "))
    B = int(input("Enter the second number (B): "))
    if A > B:
        print("A is greater.")
    elif B > A:
        print("B is greater.")
    else:
        print("Both numbers are equal.")

    while True:  # Validate user input
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print("invalid input.")

    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break
    
