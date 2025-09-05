
while True:  # Re-run program
    
# Q13: Check if the year is a leap year


    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("The year is a leap year.")
    else:
        print("The year is not a leap year.")


        
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


#Summary
#Divisible by 4 and not divisible by 100: Leap year.
#Divisible by 400: Leap year.
#Otherwise: Not a leap year.
