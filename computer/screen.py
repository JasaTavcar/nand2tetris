import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memory.RAM16k import RAM16k

class Screen:
    def __init__(self):
        self.ram = RAM16k()

    def tick(self, inn, address, load):
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12 = address
        address = (0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12)
        self.ram.tick(inn, address, load)
        return self.ram.out(address)


if __name__ == "__main__":
    mem = Screen()
    print(mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0))
    print(mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0))
    print(mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 1))
    print(mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0))
