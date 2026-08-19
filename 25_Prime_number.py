# flag concept

def check_prime(pn):
    flag = 0
    for i in range (2,pn):
        if pn%i == 0:
            flag = 1
            print(f"{pn} is not a Prime number, Firstly because of {i}.")
            break
    if flag ==0:
        print("Prime number")

check_prime(89)
