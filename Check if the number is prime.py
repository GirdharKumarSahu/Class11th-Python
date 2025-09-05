
while True:  # Re-run program
    # main program
    # Q9: Check if the number is prime
    N = int(input("Enter a number: "))
    if N > 1:
        is_prime = True  # Assume the number is prime
        i = 2
        while i < N:  # Check for factors
            if N % i == 0:
                is_prime = False
                break
            i = i + 1
        if is_prime:
            print("The number is prime.")
        else:
            print("The number is not prime.")
    else:
        print("The number is not prime.")

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
