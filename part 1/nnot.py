"""
Why *nnot* instead of *not*?
    Because *not* is a reserved word in python.
"""

from nand import Nand
class Not:
    def __call__(self, input):
        nand = Nand()
        return nand(input, input)

if __name__ == "__main__":
    """
    Prints all combinations for testing purposes
    """
    nott = Not()
    print("input: 0 -> output:", nott(0))
    print("input: 1 -> output:", nott(1))