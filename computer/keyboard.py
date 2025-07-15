import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memory.register import Register

class Keyboard:
    def __init__(self):
        self.reg = Register()

    def tick(self, inn, load):
        self.reg.tick(inn, load)
        return self.reg.out()


if __name__ == "__main__":
    mem = Keyboard()
    print(mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0))
    print(mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), 0))
    print(mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), 1))
    print(mem.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0))
