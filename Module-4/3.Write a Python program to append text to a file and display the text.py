File = open ('3_Text.txt','r+')

city = input ("Enter City : ")

File.write(f"City : {city}\t\n")

for i in File :
    print (i)

File.close()