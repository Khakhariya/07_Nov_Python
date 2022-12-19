class A :
    pass

o = A ()

print (isinstance(o,A))
print(isinstance(o, (list, tuple)))
print(isinstance(o, (list, tuple, A)))