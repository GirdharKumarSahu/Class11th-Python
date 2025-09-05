
while True:  # Re-run program
    # main program
    # Q3: Check if the number is positive or negative
    N = int(input("Enter a number: "))
    if N > 0:
        print("The number is positive.")
    elif N < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
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
