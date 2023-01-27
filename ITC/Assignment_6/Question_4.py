def is_pangram(string):                     #Pangrams are words or sentences containing every letter of the alphabet at least once.

    string_1 = "abcdefghijklmnopqrstuvwxyz"

    for pointer in string_1:

        if pointer not in string.lower():               
            return False

    return True

string = input("Enter the string: ")

print(is_pangram(string))