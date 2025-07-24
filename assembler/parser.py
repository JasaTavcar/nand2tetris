import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Parser:
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

    def instructionType(self):
        if self.instruction[0] == '@':
            return "A_INSTRUCTION"
        elif self.instruction[0] == '(':
            return "L_INSTRUCTION"
        else:
            return "C_INSTRUCTION"
    
    def symbol(self):
        if self.instructionType() == "C_INSTRUCTION":
            raise Exception("C_INSTRUCTION has no symbol")
        elif self.instructionType() == "A_INSTRUCTION":
            return self.instruction[1:-1]
        elif self.instructionType() == "L_INSTRUCTION":
            return self.instruction[1:-2]

    def _slice(self):
        if self.instructionType() != "C_INSTRUCTION":
            raise Exception("can only slice C_INSTRUCTION")
        t = [None, None, None] # dest, comp, jump
        equals = self.instruction.find('=')
        semicolon = self.instruction.find(';')
        if equals < 0:
            if semicolon < 0:
                t[1] = self.instruction[:-1]
            else:
                t[1] = self.instruction[:semicolon]
                t[2] = self.instruction[semicolon+1:-1]
        else:
            if semicolon < 0:
                t[0] = self.instruction[:equals]
                t[1] = self.instruction[equals+1:-1]
            else:
                t[0] = self.instruction[:equals]
                t[1] = self.instruction[equals+1:semicolon]
                t[2] = self.instruction[semicolon+1:-1]
        return t


    def dest(self):
        if self.instructionType() != "C_INSTRUCTION":
            raise Exception("can only read dest on C_INSTRUCTION")
        return self._slice()[0]
    
    def comp(self):
        if self.instructionType() != "C_INSTRUCTION":
            raise Exception("can only read dest on C_INSTRUCTION")
        return self._slice()[1]

    def jump(self):
        if self.instructionType() != "C_INSTRUCTION":
            raise Exception("can only read dest on C_INSTRUCTION")
        return self._slice()[2]

if __name__ == "__main__":
    parser = Parser("test.txt")
    while parser.hasMoreLines():
        parser.advance()
        print(parser._slice())
