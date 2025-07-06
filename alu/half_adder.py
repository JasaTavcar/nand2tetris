import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gates.aand import And
from gates.xor import Xor

"""
performs addition operation on two bits
- input: a, b
- output: sum, carry
"""
class HalfAdder:
    def __call__(self, a, b):
        xor = Xor()
        aand = And()

        _sum = xor(a, b)
        carry = aand(a, b)

        return (_sum, carry)

if __name__ == "__main__":
    ha = HalfAdder()
    print("a = 0, b = 0 ->", ha(0, 0))
    print("a = 0, b = 1 ->", ha(0, 1))
    print("a = 1, b = 0 ->", ha(1, 0))
    print("a = 1, b = 1 ->", ha(1, 1))