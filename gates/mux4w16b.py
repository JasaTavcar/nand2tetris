import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gates.mux16 import Mux16
from gates.and16 import And16
from gates.or16 import Or16
from gates.aand import And
from gates.nnot import Not
class Mux4w16b:
    def __call__(self, a, b, c, d, s1, s2):
        and16 = And16()
        or16 = Or16()
        nnot = Not()
        aand = And()

        nots1 = nnot(s1)
        nots2 = nnot(s2)

        select_a = aand(nots1, nots2)
        select_b = aand(nots1, s2)
        select_c = aand(s1, nots2)
        select_d = aand(s1, s2)

        xa = and16(a, (select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a))
        xb = and16(b, (select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b))
        xc = and16(c, (select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c))
        xd = and16(d, (select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d))

        y1 = or16(xa, xb)
        y2 = or16(xc, xd)

        return or16(y1, y2)

if __name__ == "__main__":
    m = Mux4w16b()
    print(m((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 0))
    print(m((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 1))
    print(m((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 1, 0))
    print(m((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 1, 1))
