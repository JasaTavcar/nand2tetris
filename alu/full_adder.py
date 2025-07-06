import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gates.oor import Or
from alu.half_adder import HalfAdder
"""
performs addition operation on two bits
- input: a, b, c
- output: sum, carry
"""
class FullAdder:
    def __call__(self, a, b, c):
        oor = Or()
        ha = HalfAdder()

        sum1, carry1 = ha(a, b)
        sum2, carry2 = ha(sum1, c)

        return (sum2, oor(carry1, carry2))

if __name__ == "__main__":
    fa = FullAdder()
    print("a = 0, b = 0, c = 0 ->", fa(0, 0, 0))
    print("a = 0, b = 0, c = 1 ->", fa(0, 0, 1))
    print("a = 0, b = 1, c = 0 ->", fa(0, 1, 0))
    print("a = 0, b = 1, c = 1 ->", fa(0, 1, 1))
    print("a = 1, b = 0, c = 0 ->", fa(1, 0, 0))
    print("a = 1, b = 0, c = 1 ->", fa(1, 0, 1))
    print("a = 1, b = 1, c = 0 ->", fa(1, 1, 0))
    print("a = 1, b = 1, c = 1 ->", fa(1, 1, 1))