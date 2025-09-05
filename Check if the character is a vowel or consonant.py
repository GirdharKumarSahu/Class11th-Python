# Q5: Check if the character is a vowel or consonant
ch = input("Enter a character: ")
if ch in 'aeiouAEIOU':
    print("The character is a vowel.")
else:
    print("The character is a consonant.")
while True:  # Re-run program
    # main program
    # Q5: Check if the character is a vowel or consonant
    ch = input("Enter a character: ")
    if ch in 'aeiouAEIOU':
        print("The character is a vowel.")
    else:
        print("The character is a consonant.")
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
