File = open('Text.txt','r')

a = True
while (a == True):
    try :
        lines = int (input ("Enter last n lines to show : "))
        a = False
    except :
        print ('Error!')

for line in (File.readlines() [-lines:]):
    
    print(line, end ='')

File.close()