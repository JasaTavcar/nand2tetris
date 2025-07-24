import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Coder:
    def dest(self, x):
        if x == None:
            return "000"
        dest = ""

        A = x.find('A')
        if A < 0:
            dest = dest + "0"
        else:
            dest = dest + "1"

        D = x.find('D')
        if D < 0:
            dest = dest + "0"
        else:
            dest = dest + "1"

        M = x.find('M')
        if M < 0:
            dest = dest + "0"
        else:
            dest = dest + "1"

        return dest

    def comp(self, comp):
        if comp == "0":
            return "0101010"
        if comp == "1":
            return "0111111"
        if comp == "-1":
            return "0111010"
        if comp == "D":
            return "0001100"
        if comp == "!D":
            return "0001101"
        if comp == "-D":
            return "0001111"
        if comp == "D+1":
            return "0011111"
        if comp == "D-1":
            return "0001110"
        if comp == "A":
            return "0110000"
        if comp == "!A":
            return "0110001"
        if comp == "-A":
            return "0110011"
        if comp == "A+1":
            return "0110111"
        if comp == "A-1":
            return "0110010"
        if comp == "D+A":
            return "0000010"
        if comp == "D-A":
            return "0010011"
        if comp == "A-D":
            return "0000111"
        if comp == "D&A":
            return "0000000"
        if comp == "D|A":
            return "0010101"
        if comp == "0":
            return "1101010"
        if comp == "1":
            return "1111111"
        if comp == "-1":
            return "1111010"
        if comp == "D":
            return "1001100"
        if comp == "!D":
            return "1001101"
        if comp == "-D":
            return "1001111"
        if comp == "D+1":
            return "1011111"
        if comp == "D-1":
            return "1001110"
        if comp == "M":
            return "1110000"
        if comp == "!M":
            return "1110001"
        if comp == "-M":
            return "1110011"
        if comp == "M+1":
            return "1110111"
        if comp == "M-1":
            return "1110010"
        if comp == "D+M":
            return "1000010"
        if comp == "D-M":
            return "1010011"
        if comp == "M-D":
            return "1000111"
        if comp == "D&M":
            return "1000000"
        if comp == "D|M":
            return "1010101"

        raise Exception("Comp part", comp, "not recognised")
        return None

    def jump(self, x):
        if x == None:
            return "000"
        if x == "JGT":
            return "001"
        if x == "JEQ":
            return "010"
        if x == "JGE":
            return "011"
        if x == "JLT":
            return "100"
        if x == "JNE":
            return "101"
        if x == "JLE":
            return "110"
        if x == "JMP":
            return "111"
        
        return "000"