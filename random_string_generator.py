from string import ascii_letters
from random import choice
def generateName():
    """Create a function for generating a random 6 character string"""
    return "".join(choice(ascii_letters) for char in range(6))
