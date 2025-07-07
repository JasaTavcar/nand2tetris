import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Fork16:
    def __call__(self, a):
        return (a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a)

if __name__ == "__main__":
    f = Fork16()
    print(f(0))
    print(f(1))