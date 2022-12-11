Tuple = (12,13,11,10,3)

print (f"Original tuple is : {Tuple}")

x = list(Tuple)

x[-1] = 12

print (f"Last value is replace from tuple : {tuple(x)}")