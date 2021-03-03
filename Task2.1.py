def square(integer, character=None):
    """
    Description: Takes an integer and a character as arguments and returns
        a square using the character provided character.
    type(output): str

    """
    try:
        if character == None:
            row = "#" * integer
            result = ""

            for i in range(integer):
                result = result + "\n" + row
            print(result)

        else:
            row = str(character) * integer
            result = ""

            for i in range(integer):
                result = result + "\n" + row
            print(result)

    except:
        return "Invalid input!"
