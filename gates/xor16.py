import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gates.xor import Xor
class Xor16:
    def __call__(self, a, b):
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15 = a
        b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15 = b
        xor = Xor()

        return (xor(a0, b0), xor(a1, b1), xor(a2, b2), xor(a3, b3), xor(a4, b4), xor(a5, b5), xor(a6, b6), xor(a7, b7),\
        xor(a8, b8), xor(a9, b9), xor(a10, b10), xor(a11, b11), xor(a12, b12), xor(a13, b13), xor(a14, b14), xor(a15, b15))

if __name__ == "__main__":
    or16 = Or16()
    print(or16((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)))