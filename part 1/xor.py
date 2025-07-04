from nnot import Not
from nand import Nand
class Xor:
    def __call__(self, a, b):
        nnot = Not()
        nand = Nand()

        nota = nnot(a)
        notb = nnot(b)

        x1 = nand(a, b)
        x2 = nand(nota, notb)
        x3 = nand(x1, x2)

        return nnot(x3)

if __name__ == "__main__":
    """
    Prints all combinations for testing purposes
    """
    xor = Xor()
    print("a = 0, b = 0 -> out =", xor(0, 0))
    print("a = 0, b = 1 -> out =", xor(0, 1))
    print("a = 0, b = 1 -> out =", xor(1, 0))
    print("a = 1, b = 1 -> out =", xor(1, 1))