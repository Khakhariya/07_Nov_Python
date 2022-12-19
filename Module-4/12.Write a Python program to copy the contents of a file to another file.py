x = []

File1 =open ('3_Text.txt','r')

x = File1.readlines()

File1.close()

File = open ('Text.txt','w')

for i in x :
    File.write(i)

File.close()