list_keys = ['English', 'Hindi', 'Mathematics', 'Computer Science', 'Physics', 'Chemistry']
list_values = [2001, 2002, 2003, 2004, 2005, 2006]

if len(list_keys) == len(list_values):  
  
    res_dict = dict(zip(list_keys, list_values))  
     
print("The resultant dictionary is: ", res_dict) 