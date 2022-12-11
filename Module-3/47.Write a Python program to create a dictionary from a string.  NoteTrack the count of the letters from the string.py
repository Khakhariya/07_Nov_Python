str1 = input ("Enter Your string to count each letter and store as dictionary : ")

list1 = list()
list2 = list()
count = 0

for i in str1 :
    for j in str1 :
            if i in j :
                count += 1
    if i != " ":
        list1.append(i)
        list2.append(count)
    count = 0

print (f"Original string is : {str1}")
print (f"Output is : {dict(zip(list1,list2))}")