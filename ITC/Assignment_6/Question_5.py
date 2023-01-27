string = input("Enter the string : ")

split = string.split("-")                     #spilt(separator, max limit) - converts string into list by spilting-be default whitesapce is seapartor

split.sort(reverse = False)              #sort() method sorts the list ascending by default.

string1 = "-".join(split)                      #Join() all items in a tuple into a string, using a hash character as separator:

print(string1)



