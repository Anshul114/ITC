def is_perfect(num):                         #A perfect number is a positive integer that is equal to the sum of its proper positive divisors

    add = 0

    for i in range(1,num):

        if num % i == 0:
            add += i

    return num == add
    
num = int(input("Enter the num : "))

print(is_perfect(num))