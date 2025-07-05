from nnot import Not
class Not16:
    def __call__(self, a):
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15 = a
        nnot = Not()

        return (nnot(a0), nnot(a1), nnot(a2), nnot(a3), nnot(a4), nnot(a5), nnot(a6), nnot(a7), \
        nnot(a8), nnot(a9), nnot(a10), nnot(a11), nnot(a12), nnot(a13), nnot(a14), nnot(a15))

if __name__ == "__main__":
    not16 = Not16()
    print(not16((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)))