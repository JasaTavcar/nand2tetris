from nnot import Not
from nand import Nand
from aand import And
from oor import Or

class Demux:
    def __call__(self, input, s):
        nnot = Not()
        aand = And()

        nots = nnot(s)

        x1 = aand(input, nots)
        x2 = aand(input, s)

        return (x1, x2)

if __name__ == "__main__":
    """
    Prints all combinations for testing purposes
    """
    demux = Demux()
    print("a = 0, s = 0 -> out =", demux(0, 0))
    print("a = 0, s = 1 -> out =", demux(0, 1))
    print("a = 0, s = 1 -> out =", demux(1, 0))
    print("a = 1, s = 1 -> out =", demux(1, 1))