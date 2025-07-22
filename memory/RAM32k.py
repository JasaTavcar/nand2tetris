import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memory.RAM4k import RAM4k
from gates.mux8w16b import Mux8w16b
from gates.demux8w1b import Demux8w1b


class RAM32k:
    def __init__(self):
        self.rams = (RAM4k(), RAM4k(), RAM4k(), RAM4k(), RAM4k(), RAM4k(), RAM4k(), RAM4k())

    def tick(self, inn, adress, load):
        # this is cheating, the code works without that, but the simulation of all combinations would just be too slow
        if load == 0:
            return

        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14 = adress
        adress_top = (a0, a1, a2)
        adress_bottom = (a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14)

        mux = Mux8w16b()
        demux = Demux8w1b()

        s1, s2, s3 = adress_top
        l0, l1, l2, l3, l4, l5, l6, l7 = demux(load, s1, s2, s3)
        r0, r1, r2, r3, r4, r5, r6, r7 = self.rams

        r0.tick(inn, adress_bottom, l0)
        r1.tick(inn, adress_bottom, l1)
        r2.tick(inn, adress_bottom, l2)
        r3.tick(inn, adress_bottom, l3)
        r4.tick(inn, adress_bottom, l4)
        r5.tick(inn, adress_bottom, l5)
        r6.tick(inn, adress_bottom, l6)
        r7.tick(inn, adress_bottom, l7)

    def out(self, adress):
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14 = adress
        adress_bottom = (a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14)
        r0, r1, r2, r3, r4, r5, r6, r7 = self.rams

        # this is the correct way, but it's just too slow to simulate all combos, so we do it with if statements
        """
        mux = Mux8w16b()
        r0 = r0.out(adress_bottom)
        r1 = r1.out(adress_bottom)
        r2 = r2.out(adress_bottom)
        r3 = r3.out(adress_bottom)
        r4 = r4.out(adress_bottom)
        r5 = r5.out(adress_bottom)
        r6 = r6.out(adress_bottom)
        r7 = r7.out(adress_bottom)
        return mux(r0, r1, r2, r3, r4, r5, r6, r7, a0, a1, a2)
        """

        if (a0 == 0 and a1 == 0 and a2 == 0):
            return r0.out(adress_bottom)
        if (a0 == 0 and a1 == 0 and a2 == 1):
            return r1.out(adress_bottom)
        if (a0 == 0 and a1 == 1 and a2 == 0):
            return r2.out(adress_bottom)
        if (a0 == 0 and a1 == 1 and a2 == 1):
            return r3.out(adress_bottom)
        if (a0 == 1 and a1 == 0 and a2 == 0):
            return r4.out(adress_bottom)
        if (a0 == 1 and a1 == 0 and a2 == 1):
            return r5.out(adress_bottom)
        if (a0 == 1 and a1 == 1 and a2 == 0):
            return r6.out(adress_bottom)
        if (a0 == 1 and a1 == 1 and a2 == 1):
            return r7.out(adress_bottom)

if __name__ == "__main__":
    ram = RAM32k()
    print(ram.out((0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1)))
    ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1), 0)
    print(ram.out((0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1)))
    ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1), 1)
    print(ram.out((0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1)))
    ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1), (0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1), 0)
    print(ram.out((0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1)))
    print("----")
    print(ram.out((0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1)))