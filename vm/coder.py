import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class VM_Coder:
    def __init__(self, filename):
        self.f = open(filename, "w")

    def close(self):
        self.f.close()

    def writeArithmetic(self, command):
        self.f.write("// " + command + "\n")
        if command == "add":
            self.f.write("@SP" + '\n') # A <- 1 (register with SP address)
            self.f.write("M=M-1" + "\n") # SP--
            self.f.write("A=M" + '\n') # A <- SP (actual address)
            self.f.write("D=M" + '\n') # D <- RAM[SP] <==> a
            self.f.write("@SP" + '\n') # A <- 1 (register with SP address)
            self.f.write("M=M-1" + "\n") # SP--
            self.f.write("A=M" + '\n') # A <- SP (actual address)
            self.f.write("M=D+M\n") # b = a + b
            self.f.write("@SP" + '\n') # A <- 1 (register with SP address)
            self.f.write("M=M+1" + "\n") # SP++
            self.f.write("\n")
            
        elif command == "sub":
            self.f.write("@SP" + '\n') # A <- 1 (register with SP address)
            self.f.write("M=M-1" + "\n") # SP--
            self.f.write("A=M" + '\n') # A <- SP (actual address)
            self.f.write("D=M" + '\n') # D <- RAM[SP] <==> a
            self.f.write("@SP" + '\n') # A <- 1 (register with SP address)
            self.f.write("M=M-1" + "\n") # SP--
            self.f.write("A=M" + '\n') # A <- SP (actual address)
            self.f.write("M=M-D\n") # b = a - b
            self.f.write("@SP" + '\n') # A <- 1 (register with SP address)
            self.f.write("M=M+1" + "\n") # SP++
            self.f.write("\n")

        elif command == "neg":
            self.f.write("@SP" + '\n') # A <- 1 (register with SP address)
            self.f.write("M=M-1" + "\n") # SP--
            self.f.write("A=M" + '\n') # A <- SP (actual address)
            self.f.write("M=-M" + '\n') # M <- -M
            self.f.write("@SP" + '\n') # A <- 1 (register with SP address)
            self.f.write("M=M+1" + "\n") # SP++
            self.f.write("\n")
            
        else:
            raise Exception("vm coder: not an arithmetic command")

    def writePushPop(self, command, segment, index):
        self.f.write("// " + command + " " + segment + " " + index + "\n")
        if command == "C_PUSH":
            if segment == "constant":
                self.f.write("@" + index + '\n') # A <- index
                self.f.write("D=A" + '\n') # D <- index
                self.f.write("@SP + \n") # A <- 1 (location of SP address)
                self.f.write("A=M + \n") # A <- SP (actual)
                self.f.write("M=D + \n") # stack <- index
                self.f.write("@SP" + "\n") # A <- 1 (location of SP address)
                self.f.write("M=M+1" + "\n\n") # RAM[SP]++

            else:
                self.f.write("@" + segment + "\n") # A <- segment
                self.f.write("D=M" + "\n") # D <- RAM[segment]
                self.f.write("@" + index + "\n") # A <- index
                self.f.write("D=D+A" + "\n") # D <- RAM[segment] + index <==> x
                self.f.write("@SP" + "\n") # A <- 1 (location of SP address)
                self.f.write("A=M" + "\n") # A <- SP (actual)
                self.f.write("M=D" + "\n") # RAM[SP] <- x (push x)
                self.f.write("@SP" + "\n") # A <- 1 (location of SP address)
                self.f.write("M=M+1" + "\n") # RAM[SP]++
                self.f.write("\n")

        elif command == "C_POP":
            self.f.write("@SP" + "\n") # A <- 1 (location of SP address)
            self.f.write("M=M-1" + "\n") # SP--
            self.f.write("A=M" + "\n") # A <- SP (actual)
            self.f.write("D=M" + "\n") # D <- RAM[SP] <==> x
            self.f.write("@popped" + "\n")  # A <- popped
            self.f.write("M=D" + "\n") # RAM[popped] = x
            self.f.write("@" + segment + "\n") # A <- segment
            self.f.write("D=M" + "\n") # D <- RAM[segment]
            self.f.write("@" + index + "\n") # A <- index
            self.f.write("D=D+A" + "\n") # D <- RAM[segment] + index <==> save location
            self.f.write("@save_addr" + "\n") # A <- save_addr
            self.f.write("M=D" + "\n") # RAM[save_addr] <- save location
            self.f.write("@popped" + "\n") # A <- popped
            self.f.write("D=M" + "\n") # D <- x
            self.f.write("@save_addr" + "\n") # A <- save_addr
            self.f.write("M=D" + "\n") # RAM[save location] = x
            self.f.write("\n")

        else:
            raise Exception("vm coder: not a push/pop command")

if __name__ == "__main__":
    coder = VM_Coder("test.res")
    coder.writePushPop("C_PUSH", "local", "0")
    coder.writePushPop("C_PUSH", "local", "1")
    coder.writeArithmetic("add")
