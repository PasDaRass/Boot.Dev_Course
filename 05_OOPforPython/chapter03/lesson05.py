class Wall:
    def __init__(self, height):
        # the double underscore make this a private property
        # but it's not strictly enforced, there are hacks to get around it
        self.__height = height

    def get_height(self):
        return self.__height

  # QUIZ #

"""
Q: Python enforces encapsulation by fully preventing developers from touching private class members
A: False
"""
