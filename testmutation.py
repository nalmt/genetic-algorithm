from mutation import *



g = "90K2AWI10U5LIKWHRQ"
print("avant mutation", g)
print("longeur initale:", len(g))
s = mutateGenotype(g)
print("après mutation",s)
print("longeur après mutation", len(s))