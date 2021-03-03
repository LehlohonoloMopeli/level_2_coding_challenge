"""
    Disclaimer: To solve this challenge, I borrowed a function called longest we completed
    in the level 1 coding challenge.
    
"""


def longest(array):
    """
    Description: Takes an array of strings as an argument and returns the longest strings
    type(output) : str

    """
    maximum_length = 0
    list_items = []

    for i in range(len(array)):
        if len(array[i]) >= maximum_length:
            maximum_length = len(array[i])

    for i in range(len(array)):
        if len(array[i]) == maximum_length:
            list_items.append(array[i])

    return list_items


def columns(array):
    """
    Description: Takes a list of strings and prints them as columns,
        with a single space space between the columns.
    type(output): str

    """

    result = ""
    list = []

    max_characters = longest(array)
    max_characters = len(max_characters[0])

    for i in array:
        if len(i) <= max_characters:
            i += " " * (max_characters - len(i))
            list.append(i)

    for i in range(0, max_characters):
        for j in list:
            result += j[i] + " "
        result += "\n"

    print(result)
