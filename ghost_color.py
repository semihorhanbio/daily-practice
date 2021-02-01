from random import randint
class Ghost:
    """Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated"""
    def __init__(self):
        self.color =  ["white", "yellow", "purple", "red"][randint(0,3)]
