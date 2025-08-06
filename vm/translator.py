import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from vm.coder import VM_Coder
from vm.parser import VM_Parser

# remember to close the file

def translate(file):
    name = file[:-3] + ".asm"

    parser = VM_Parser(file)
    coder = VM_Coder(name)
    while parser.hasMoreLines():
        parser.advance()

        if parser.commandType() == "C_ARITHMETIC":
            coder.writeArithmetic(parser.arg1())
        
        if parser.commandType() == "C_PUSH" or parser.commandType() == "C_POP":
            coder.writePushPop(parser.commandType(), parser.arg1(), parser.arg2())

    coder.close()

if __name__ == "__main__":
    n = len(sys.argv)
    for i in range(1, n):
        if(sys.argv[i][-3:] != ".vm"):
            raise Exception("VM files must be .asm")
        translate(sys.argv[i])