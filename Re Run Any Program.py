while True: 
   #main program
    while True: 
        answer = input('Run again? (yes/no): ')
        if answer in ('yes', 'no'):
            break
        print("invalid input.")

    if answer == 'yes':
        continue
    else:
        print("Goodbye")
        break
