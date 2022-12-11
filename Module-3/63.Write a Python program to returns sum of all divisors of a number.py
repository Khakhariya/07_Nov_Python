def sum_divisors (number):
    a = 0
    for i in range (1,number) :
        if number % i == 0 :
            a = a + i
    print (a)

num = int (input ("Enter the number to get sum of all divisors of number :- "))
sum_divisors (num)