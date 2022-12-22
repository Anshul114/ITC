string = "Python is a case sensitive language";

print(len(string));         #a

print(string[::-1]);        #b

string2 = string[10:26];    #c
print(string2);

string3 = "object oriented";    #d
string4 = string.replace(string2,string3);
print(string4)

print(string.find("a"));        #e

string5 = ""                    #f
for i in string:
    if i != " ":
        string5 = string5 + i
print(string5)




