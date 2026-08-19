# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p. 
# we want to find a positive integer k, if it exists,
# such that the sum of the digits of n taken to the successive powers of p is equal to k * n.


# dig_pow(695, 2) should return 2 since 6^2 + 9^3 + 5^4= 1390 = 695 * 2
# dig_pow(46288, 3) should return 51 since 4^3 + 6^4+ 2^5 + 8^6 + 8^7 = 2360688 = 46288 * 51

def dig_pow(n,p):
    n=str(n)
    num = 0
    for i in n:
        i=int(i)
        num += i**p
        p+=1
    n =int(n)
    if num%n==0:
        return int(num/n)
    else:
        return "does not exist..."
    
print(dig_pow(46288, 3))
