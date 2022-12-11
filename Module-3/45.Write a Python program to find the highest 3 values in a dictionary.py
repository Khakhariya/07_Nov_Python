'''Input : my_dict = {'A': 67, 'B': 23, 'C': 45,
                   'D': 56, 'E': 12, 'F': 69} 
Output : {'F': 69, 'A': 67, 'D': 56}'''

my_dict = {'A': 67, 'B': 23, 'C': 45,'D': 56, 'E': 12, 'F': 69}
print (f"Original dictionary {my_dict}")
x = list (my_dict.values())
x.sort()
print ("Highest three values in dictionary is unders : -")
print(x[-3:])