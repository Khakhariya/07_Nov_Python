dic = {"TV" : 21 , "A.C." : 12 , "Watch" : 15 , "Mobile No." : 13}
dic1 = {"iPhone" : 5 , "mac_book" : 10 , "Smart_Tv" : 9 , "iWatch" : 3}

list1 = list(dic.items())
list2 = list(dic1.items())

list3 = list1 + list2

new_dic = dict(list3)

print (f"Original dictionary 1 is : {dic} \nOriginal dictionary 2 is : {dic1}")
print (f"\nFinal concatenate dictionary is : {new_dic}")

'''dic = {"TV" : 21 , "A.C." : 12 , "Watch" : 15 , "Mobile No." : 13}
dic1 = {"iPhone" : 5 , "mac_book" : 10 , "Smart_Tv" : 9 , "iWatch" : 3}
new_dic = {}
for i in (dic ,dic1) :
    new_dic.update(i)
print (f"\nconcatenate dictonaries is : \n\t\t{new_dic}\n")'''