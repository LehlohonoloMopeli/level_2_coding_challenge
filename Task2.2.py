def triangle(number, mode=None):
    """
    Description: Takes an integer and mode as arguments and returns a
        triangle formed using hashes.
    type(output): str

    """

    result = ""

    if type(number) == int:

        # Positive cases
        if number >= 0:
            if mode == None or mode == "left":
                for i in range(1, number + 1):
                    result += ("#" * i) + "\n"

            if mode == "right":
                for i in range(1, number + 1):
                    result += (" " * (number - i)) + ("#" * i) + "\n"

            if mode == "isoscoles":
                for i in range(1, number + 1):
                    result += (" " * (number - i)) + ("#" * (2 * i - 1)) + "\n"

        # Negative cases
        if number < 0:
            if mode == None or mode == "left":
                for i in range(number * (-1), 0, -1):
                    result += ("#" * i) + "\n"

            if mode == "right":
                for i in range(number * (-1), 0, -1):
                    result += (" " * ((-1) * (number) - i)) + ("#" * i) + "\n"

            if mode == "isoscoles":
                for i in range(number * (-1), 0, -1):
                    result += (" " * ((-1) * (number) - i)) + ("#" * (2 * i - 1)) + "\n"

        print(result)

    else:
        return "Invalid input!"
