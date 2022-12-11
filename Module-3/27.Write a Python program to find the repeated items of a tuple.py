Items = ("Mobile","Laptop","Smart watch","TV","Smart watch","Laptop","Mobile","TV","TV","Smart watch")
print (f"Orginal tuple : {Items}")

List = set (Items)
List1 = tuple (List)
Length = len (List1)
print (f"Listed tuple : {List1}")

for i in range (Length):
    repeated_items = Items.count(List1[i])
    if repeated_items >= 2 :
        print (f"{List1[i]} : {repeated_items}")