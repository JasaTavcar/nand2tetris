import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gates.nnot import Not
from gates.nand import Nand
from gates.aand import And
from gates.oor import Or

class Mux:
    def __call__(self, a, b, s):
        nnot = Not()
        oor = Or()
        aand = And()

        nots = nnot(s)
        x1 = aand(s, b)
        x2 = aand(nots, a)

        return oor(x1, x2)

if __name__ == "__main__":
    """
    Prints all combinations for testing purposes
    """
    mux = Mux()
    print("a = 0, b = 0, s = 0 | out =", mux(0, 0, 0))
    print("a = 0, b = 0, s = 1 | out =", mux(0, 0, 1))
    print("a = 0, b = 1, s = 0 | out =", mux(0, 1, 0))
    print("a = 0, b = 1, s = 1 | out =", mux(0, 1, 1))
    print("a = 1, b = 0, s = 0 | out =", mux(1, 0, 0))
    print("a = 1, b = 0, s = 1 | out =", mux(1, 0, 1))
    print("a = 1, b = 1, s = 0 | out =", mux(1, 1, 0))
    print("a = 1, b = 1, s = 1 | out =", mux(1, 1, 1))