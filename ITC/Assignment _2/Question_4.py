a = input("ENTER FIRST NUMBER: " );
b = input("ENTER SECOND NUMBER: " );
c = input("ENTER THIRD NUMBER: " );

a = int(a);
b = int(b);
c = int(c);

if a > b:
    if a > c:
        print("First num is largest");
    else:
        print("Third is largest");
        
elif a < b:
        if b > c:
            print("Second num is largest");
        else:
            print("Third num is largest");