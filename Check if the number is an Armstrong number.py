
while True:  # Re-run program
    # main program
    # Q10: Check if the number is an Armstrong number
    N = int(input("Enter a number: "))
    original = N
    sum_of_cubes = 0
    while N > 0:
        digit = N % 10
        sum_of_cubes += digit ** 3
        N = N // 10
    if original == sum_of_cubes:
        print("The number is an Armstrong number.")
    else:
        print("The number is not an Armstrong number.")

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
