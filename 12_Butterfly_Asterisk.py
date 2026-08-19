"""__________________________________________________________________________________________"""

""" BUTTERFLY """

def butterfly_pattern(a):
    b = "*"
    c = a
    for i in range (1,a+1):
        if i <= a/2:
            c-=2
            d = (b*i) + ((" ")*c) + (b*i)
            print(d)
        else:
            c+=2
            if a%2==0:
                d = (b*(i-c)) + ((" ")*c) + (b*(i-c))
                print(d)
            else:
                d = (b*(i-c+1)) + ((" ")*c) + (b*(i-c+1))
                print(d)

butterfly_pattern(10)
