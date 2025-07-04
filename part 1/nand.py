class Nand:
    """
    The only hard-coded simulated piece of hardware in this entire project.
    Everything else is built from here.
    """
    def __call__(self, a, b):
        if a == 1 and b == 1:
             return 0
        else:
            return 1

if __name__ == "__main__":
    """
    Prints all combinations for testing purposes
    """
    nand = Nand()
    print("a = 0, b = 0 -> out =", nand(0, 0))
    print("a = 0, b = 1 -> out =", nand(0, 1))
    print("a = 0, b = 1 -> out =", nand(1, 0))
    print("a = 0, b = 1 -> out =", nand(1, 1))
