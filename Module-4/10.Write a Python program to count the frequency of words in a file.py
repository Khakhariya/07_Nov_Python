from collections import Counter

File = open ('Text.txt','r')

x = Counter(File.read().split())

print(x)

File.close()