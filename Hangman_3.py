def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = list("abcdefghijklmnopqrstuvwxyz")
    returnLetters = letters
    returnString = ""
    lgList = list(lettersGuessed)

    for char in lgList:
        if char in letters:
            returnLetters.remove(char)
    return returnString.join(returnLetters)
