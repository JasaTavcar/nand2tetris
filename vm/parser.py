import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class VM_Parser:
    def __init__(self, file):
        self.file = open(file)
        self.instruction = None
        self.nextline = self._nextValid()

    def advance(self):
        self.instruction = self.nextline
        self.nextline = self._nextValid()

    def _nextValid(self):
        while True:
            line = self.file.readline()
            if line == "":
                return None
            while line[0] == ' ':
                line = line[1:]
            if len(line) < 2 or line[0] == '/' and line [1] == '/':
                continue
            white = True
            for c in range(len(line)):
                if c != ' ' and c != '\n':
                    white = False
            if white:
                continue
            return line
    
    def hasMoreLines(self):
        if self.nextline != None:
            return True
        else:
             return False

    def commandType(self):
        if self.instruction[0:3] == "add":
            return "C_ARITHMETIC"
        if self.instruction[0:3] == "sub":
            return "C_ARITHMETIC"
        if self.instruction[0:3] == "neg":
            return "C_ARITHMETIC"
        if self.instruction[0:3] == "pop":
            return "C_POP"
        if self.instruction[0:4] == "push":
            return "C_PUSH"
        else:
            return "C_INSTRUCTION"
    
    def symbol(self):
        if self.instructionType() == "C_INSTRUCTION":
            raise Exception("C_INSTRUCTION has no symbol")
        elif self.instructionType() == "A_INSTRUCTION":
            return self.instruction[1:-1]
        elif self.instructionType() == "L_INSTRUCTION":
            return self.instruction[1:-2]

    def arg1(self):
        tokens = self.instruction.split()
        print(tokens)
        if self.commandType() == "C_RETURN":
            raise Exception("VM parser: Return command has no arguments")
        elif self.commandType() == "C_ARITHMETIC":
            return tokens[0]
        else:
            return tokens[1]

    def arg2(self):
        tokens = self.instruction.split()
        if self.commandType() in ["C_PUSH", "C_POP", "C_FUNCTION", "C_CALL"]:
            return tokens[2]
        else:
            raise Exception("VM parser: no second argument found")

if __name__ == "__main__":
    parser = VM_Parser("test.txt")
    while parser.hasMoreLines():
        parser.advance()
        print(parser.arg1())
