import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memory.RAM16k import RAM16k
from computer.keyboard import Keyboard
from computer.screen import Screen
from gates.aand import And
from gates.nnot import Not
from gates.fork16 import Fork16
from gates.and16 import And16
from gates.or8w import Or8w
from gates.or16 import Or16

class RAM:
    def __init__(self):
        self.ram = RAM16k()
        self.keyboard = Keyboard()
        self.screen = Screen()

    def tick(self, inn, address, load):
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14 = address
        aand = And()
        nnot = Not()
        fork = Fork16()
        and16 = And16()
        or8w = Or8w()
        or16 = Or16()

        # if a0==0, we are accsessing ram
        ram_addr = (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14)
        do_ram = nnot(a0)
        self.ram.tick(inn, ram_addr, aand(do_ram, load))
        ram_out = self.ram.out(ram_addr)
        ram_out = and16(ram_out, fork(do_ram))

        # if a0==1 and a1==0, we are accsessing screen memory
        screen_addr = (a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14)
        do_screen = aand(a0, nnot(a1))
        screen_out = self.screen.tick(inn, screen_addr, aand(do_screen, load))
        screen_out = and16(screen_out, fork(do_screen))

        # if a0==1, a1==1 and everything else 0, we are accsessing keyboard memory
        a0 = nnot(a0)
        a1 = nnot(a1)
        x1 = nnot(or8w((a0, a1, a2, a3, a4, a5, a6, a7)))
        x2 = nnot(or8w((a7, a8, a9, a10, a11, a12, a13, a14)))
        do_keyboard = aand(x1, x2)
        keyboard_out = self.keyboard.tick(inn, aand(do_keyboard, load))
        keyboard_out = and16(keyboard_out, fork(do_keyboard))

        # up to one of the output values hasn't been zeroed out
        # return this one
        return or16(or16(ram_out, screen_out), keyboard_out)


if __name__ == "__main__":
    mem = RAM()
    print("ram:", mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0))
    print("ram:", mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0))
    print("ram:", mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 1))
    print("ram:", mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0))

    # screen
    print("screen:", mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 1))

    # keyboard
    print("keyboard:", mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 1))