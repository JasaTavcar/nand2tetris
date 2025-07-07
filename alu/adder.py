import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from alu.full_adder import FullAdder

"""
performs addition operation on two bits
- input: a, b
- output: sum, carry
"""
class Adder:
    def __call__(self, a, b):
        fa = FullAdder()
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15 = a
        b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15 = b

        s15, c15 = fa(a15, b15, 0)
        s14, c14 = fa(a14, b14, c15)
        s13, c13 = fa(a13, b13, c14)
        s12, c12 = fa(a12, b12, c13)
        s11, c11 = fa(a11, b11, c12)
        s10, c10 = fa(a10, b10, c11)
        s9, c9 = fa(a9, b9, c10)
        s8, c8 = fa(a8, b8, c9)
        s7, c7 = fa(a7, b7, c8)
        s6, c6 = fa(a6, b6, c7)
        s5, c5 = fa(a5, b5, c6)
        s4, c4 = fa(a4, b4, c5)
        s3, c3 = fa(a3, b3, c4)
        s2, c2 = fa(a2, b2, c3)
        s1, c1 = fa(a1, b1, c2)
        s0, c0 = fa(a0, b0, c1)

        return (s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15)


if __name__ == "__main__":
    adder = Adder()
    print(adder((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1), (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)))
     