def valid_triangle(sides):
    """
    The function takes a list of sides of the triangle and
    returns a boolean value indicating whether the triangle is valid or not.

    For a shape to be a triangle at all, all sides have to be of length > 0,
    and the sum of the lengths of any two sides must be greater than or equal
    to the length of the third side.

    Parameters:
    sides (list): A list of integers representing the sides of the triangle

    Returns:
    bool: True if the triangle is valid, False otherwise
    """
    sides.sort()
    if all(a <= 0 for a in sides):
        return False
    if sides[0] + sides[1] < sides[2]:
        return False
    return True


def equilateral(sides):
    """
    The function takes a list of sides of the triangle and returns
    a boolean value indicating whether the triangle is equilateral or not.
    An equilateral triangle has all three sides the same length.

    Parameters:
    sides (list): A list of integers representing the sides of the triangle

    Returns:
    bool: True if the triangle is equilateral, False otherwise
    """
    if valid_triangle(sides):
        if all(length == sides[0] for length in sides):
            return True
    return False


def isosceles(sides):
    """
    The function takes a list of sides of the triangle and returns
    a boolean value indicating whether the triangle is isosceles or not.
    An isosceles triangle has at least two sides the same length.

    Parameters:
    sides (list): A list of integers representing the sides of the triangle

    Returns:
    bool: True if the triangle is isosceles, False otherwise
    """
    sides.sort()
    if valid_triangle(sides):
        sides_set = set(sides)
        if len(sides_set) <= 2:
            return True
    return False


def scalene(sides):
    """
    The function takes a list of sides of the triangle and returns
    a boolean value indicating whether the triangle is scalene or not.
    A scalene triangle has all sides of different lengths.

    Parameters:
    sides (list): A list of integers representing the sides of the triangle

    Returns:
    bool: True if the triangle is scalene, False otherwise
    """
    if valid_triangle(sides):
        sides_set = set(sides)
        if len(sides_set) == 3:
            return True
    return False
