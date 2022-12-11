def sort_dictionary (dic , revrse=True) :
    return dict(sorted(dic.items(), key = lambda x : x[1], reverse=revrse))

dic = {"TV" : 21 , "A.C." : 12 , "Watch" : 15 , "Mobile No." : 13}

print (f"Ascending order is : {sort_dictionary(dic,False)}")

print (f"Descending order is : {sort_dictionary(dic)}")