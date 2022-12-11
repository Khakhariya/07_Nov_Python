import random

file = open ("58_test.txt","w")

file.write('''This is python.
This is program base on file handling 
Using file handling we can read any line from a file
but we read only random lines from file.
''')

file.close ()

read = open ("58_test.txt","r")

lines = read.readlines()
a = 0
print ("All lines of file :-\n")
for i in lines :
    print (f"{a} : {i}")
    a += 1

x = random.choice(lines)

print (f"Random line form file is :- \n{x}")

read.close()