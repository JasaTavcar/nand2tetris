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

class ALU:
    def __call__(self, zx, nx, zy, ny, f, no, x, y):
        fork = Fork16()
        aand = And16()
        oor = Or16()
        nnot = Not16()
        xor = Xor16()
        adder = Adder()

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

        return out

if __name__ == "__main__":
    alu = ALU()
    print(alu(0, 0, 0, 0, 0, 0, \
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), \
    (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)))