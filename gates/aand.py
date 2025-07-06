"""
Why *aand* instead of *and*?
    Because *and* is a reserved word in python.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gates.nnot import Not
from gates.nand import Nand
class And():
    def __call__(self, a, b):
        nand = Nand()
        nnot = Not()

        nota = nnot(a)

        x1 = nand(a, nota)
        x2 = nand(a, b)

        return nand(x1, x2)
        
if __name__ == "__main__":
    """
    Prints all combinations for testing purposes
    """
    aand = And()
    print("a = 0, b = 0 -> out =", aand(0, 0))
    print("a = 0, b = 1 -> out =", aand(0, 1))
    print("a = 0, b = 1 -> out =", aand(1, 0))
    print("a = 1, b = 1 -> out =", aand(1, 1))