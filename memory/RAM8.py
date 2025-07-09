import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memory.register import Register
from gates.mux8w16b import Mux8w16b
from gates.demux8w1b import Demux8w1b


class RAM8:
    def __init__(self):
        self.registers = (Register(), Register(), Register(), Register(), Register(), Register(), Register(), Register())

    def tick(self, inn, adress, load):
        # this is cheating, the code works without that, but the simulation of all combinations would just be too slow
        if load == 0:
            return
            
        mux = Mux8w16b()
        demux = Demux8w1b()

        s1, s2, s3 = adress
        a0, a1, a2, a3, a4, a5, a6, a7 = demux(load, s1, s2, s3)
        r0, r1, r2, r3, r4, r5, r6, r7 = self.registers

        r0.tick(inn, a0)
        r1.tick(inn, a1)
        r2.tick(inn, a2)
        r3.tick(inn, a3)
        r4.tick(inn, a4)
        r5.tick(inn, a5)
        r6.tick(inn, a6)
        r7.tick(inn, a7)

    def out(self, adress):
        mux = Mux8w16b()
        r0, r1, r2, r3, r4, r5, r6, r7 = self.registers
        r0 = r0.out()
        r1 = r1.out()
        r2 = r2.out()
        r3 = r3.out()
        r4 = r4.out()
        r5 = r5.out()
        r6 = r6.out()
        r7 = r7.out()
        s1, s2, s3 = adress
        return mux(r0, r1, r2, r3, r4, r5, r6, r7, s1, s2, s3)

if __name__ == "__main__":
    ram = RAM8()
    print(ram.out((0, 0, 1)))
    ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 1), 0)
    print(ram.out((0, 0, 1)))
    ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 1), 1)
    print(ram.out((0, 0, 1)))
    ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1), (0, 0, 1), 0)
    print(ram.out((0, 0, 1)))
    print("----")
    print(ram.out((0, 0, 0)))