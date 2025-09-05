
while True:  # Re-run program
    # main program
    # Q4: Check if the number is even or odd
    N = int(input("Enter a number: "))
    if N % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

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
