class MyVector:
    """A vector in python that automatically resizes

    This is implemented as a simple wrapper around the built in list class.
    This is rather pointless.
    """

    def __init__(self):
        self.items = []

    def __getitem__(self, index):
        """This item enables this class to be subscriptable.

        ie. you can use the [] operator to get a specific item.
        """
        return self.items[index]

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)
