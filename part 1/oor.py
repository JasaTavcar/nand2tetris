from aand import And
from nnot import Not
from nand import Nand
class Or:
    def __call__(self, a, b):
        nnot = Not()
        nand = Nand()
        aand = And()

        nota = nnot(a)
        notb = nnot(b)

        return nand(nota, notb)

if __name__ == "__main__":
    """
    Prints all combinations for testing purposes
    """
    oor = Or()
    print("a = 0, b = 0 -> out =", oor(0, 0))
    print("a = 0, b = 1 -> out =", oor(0, 1))
    print("a = 0, b = 1 -> out =", oor(1, 0))
    print("a = 1, b = 1 -> out =", oor(1, 1))