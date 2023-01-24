# n is number of candies in bowl

for n in range(201):                        # by looking at bowl, n is less than 200

    if n % 5 == 2:                          # n divides among 5 people, 2 candies were left in bowl

        if n % 6 == 3:

            if n % 7 == 2:
                print(n)
