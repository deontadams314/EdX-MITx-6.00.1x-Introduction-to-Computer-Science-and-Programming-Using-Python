# Declare the variable lows and highs, which will be "c" if the guess is correct.
low = 0
high = 100
num = 50
test = True

# initial dialogue for the user
print("Please think of a number between 0 and 100! and watch me guess it!")
print("Got it?.....")
print("Good!")
print("Is your secret number " + str(num) + "?")

# loop to ask input
while test == True:
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if guess == 'h': # the guessed num becomes the high
        high = num
        num = ((high - low) // 2) + low
        print("Is your secret number ", num, "?")
    elif guess == 'l': # the guessed num becomes the low
        low = num
        num = ((high - low) // 2) + low
        print("Is your secret number ", num, "?")
    elif guess == "c":
        print("I guessed CORRECT!, your secret number is ", num)
        break
    elif guess != 'h' or guess != 'l' or guess != 'c':
        print("I'm sorry but " + guess + " is not a valid input. Please try again breh!!!!")
