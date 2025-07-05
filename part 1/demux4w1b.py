from nnot import Not
from nand import Nand
from aand import And
from oor import Or

class Demux4w1b:
    def __call__(self, input, s1, s2):
        nnot = Not()
        aand = And()

        nots1 = nnot(s1)
        nots2 = nnot(s2)

        a = aand(input, aand(nots1, nots2))
        b = aand(input, aand(nots1, s2))
        c = aand(input, aand(s1, nots2))
        d = aand(input, aand(s1, s2))

        return (a, b, c, d)

if __name__ == "__main__":
    d = Demux4w1b()
    print(d(1, 0, 1))
