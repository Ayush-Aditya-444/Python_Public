set1=set([1,2,3,4,5])
set2=set([3,4,5,6,7])
print("Set1:-", set1)
print("Set2:-", set2)
seta=set1.union(set2)
print("Union:-", seta)
setb=set1.intersection(set2)
print("Intersection:-", setb)
setc=set1.difference(set2)
print("Difference (Set1 - Set2):-", setc)
setd=set2.difference(set1)
print("Difference (Set2 - Set1):-", setd)