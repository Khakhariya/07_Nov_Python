--> we can remove the last object from list using 
    three method
    1) remove function
    2) pop function 
    3) del function 
'''

'''
1) remove function :- we can remove any object from list using 
   it but only one element remove.
'''
print ("Remove Function :- ")
list1 = [2, 33, 222, 14, 25]
print ("Original list :- ",list1) 

list1.remove(222)

print (list1)    

'''
2) pop function :- it is used to remove the last object from 
   list and also we can remove any object in pop function.
'''
print ("\npop Function :- ")
list1 = [2, 33, 222, 14, 25]
print ("Original list :- ",list1) 

list1.pop() 
print (list1)    

list1.pop(1)
print (list1)

'''
3) del function :- we can remove the last object from 
   the list and also delete the full list using del -
   function.
'''
print ("\ndel Function :- ")
list1 = [2, 33, 222, 14, 25]
print ("Original list :- ",list1)  

del list1[-1] 
print (list1)    

del list