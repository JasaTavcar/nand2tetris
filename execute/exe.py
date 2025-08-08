import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from computer.comp import Comp
from vm.translator import translate
from assembler.asm import assemble
computer = Comp()

def instruction_number_tuple(instruction_number):
    t = []
    for i in range(15):
        t.append(instruction_number % 2)
        instruction_number //= 2
    t.reverse()
    return tuple(t)

root = sys.argv[1][:-3]
translate(root + ".vm")
assemble(root + ".asm")

# read instruction file and load instructions into ROM
hack_file = open(root + ".hack", "r")
instruction_number = 0
for line in hack_file:
    instruction = line.strip()
    l = []
    for i in range(16):
        l.append(int(instruction[i]))
    t = tuple(l)
    computer.rom.tick(t, instruction_number_tuple(instruction_number), 1)
    instruction_number += 1

# additional RAM initializations
computer.ram.tick((0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 1)

# execute
for i in range(1000): # instruction_number
    computer.tick()

# ending RAM value test
print("0: ", computer.ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0))
print("256: ", computer.ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0), 0))
print("257: ", computer.ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1), 0))
print("258: ", computer.ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0), 0))
print("259: ", computer.ram.tick((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1), 0))

hack_file.close()
