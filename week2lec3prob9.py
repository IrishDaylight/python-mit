guess = 0
low = 0
high = 100
ans = ""
correct = False

print "Please think of a number between 0 and 100!"

while not correct:
    guess = (low + high) / 2

    print "Is your secret number " + str(guess) + "?"
    print "Enter 'h' to indicate the guess is too high.",
    print "Enter 'l' to indicate the guess is too low.",
    ans = raw_input("Type 'c' to indicate I guessed correctly. ")
    
    if ans == "h":
        high = guess
    elif ans == "l":
        low = guess
    elif ans == "c":
        correct = True
    else:
        print "Sorry, I did not understand your input."
        
print "Game over. Your secret number was: " + str(guess)