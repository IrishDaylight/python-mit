#This script counts the number of lowercase vowels in a string

def countVowels(s):
    """
    s: string of lowercase characters
    returns: integer representing number of lowercase vowels
    """
    
    vowelCount = 0 #the number of vowels in the string
    vowels = "aeiou" #Vowels Note: add "AEIOU" to support uppercase vowels too
    
    for char in s: #For loop
        if char in vowels: #check if char is in the string vowels
            vowelCount += 1
            
    #Return vowel count as an integer
    return vowelCount
    
print "Number of vowels: " + str(countVowels())