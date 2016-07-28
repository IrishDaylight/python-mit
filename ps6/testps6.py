import string

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.

    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
    cipherDict = {}
    shiftChar = 0
    delta = (shift % 26) - 26 #Calculate index for letters out of index range
    hiLetters = string.ascii_uppercase
    loLetters = string.ascii_lowercase

    for letter in hiLetters:
        if(hiLetters.index(letter) + shift) < 26:
            shiftChar = hiLetters[hiLetters.index(letter) + shift]
        else:
            shiftChar = hiLetters[hiLetters.index(letter) + delta]
        cipherDict[letter] = shiftChar
    for letter in loLetters:
        if(loLetters.index(letter) + shift) < 26:
            shiftChar = loLetters[loLetters.index(letter) + shift]
        else:
            shiftChar = loLetters[loLetters.index(letter) + delta]
        cipherDict[letter] = shiftChar

    return cipherDict

def apply_shift(shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift

    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
         down the alphabet by the input shift
    '''
    cipherDict = build_shift_dict(shift)
    cipherStr = ""
    message = self.message_text
    for char in message:
        if char in cipherDict:
            cipherStr += cipherDict.get(char)
        else:
            cipherStr += char
    return cipherStr
