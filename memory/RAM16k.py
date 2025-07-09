import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memory.RAM4k import RAM4k
from gates.mux4w16b import Mux4w16b
from gates.demux4w1b import Demux4w1b


class RAM16k:
    def __init__(self):
        self.rams = (RAM4k(), RAM4k(), RAM4k(), RAM4k())

    def tick(self, inn, adress, load):
        # this is cheating, the code works without that, but the simulation of all combinations would just be too slow
        if load == 0:
            return

        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13 = adress
        adress_top = (a0, a1)
        adress_bottom = (a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13)

        mux = Mux4w16b()
        demux = Demux4w1b()

        s1, s2 = adress_top
        l0, l1, l2, l3 = demux(load, s1, s2)
        r0, r1, r2, r3 = self.rams

        r0.tick(inn, adress_bottom, l0)
        r1.tick(inn, adress_bottom, l1)
        r2.tick(inn, adress_bottom, l2)
        r3.tick(inn, adress_bottom, l3)

    def out(self, adress):
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13 = adress
        adress_bottom = (a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13)
        r0, r1, r2, r3 = self.rams

        # this is the correct way, but it's just too slow to simulate all combos, so we do it with if statements
        """
        mux = Mux4w16b()
        r0 = r0.out(adress_bottom)
        r1 = r1.out(adress_bottom)
        r2 = r2.out(adress_bottom)
        r3 = r3.out(adress_bottom)
        return mux(r0, r1, r2, r3, a0, a1)
        """

        if (a0 == 0 and a1 == 0):
            return r0.out(adress_bottom)
        if (a0 == 0 and a1 == 1):
            return r1.out(adress_bottom)
        if (a0 == 1 and a1 == 0):
            return r2.out(adress_bottom)
        if (a0 == 1 and a1 == 1):
            return r3.out(adress_bottom)

if __name__ == "__main__":
    ram = RAM16k()
    print(ram.out((0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0)))
    ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0), 0)
    print(ram.out((0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0)))
    ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0), 1)
    print(ram.out((0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0)))
    ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1), (0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0), 0)
    print(ram.out((0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0)))
    print("----")
    print(ram.out((0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0)))