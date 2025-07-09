import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memory.RAM8 import RAM8
from gates.mux8w16b import Mux8w16b
from gates.demux8w1b import Demux8w1b


class RAM64:
    def __init__(self):
        self.rams = (RAM8(), RAM8(), RAM8(), RAM8(), RAM8(), RAM8(), RAM8(), RAM8())

    def tick(self, inn, adress, load):
        a0, a1, a2, a3, a4, a5 = adress
        adress_top = (a0, a1, a2)
        adress_bottom = (a3, a4, a5)

        mux = Mux8w16b()
        demux = Demux8w1b()

        s1, s2, s3 = adress_top
        a0, a1, a2, a3, a4, a5, a6, a7 = demux(load, s1, s2, s3)
        r0, r1, r2, r3, r4, r5, r6, r7 = self.rams

        r0.tick(inn, adress_bottom, a0)
        r1.tick(inn, adress_bottom, a1)
        r2.tick(inn, adress_bottom, a2)
        r3.tick(inn, adress_bottom, a3)
        r4.tick(inn, adress_bottom, a4)
        r5.tick(inn, adress_bottom, a5)
        r6.tick(inn, adress_bottom, a6)
        r7.tick(inn, adress_bottom, a7)

    def out(self, adress):
        a0, a1, a2, a3, a4, a5 = adress
        adress_bottom = (a3, a4, a5)

        mux = Mux8w16b()
        r0, r1, r2, r3, r4, r5, r6, r7 = self.rams
        r0 = r0.out(adress_bottom)
        r1 = r1.out(adress_bottom)
        r2 = r2.out(adress_bottom)
        r3 = r3.out(adress_bottom)
        r4 = r4.out(adress_bottom)
        r5 = r5.out(adress_bottom)
        r6 = r6.out(adress_bottom)
        r7 = r7.out(adress_bottom)
        return mux(r0, r1, r2, r3, r4, r5, r6, r7, a0, a1, a2)

if __name__ == "__main__":
    ram = RAM64()
    print(ram.out((0, 0, 1, 0, 0, 1)))
    ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1), 0)
    print(ram.out((0, 0, 1, 0, 0, 1)))
    ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1), 1)
    print(ram.out((0, 0, 1, 0, 0, 1)))
    ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1), (0, 0, 1, 0, 0, 1), 0)
    print(ram.out((0, 0, 1, 0, 0, 1)))
    print("----")
    print(ram.out((0, 0, 0, 0, 0, 0)))