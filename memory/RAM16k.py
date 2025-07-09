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
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13 = adress
        adress_top = (a0, a1)
        adress_bottom = (a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13)

        mux = Mux4w16b()
        demux = Demux4w1b()

        s1, s2 = adress_top
        a0, a1, a2, a3 = demux(load, s1, s2)
        r0, r1, r2, r3 = self.rams

        r0.tick(inn, adress_bottom, a0)
        r1.tick(inn, adress_bottom, a1)
        r2.tick(inn, adress_bottom, a2)
        r3.tick(inn, adress_bottom, a3)

    def out(self, adress):
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13 = adress
        adress_bottom = (a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13)

        mux = Mux4w16b()
        r0, r1, r2, r3 = self.rams
        r0 = r0.out(adress_bottom)
        r1 = r1.out(adress_bottom)
        r2 = r2.out(adress_bottom)
        r3 = r3.out(adress_bottom)
        return mux(r0, r1, r2, r3, a0, a1)

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