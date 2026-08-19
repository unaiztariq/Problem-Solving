# Write a function which will take an integer as input and print each digit in a separate line.
# You are not allowed to use str or any other method will convert the integer into string.

def digit_separation(num):
    while True:
        if num <10:
            print(num)
            break
        last_num = num%10
        print(last_num)
        num = num//10

digit_separation(1011)
