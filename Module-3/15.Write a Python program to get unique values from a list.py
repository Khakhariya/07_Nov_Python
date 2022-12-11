list1 = [1,23,12,16,29,63,29.5,12,16,29]

print (f"Original list :- {list1}")

x = set (list1)

print ("Unique values are : ",end="")
for i in x:
    print (i,end=", ")