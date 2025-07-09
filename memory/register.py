import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memory.bit import Bit

class Register:
    def __init__(self):
        self.bits = (Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit())

    def tick(self, inn, load):
        b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15 = self.bits
        i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15 = inn

        b0.tick(i0, load)
        b1.tick(i1, load)
        b2.tick(i2, load)
        b3.tick(i3, load)
        b4.tick(i4, load)
        b5.tick(i5, load)
        b6.tick(i6, load)
        b7.tick(i7, load)
        b8.tick(i8, load)
        b9.tick(i9, load)
        b10.tick(i10, load)
        b11.tick(i11, load)
        b12.tick(i12, load)
        b13.tick(i13, load)
        b14.tick(i14, load)
        b15.tick(i15, load)

        #?
        #self.bits = b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15
        
    def out(self):
        b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15 = self.bits

        return (b0.dff.out(), b1.dff.out(), b2.dff.out(), b3.dff.out(), b4.dff.out(), b5.dff.out(), b6.dff.out(), b7.dff.out(), \
        b8.dff.out(), b9.dff.out(), b10.dff.out(), b11.dff.out(), b12.dff.out(), b13.dff.out(), b14.dff.out(), b15.dff.out())

if __name__ == "__main__":
    register = Register()
    print(register.out())
    register.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), 0)
    print(register.out())
    register.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), 1)
    print(register.out())
    register.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1), 0)
    print(register.out())
    