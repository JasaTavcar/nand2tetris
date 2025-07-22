import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from alu.alu import ALU
from gates.mux16 import Mux16
from gates.aand import And
from gates.oor import Or
from gates.nnot import Not
from alu.incrementer import Incrementer

class CPU:
    def __init__(self):
        self.alu = ALU()
        self.A = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) # 16 long!
        self.D = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.PC = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) # 16 long!

    def tick(self, inM, instruction, reset):
        mux16 = Mux16()
        alu = ALU()
        aand = And()
        oor = Or()
        nnot = Not()
        incrementer = Incrementer()

        # instruction decoding
        b, x1, x2, a, c1, c2, c3, c4, c5, c6, d1, d2, d3, j1, j2, j3 = instructrion

        # A-instruction
        # if we perform A-instruction, should other CPU functions be blocked?
        self.A = mux16(instruction, self.A, b)

        # C-instruction
        alu_in2 = mux16(self.A, inM, a)
        alu_out, zr, ng = alu(c1, c2, c3, c4, c5, c6, self.D, alu_in2)

        # if d1==1, save alu output into A
        save = aand(b, d1)
        self.A = mux16(self.A, alu_out, save)

        # if d2==1, save alu output into D
        save = aand(b, d2)
        self.D = mux16(self.D, alu_out, save)

        # if d3==1, save alu output into RAM[A]
        writeM = aand(b, d3)
        outM = self.alu_out
        addressM = self.A # 16 bit!

        # jump / increment PC
        not_neg = nnot(ng)
        j1 = oor(j1, not_neg)
        not_zero = nnot(zr)
        j2 = oor(j2, not_zero)
        not_pos = oor(zr, ng)
        j3 = oor(j3, not_pos)

        jump = aand(aand(j1, j2), j3)
        self.PC = incrementer(self.PC)
        self.PC = mux16(self.PC, self.A, jump)

        # reset PC
        self.PC = mux16(self.PC, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), jump)

        return (outM, writeM, addressM, PC)
