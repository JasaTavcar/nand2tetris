import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class DFF:
    def __init__(self, a=0):
        self.state = a
    
    def tick(self, inn):
        self.state = inn

    def out(self):
        return self.state