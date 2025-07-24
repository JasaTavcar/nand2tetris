import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from assembler.coder import Coder
from assembler.parser import Parser
coder = Coder()

def assemble(file):
    name = file[:-4] + ".hack"
    f = open(name, "w")
    
    # first pass
    parser = Parser(file)
    symbols = {
        "R0": 0,
        "R1": 1,
        "R2": 2,
        "R3": 3,
        "R4": 4,
        "R5": 5,
        "R6": 6,
        "R7": 7,
        "R8": 8,
        "R9": 9,
        "R10": 10,
        "R11": 11,
        "R12": 12,
        "R13": 13,
        "R14": 14,
        "R15": 15,
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576
    }
    line = 1
    while parser.hasMoreLines():
        parser.advance()
        if parser.instructionType() == "L_INSTRUCTION":
            symbols.update({parser.symbol: line})
        else:
            line += 1

    # second pass, compile
    parser = Parser(file)
    counter = 16
    while parser.hasMoreLines():
        parser.advance()
        
        if parser.instructionType() == "A_INSTRUCTION":
            x = parser.symbol()

            if not x.isdigit():
                n = symbols.get(x)
                if n == None:
                    symbols.update({n: counter})
                    n = counter
                    counter += 1
            else: 
                n = int(x)
            print(x, "-->", n)

            code = ""
            for i in range(15):
                code = str(n%2) + code
                n = n // 2
            code = "0" + code
            f.write(code)

        if parser.instructionType() == "C_INSTRUCTION":
            dest = parser.dest()
            comp = parser.comp()
            jump = parser.jump()
            print(parser.instruction)
            print(dest, comp, jump)
            f.write("111" + coder.comp(comp) + coder.dest(dest) + coder.jump(jump))

        f.write('\n')



if __name__ == "__main__":
    n = len(sys.argv)
    for i in range(1, n):
        if(sys.argv[i][-4:] != ".asm"):
            raise Exception("Assembly files must be .asm")
        assemble(sys.argv[i])