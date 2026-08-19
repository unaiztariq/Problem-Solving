# fibonacci series 0,1,1,2,3,5,8,13,...

def fibonacci_basic(n):
    a= 0 
    b=1
    print(a)
    print(b)
    for i in range(n-2):
        a,b= b,a+b
        print(b)


def fibonacci_comma_output(x):
    a = 0
    b = 1
    print("0,1",end="")
    for i in range ( 2,x):
        print(f",{a+b}",end="")
        a += 1
        b += 1


def fibonacci_with_limit(x):
    a = 0
    b = 1
    print("0,1",end="")
    for i in range ( 2,x):
        if a+b != x:
            print(f",{a+b}",end="")
            a += 1
            b += 1
        else :
            break

fibonacci_basic(10)
