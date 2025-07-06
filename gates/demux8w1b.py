import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gates.nnot import Not
from gates.nand import Nand
from gates.aand import And
from gates.oor import Or

class Demux8w1b:
    def __call__(self, input, s1, s2, s3):
        nnot = Not()
        aand = And()

        nots1 = nnot(s1)
        nots2 = nnot(s2)
        nots3 = nnot(s3)

        a = aand(input, aand(nots1, aand(nots2, nots3)))
        b = aand(input, aand(nots1, aand(nots2, s3)))
        c = aand(input, aand(nots1, aand(s2, nots3)))
        d = aand(input, aand(nots1, aand(s2, s3)))
        e = aand(input, aand(s1, aand(nots2, nots3)))
        f = aand(input, aand(s1, aand(nots2, s3)))
        g = aand(input, aand(s1, aand(s2, nots3)))
        h = aand(input, aand(s1, aand(s2, s3)))

        return (a, b, c, d, e, f, g, h)

if __name__ == "__main__":
    d = Demux8w1b()
    print(d(1, 1, 1, 0))
