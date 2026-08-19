
# Check Palindrome: Given a string, write a function to determine if it is a palindrome
# (reads the same forward and backward), ignoring case and non-alphanumeric characters.

# Input: A string s.

# Output: A Boolean (True or False) indicating whether s is a palindrome.

# Example: s = "RaceCar!" -> output True (ignoring case and the exclamation mark).

def palindrome(string):
    re_string=""
    legit_string = "".join([letter for letter in string if letter not in "!.,:"])
    for index in range (len(string)-1,-1,-1):
        if string[index] in "!.,:":
            continue
        re_string+= string[index]
    
    if legit_string == re_string:
        return True
    else:
        return False

print(palindrome("RaceCar!"))
