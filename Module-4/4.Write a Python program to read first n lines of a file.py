File = open('3_Text.txt','r')

lines = int (input ("Enter First n lines to show : "))

for i in range (lines):
    print(File.readline())

File.close()