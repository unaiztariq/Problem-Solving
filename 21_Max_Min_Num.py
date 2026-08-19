"""__________________________________________________________________________________________"""
#Q9/ Q10: Create a function that takes a list of numbers as input and 
# returns the maximum and minimum number in the list.
"""__________________________________________________________________________________________"""

def max_min_interactive():
    a = []
    b = int(input("Enter number in the list: "))
    a.append(b)
    for i in range (1,10):
       com = str(input("Want to add another number(press \"y\" for yes and \"n\" for no): "))
       if com == "y":
        c = int (input("Enter a another number: "))
        a.append(c)
       elif com == "n" :
        print (" Thank you, for adding numbers.")   
        break   
       else:
        print("Invalid input.")
        break
    a.sort()
    print(f"{a[0]} is the smallest number.")
    print(f"{a[len(a)-1]} is the largest number.")


def max_min_space_separated():
    a = (input("Enter numbers with space: ")).split()
    c = list(map(int,a))
    c.sort()
    b = len(a) -1
    print(f"{c[0]} is the smallest number.")
    print(f"{c[b]} is the largest number.")


def max_min_from_list(a):
    a.sort()
    b = len(a) -1
    print(f"{a[0]} is the smallest number.")
    print(f"{a[b]} is the largest number.")

max_min_from_list([23,340,56,576,26])
