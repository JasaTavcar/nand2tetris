# nand2tetris
Building a general purpose computer all the way up from a simple nAND gate.

Roughly following the nand2tetris website but from scratch, without the provided software tools. 

The starting nAND gate is a Python class with a simple if statement.

## Part I: Boolean logic
nAND -> elementary gates

Time scale:
- Theory: 1h 30min
- Implementation: 3h 30min

## Part II: Boolean arithmatic
Using elementary gates to create an ALU, capable of performing the most necessary elementary operations.

Time scale:
- Theory: 50min
- Implementation: 2h 30min

## Part III: Memory
Creating a 16kB RAM

The correct implementation (a hierarchy of RAMS, where the correct register comes out through multiplexers on each level) 
causes each clock cycle to take two seconds, which is why I cheated a little and selected the correct register with
if statements on every layer of the hierarchy. The "more realistic" code is still there in the comments.

Time scale:
- Theory: 1h 20min
- Implementation: 3h 30min