from z3 import *
from z3 import Solver

s=Int('S')
e=Int('E')
n=Int('N')
d=Int('D')
m=Int('M')
o=Int('O')
r=Int('R')
y=Int('Y')

solver=Solver()
SEND=s*pow(10,3)+e*pow(10,2)+n*pow(10,1)+d*pow(10,0)
MORE=m*pow(10,3)+o*pow(10,2)+r*pow(10,1)+e*pow(10,0)
MONEY=m*pow(10,4)+o*pow(10,3)+n*pow(10,2)+e*pow(10,1)+y*pow(10,0)

solver.add(SEND+MORE==MONEY)

solver.add(Distinct(s,e,n,d,m,o,r,y))


for var in ([s,e,n,d,m,o,r,y]):
    solver.add(var>=0,var<=9)
if solver.check()==sat:
    model=solver.model()
    print("Solution:\n")
    for var in [s,e,n,d]:
        print(f"{var}:{model[var]}")
    for var in [m,o,r,e]:
        print(f"{var}:{model[var]}")
    for var in [m,o,n,e,y]:
        print(f"{var}:{model[var]}")
else:
    print("No solution found");