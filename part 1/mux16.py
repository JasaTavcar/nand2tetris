from mux import Mux
class Mux16:
    def __call__(self, a, b, s):
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15 = a
        b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15 = b
        mux = Mux()

        return (mux(a0, b0, s), mux(a1, b1, s), mux(a2, b2, s), mux(a3, b3, s), mux(a4, b4, s), mux(a5, b5, s), mux(a6, b6, s), mux(a7, b7, s),\
        mux(a8, b8, s), mux(a9, b9, s), mux(a10, b10, s), mux(a11, b11, s), mux(a12, b12, s), mux(a13, b13, s), mux(a14, b14, s), mux(a15, b15, s))

if __name__ == "__main__":
    mux16 = Mux16()
    print(mux16((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 1))