#Function takes certain orders separated by a space and adds them to lists
def item_order(order):
    """
    order: A string with words separated by spaces
    returns: A string that counts the number of repetitve words in 'order'
    """
    burgerCount = 0
    waterCount = 0
    saladCount = 0
    indexPos = 0 #Used to create an incrementing index
    
    while indexPos < len(order):
        char = order[indexPos]
        if char is "h":
            burgerCount += 1
            indexPos += 9
        elif char is "w":
            waterCount += 1
            indexPos += 5
        elif char is "s":
            saladCount += 1
            indexPos += 5
        else:
            indexPos += 1
                
    return "salad:" + str(saladCount) + " hamburger:" + str(burgerCount) + " water:" + str(waterCount)