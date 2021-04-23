class MyVector:
    """A vector in python that automatically resizes"""

    def __init__(self):
        self._size = 0

    def size(self):
        return self._size

    def push(self, item):
        self._size += 1
