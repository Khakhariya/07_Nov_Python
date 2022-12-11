list_num = []

Number = int(input("Enter the number :- "))

for i in range (Number) :
    number = int (input ("Enter the number to make a list :- "))
    list_num.append (number)

def new_list (listno) :
    print (f"Original list : {listno}")
    x = list(set(listno))
    return x

print (f"newlist : {new_list(list_num)}")