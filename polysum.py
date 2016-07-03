import math

def polysum(n, s):
    """
    n: number of sides (float or int)
    s: side length (float or int)
    returns one number rounded to four decimal places
    """
    
    #Numerator
    numer = 0.25 * n * s**2
    
    #Denominator
    denom = math.tan(math.pi / n)
    
    #Perimeter
    perim = (s * n)**2
    
    return round((numer / denom) + perim, 4)