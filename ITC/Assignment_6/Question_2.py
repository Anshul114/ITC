def is_palindrome(string):              #A palindrome is a word, phrase, or sequence that reads the same backward as forward

    if string == string[::-1]:
        return True

    else:
        return False

string = input("Enter the string : ")

print(is_palindrome(string))