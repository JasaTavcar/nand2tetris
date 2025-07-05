from mux16 import Mux16
from and16 import And16
from or16 import Or16
from aand import And
from nnot import Not
class Mux8w16b:
    def __call__(self, a, b, c, d, e,  f, g, h, s1, s2, s3):
        and16 = And16()
        or16 = Or16()
        nnot = Not()
        aand = And()

        nots1 = nnot(s1)
        nots2 = nnot(s2)
        nots3 = nnot(s3)

        select_a = aand(nots1, aand(nots2, nots3))
        select_b = aand(nots1, aand(nots2, s3))
        select_c = aand(nots1, aand(s2, nots3))
        select_d = aand(nots1, aand(s2, s3))
        select_e = aand(s1, aand(nots2, nots3))
        select_f = aand(s1, aand(nots2, s3))
        select_g = aand(s1, aand(s2, nots3))
        select_h = aand(s1, aand(s2, s3))

        xa = and16(a, (select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a, select_a))
        xb = and16(b, (select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b, select_b))
        xc = and16(c, (select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c, select_c))
        xd = and16(d, (select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d, select_d))
        xe = and16(e, (select_e, select_e, select_e, select_e, select_e, select_e, select_e, select_e, select_e, select_e, select_e, select_e, select_e, select_e, select_e, select_e))
        xf = and16(f, (select_f, select_f, select_f, select_f, select_f, select_f, select_f, select_f, select_f, select_f, select_f, select_f, select_f, select_f, select_f, select_f))
        xg = and16(g, (select_g, select_g, select_g, select_g, select_g, select_g, select_g, select_g, select_g, select_g, select_g, select_g, select_g, select_g, select_g, select_g))
        xh = and16(h, (select_h, select_h, select_h, select_h, select_h, select_h, select_h, select_h, select_h, select_h, select_h, select_h, select_h, select_h, select_h, select_h))

        y1 = or16(xa, xb)
        y2 = or16(xc, xd)
        y3 = or16(xe, xf)
        y4 = or16(xg, xh)

        z1 = or16(y1, y2)
        z2 = or16(y3, y4)

        return or16(z1, z2)

if __name__ == "__main__":
    m = Mux8w16b()
    print(m((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 1, 0, 0))
