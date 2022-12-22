a = input("FIRST SIDE LENGTH: ")
b = input("SECOND SIDE LENGTH: ")
c = input("THIRD SIDE LENGTH: ")

a = int(a)
b = int(b)
c = int(c)

if (a + b <= c) or (a + c <= b) or (b + c <= a) :
    print("NO")
else:
    print("Yes")