def factorial () :
    number = int (input ("Enter the number to find factorial of numbers : "))
    res = 1
    for i in range (number):
        res = res * (i+1)
    print (f"Factorial of {number} is : {res}")

def user_list () :
    list1 = []
    n = int(input("Enter the list of items :-"))
    for i in range (n):
        list_item = input("Enter the item of list")
        list1.append(list_item)
    return list1

def user_dict ():
    keys = []
    values = []

    n = int (input ("Enter the number of keys :- "))

    for i in range (n):
        key = input("Enter the key :- ")
        value = input("Enter the value :- ")
        keys.append(key)
        values.append(value)
    x = dict(zip (keys,values))
    return x


def error_handle ():
    from builtins import int
    while True:
        try:
            n=input("Enter the value : ")
            n=int(n)
            break
        except Exception:
            print("Invalid Input")
        finally:
            print("Finally Called")
    print("Bye")