def find_number (list1):
    sum = int()
    list1.sort()
    for i in list1 :
        sum = sum + i
    print (f"largest number is : {list1[-1]}")
    print (f"smallest number is : {list1[0]}")
    print (f"sum of all numbers in list : {sum}")

number = []
n = int (input ("Enter the number to run loop : "))
for i in range (n) :
    num = int (input ("Enter the number : "))
    number.append(num)
print (number)

find_number(number)