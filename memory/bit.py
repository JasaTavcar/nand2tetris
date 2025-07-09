import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memory.dff import DFF
from gates.mux import Mux

class Bit:
    def __init__(self):
        self.dff = DFF()

    def tick(self, inn, load):
        mux = Mux()
        new = mux(self.dff.out(), inn, load)
        self.dff.tick(new)

    def out(self):
        return self.dff.out()

