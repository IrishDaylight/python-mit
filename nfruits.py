def nfruits(foodList, foodPattern):
    """
    foodList: a dictionary that holds type of food and amount (string -> int)
    foodPattern: a string that holds a letter sequence representing the food eaten. "ABBABACDBA"
    returns: an int representing the maximum number of foods upon arrival
    """

    foodListAfter = foodList.copy()
    loopCount = 1  #Note: Starts at one

    for food in foodPattern:

        foodListAfter[food] -= 1

        for f in foodListAfter:
            if f is not food and loopCount < len(foodPattern):
                foodListAfter[f] += 1 # Add to the foodList

        loopCount += 1

    return foodListAfter.get(max(foodListAfter, key = foodListAfter.get), 0)
