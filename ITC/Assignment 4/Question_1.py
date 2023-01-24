marks = int(input("Enter Marks : "))

if marks <= 25 and marks >= 0:
    print('F')

elif marks <= 45 and marks > 25:
    print('E')

elif marks <= 50 and marks > 45:
    print('D')

elif marks <= 60 and marks > 50:
    print('C')

elif marks <= 80 and marks > 60:
    print('B')

elif marks <= 100 and marks > 80:
    print('A')

else:
    print("Enter Valid Marks")  