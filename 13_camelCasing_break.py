# Complete the solution so that the function will break up camel casing, using a space between words.

# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""   =>  ""

def break_camel_casing(a):
    new = ""
    for i in a:
        if i == i.upper():
            new+=f" {i}"
            continue
        new+=i
    return new

print(break_camel_casing("camelCasing"))
