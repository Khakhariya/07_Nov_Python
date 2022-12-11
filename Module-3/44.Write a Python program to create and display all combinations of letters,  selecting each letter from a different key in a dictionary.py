import itertools

dic1 = {'1': ['a','b'], '2': ['c','d']}
x = []

for i in dic1.values():
    x.append(i)

print (f"Original dictionary is : {dic1}")
print (f"\nList of values of dictionary is : {x}")   

print (f"\nOutput is under :-")
for combo in itertools.product(*x):
    print("".join(combo))