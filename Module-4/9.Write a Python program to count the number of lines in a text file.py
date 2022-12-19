File = open ('Text.txt','r')

a = 0
for i in File :
    a += 1
    
print (f"Number of lines in file is : {a}")

File.close()