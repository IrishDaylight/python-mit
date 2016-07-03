#Find the number of 'bob's in a given string

def findBob(s):
    """
    s: string of lowercase characters
    returns: integer representing number of lowercase vowels
    """
    #Change string to a list for better use
    
    bobCount = 0
    strPos = 0
    
    for char in s:
        strPos = s.find("bob", strPos) # Find index of "bob"
        if strPos != -1: # Make sure "bob" is still in the string
            bobCount += 1
            strPos += 2 # Add 2 indices to eliminate past "bob"s
        
    return bobCount
    
print "Number of times bob occurs is: " + str(findBob())