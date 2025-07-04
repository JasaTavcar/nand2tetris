"""
Why *oor* instead of *or*?
    Because *or* is a reserved word in python.
"""

from aand import And
from nnot import Not
class Or:
    def __call__(self, a, b):
        nnot = Not()
        aand = And()

        x1 = aand(a, b)

        return nnot(x1)

if __name__ == "__main__":
    """
    Prints all combinations for testing purposes
    """
    oor = Or()
    print("a = 0, b = 0 -> out =", oor(0, 0))
    print("a = 0, b = 1 -> out =", oor(0, 1))
    print("a = 0, b = 1 -> out =", oor(1, 0))
    print("a = 1, b = 1 -> out =", oor(1, 1))