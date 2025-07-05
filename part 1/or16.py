from oor import Or
class Or16:
    def __call__(self, a, b):
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15 = a
        b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15 = b
        oor = Or()

        return (oor(a0, b0), oor(a1, b1), oor(a2, b2), oor(a3, b3), oor(a4, b4), oor(a5, b5), oor(a6, b6), oor(a7, b7),\
        oor(a8, b8), oor(a9, b9), oor(a10, b10), oor(a11, b11), oor(a12, b12), oor(a13, b13), oor(a14, b14), oor(a15, b15))

if __name__ == "__main__":
    or16 = Or16()
    print(or16((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)))