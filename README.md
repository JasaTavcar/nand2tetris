# nand2tetris
Building a general purpose computer all the way up from a simple nAND gate.

Roughly following the nand2tetris website but from scratch, without the provided software tools. 

The starting nAND gate is a Python class with a simple if statement.

## Part I: Boolean logic
nAND -> elementary gates

Time scale: 5h

## Part II: Boolean arithmatic
elementary gates -> ALU.

Time scale:3h 20min

## Part III: Memory
Creating a 16kB RAM

The correct (realistic) implementation (a hierarchy of RAMs, where the correct register comes out through multiplexers on each level) 
causes each clock cycle to take two seconds, which is why I cheated a little and selected the correct register with
if statements on every layer of the hierarchy. The "more realistic" code is still there but commented out.

Time scale: 4h 50min

## Part IV: Machine language
No programming in this part, just laying out the form of machine language and assembly for this computer platform.

Time scale: 2h 10min