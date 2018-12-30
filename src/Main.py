from Table import Table
from Process import Process

Maintable=Table()
P1=Process()
P2=Process()
P3=Process()
P4=Process()

Maintable.printf()

print("P1")
if P1.firstfit(Maintable,15):
    Maintable.printf()
else:
    print("Register allocation failure")

print("P2")
if P2.nextfit(Maintable,20,1):
     Maintable.printf()
else:
     print("Register allocation failure")

print("P3")
if P3.bestfit(Maintable,25):
    Maintable.printf()
else:
    print("Register allocation failure")

print("P4:")
if P4.worsefit(Maintable,22):
    Maintable.printf()
else:
    print("Register allocation failure")

Maintable.recyc(0)
Maintable.recyc(187)
