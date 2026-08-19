# Character Frequency: Given a string, count the occurrences of each character and 
# return a dictionary mapping each character to its frequency. Treat uppercase and lowercase as distinct.

# Input: A string s.
# Output: A dictionary {char: count}.
# Example: s = "banana" -> output {'b': 1, 'a': 3, 'n': 2}.

def frequency(s):
    dict1= {}
    for i in s:
        if i in dict1:
            value = dict1[i] +1
            dict1[i] = value
        else:
            value = 1
            dict1[i] = value
    return dict1

print(frequency("banana"))
