import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from alu.adder import Adder
from alu.incrementer import Incrementer
from gates.and16 import And16
from gates.or16 import Or16
from gates.fork16 import Fork16
from gates.not16 import Not16
from gates.xor16 import Xor16
from gates.aand import And
from gates.nnot import Not

class ALU:
    def __call__(self, zx, nx, zy, ny, f, no, x, y):
        fork = Fork16()
        aand = And16()
        oor = Or16()
        nnot = Not16()
        xor = Xor16()
        adder = Adder()
        s_and = And()
        s_not = Not()

        zx = fork(zx)
        x = aand(nnot(zx), x)
        print(x)

        nx = fork(nx)
        x = xor(nx, x)
        print(x)

        zy = fork(zy)
        y = aand(nnot(zy), y)
        print(y)

        ny = fork(ny)
        y = xor(ny, y)
        print(y)

        f = fork(f)
        addition = aand(f, adder(x, y)) # if f==1 -> x+y
        comparison = aand(nnot(f), aand(x, y)) # if f==0 -> x & y
        out = oor(addition, comparison)
        print(out)

        no = fork(no)
        out = xor(no, out)
        print(out)
        print("-----------")

        # is output zero?
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15 = nnot(out)

        a1 = s_and(a0, a1)
        a2 = s_and(a2, a3)
        a3 = s_and(a4, a5)
        a4 = s_and(a6, a7)
        a5 = s_and(a8, a9)
        a6 = s_and(a10, a11)
        a7 = s_and(a12, a13)
        a8 = s_and(a14, a15)

        x1 = s_and(a1, a2)
        x2 = s_and(a3, a4)
        x3 = s_and(a5, a6)
        x4 = s_and(a7, a8)

        x5 = s_and(x1, x2)
        x6 = s_and(x3, x4)

        zr = s_and(x5, x6)

        # is output negative?
        ng = s_not(a0)

        return out, zr, ng

if __name__ == "__main__":
    alu = ALU()
    print(alu(0, 0, 0, 0, 0, 0, \
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), \
    (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)))