
while True:  # Re-run program
    # main program
    # Q12: Find the simple interest for a given time period
    P = float(input("Enter the principal amount: "))
    R = float(input("Enter the rate of interest: "))
    T = float(input("Enter the time in years: "))
    simple_interest = (P * R * T) / 100
    print(f"The simple interest is {simple_interest}.")

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
