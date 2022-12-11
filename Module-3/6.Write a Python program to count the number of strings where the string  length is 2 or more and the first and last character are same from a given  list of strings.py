list = ["rajr","tant","Ujash","kailashk","ab"]

'''
list = []
n = int(input("Enter the list of items :-"))
for i in range (n):
    list_item = input("Enter the item of list :- ")
    list.append(list_item)
'''

count = int()

for i in list :
    L = len (i)
    if L >= 2 :
        if i[0] == i[-1] :
            count += 1
            print(f"{count} : {i}")
 
print (f"Number of string is : {count}")