import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from alu.adder import Adder

class Incrementer:
    def __call__(self, a):
        adder = Adder()
        return adder(a, ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)))

if __name__ == "__main__":
    inc = Incrementer()
    print(inc((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1)))