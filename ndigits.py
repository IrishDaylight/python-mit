def ndigits(x):
    """
    x: integer of any length
    returns: an integer of the length of x
    """

    if abs(x) == 0:
        return 0 #No more digits. Return recursive value
    else:
        return 1 + ndigits(int(abs(x)/10)) #Recursion
