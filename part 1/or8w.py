from oor import Or
class Or8w:
    def __call__(self, a):
        a1, a2, a3, a4, a5, a6, a7, a8 = a

        oor = Or()

        x1 = oor(a1, a2)
        x2 = oor(a3, a4)
        x3 = oor(a5, a6)
        x4 = oor(a7, a8)

        x5 = oor(x1, x2)
        x6 = oor(x3, x4)

        return oor(x5, x6)

if __name__ == "__main__":
    or8w = Or8w()
    print(or8w((0, 0, 0, 0, 0, 0, 0, 0)))
    print(or8w((0, 0, 0, 0, 0, 0, 0, 1)))