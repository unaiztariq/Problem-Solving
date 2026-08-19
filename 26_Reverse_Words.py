# Complete the function that accepts a string parameter, and reverses each word in the string.
# All spaces in the string should be retained.

def reverse_words(a):
    c = []
    b = list(a.split())
    for i in b:
        mod_i = reversed(list(i))
        mod_i= "".join(mod_i)
        c.append(mod_i)

    d = " ".join(c)
    return d

print(reverse_words("This is an example!"))
