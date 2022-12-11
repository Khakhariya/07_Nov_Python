list = [(),("my","name","jay"),("ridham","Jatin"),(),(11,12)]
new_list = []

Length = len(list) 

for i in range (Length) :
    if list[i] != ():
        new_list.append(list[i])

print (f"Original list : {list} \n--> New list : {new_list}")