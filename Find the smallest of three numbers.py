# Q7: Find the smallest of three numbers
A = int(input("Enter the first number (A): "))
B = int(input("Enter the second number (B): "))
C = int(input("Enter the third number (C): "))
if A < B and A < C:
    print("A is the smallest.")
elif B < C:
    print("B is the smallest.")
elif C < B:
    print("C is the smallest.")
else:
    print("All numbers are equal.")
while True:  # Re-run program
    # main program
    # Q7: Find the smallest of three numbers
    A = int(input("Enter the first number (A): "))
    B = int(input("Enter the second number (B): "))
    C = int(input("Enter the third number (C): "))
    if A < B and A < C:
        print("A is the smallest.")
    elif B < C:
        print("B is the smallest.")
    elif C < B:
        print("C is the smallest.")
    else:
        print("All numbers are equal.")
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
