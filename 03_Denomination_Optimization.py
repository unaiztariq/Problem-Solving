# Problem 1. Write a program to take user input amount and check check that how many currency notes contains that amount.
# like notes 5000, 1000, 500, 100, 50, 20, 10, 5, 2,1

def denomination_optimization(amount):
    currency=[5000, 1000, 500, 100, 50, 20, 10, 5, 2,1]
    note_dict = {}
    total_notes_amount = 0
    for note in currency:
        if amount == total_notes_amount:
            break
        if amount < note:
            continue
        if amount < total_notes_amount + note:
            continue
   
        elif amount> total_notes_amount:
            num_of_notes=0
    
            while True:
                num_of_notes+=1
                total_notes_amount+=note
                if total_notes_amount > amount:
                    num_of_notes -=1
                    total_notes_amount -= note
                    note_dict[note] = num_of_notes
                    break

    return note_dict

print(denomination_optimization(5873))
