import random

points = 0

for i in range(0,10):
    num1 = random.randint(2,21)
    num2 = random.randint(2,21)
    ans = num1 * num2

    print("What is ", num1 , '*' , num2, '?')
    num3 = int(input())

    if num3 !=ans:
        print("Wrong. The answer is ", ans)
        print("Your total points are", points)
        
    else:
        print("Right!" )
        points += 1
        print("Your total points are ", points)