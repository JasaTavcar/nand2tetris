from aand import And
class And16:
    def __call__(self, a, b):
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15 = a
        b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15 = b
        aand = And()

        return (aand(a0, b0), aand(a1, b1), aand(a2, b2), aand(a3, b3), aand(a4, b4), aand(a5, b5), aand(a6, b6), aand(a7, b7),\
        aand(a8, b8), aand(a9, b9), aand(a10, b10), aand(a11, b11), aand(a12, b12), aand(a13, b13), aand(a14, b14), aand(a15, b15))

if __name__ == "__main__":
    and16 = And16()
    print(and16((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)))