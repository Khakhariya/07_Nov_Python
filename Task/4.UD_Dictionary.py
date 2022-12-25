Loop = int (input ("Enter the number insert key in dictionary :- "))
key = []
values = []

for i in range (Loop):
    KEY = input ("Enter the Key of Dictionary :- ")
    Values = input ("Enter the values of Dictionary :- ")
    key.append(KEY)
    values.append(Values)

x = dict (zip(key,values))
print (f"Dictionary is under :- \n\t{x}")