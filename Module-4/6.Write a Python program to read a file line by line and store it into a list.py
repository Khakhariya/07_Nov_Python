List = []

File = open ('Text.txt','r')

for i in File :
    print (i)
    List.append(i)

print (f"\nStore in List :- {List}")

File.close()