# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
# The function should return true if the string is valid, and false if it's invalid.

# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(( )) ((( ) ( )) ( ) )"  =>  true

def brackets(a):
    if a[0] == "("and a[len(a)-1] == ")" :
        open =0
        close =0
        for i in range(0,len(a)):
            if a[i] == ")":
                close+=1
            elif a[i] == "(":
                open+=1
        if open==close:
            return True
        return False

print(brackets("(())((()())())"))
