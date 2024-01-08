#!/usr/bin/python3
"""
Module MyList
"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)

        Args:
            self: the object
        """
        try:
            new = self[:]
            t = 0
            for i in range(len(new)):
                for j in range(i + 1, len(new)):
                    if new[i] > new[j]:
                        t = new[i]
                        new[i] = new[j]
                        new[j] = t
            print(new)
        except TypeError as te:
            print(te)
