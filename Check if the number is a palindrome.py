

while True:  # Re-run program
    # main program
    # Q11: Check if the number is a palindrome
    N = int(input("Enter a number: "))
    original = N
    reverse = 0
    while N > 0:
        digit = N % 10
        reverse = reverse * 10 + digit
        N = N // 10
    if original == reverse:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")

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
