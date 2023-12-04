import random

def name_friends():
    print("Enter the name of every friend (including you), each on a new line:")
    for x in range(num_friends):
        name = input()
        friends[name] = 0


def split_bill(bill):
    if bill % num_friends == 0:
        part = int(bill / num_friends)
    else:
        part = round(bill / num_friends, 2)
    return part



def split_bill_with_lucky(bill):
    if bill % (num_friends - 1) == 0:
        part = int(bill / (num_friends - 1))
    else:
        part = round(bill / (num_friends - 1), 2)
    return part


print("Enter the number of friends joining (including you):")
num_friends = int(input())
friends = {}
if num_friends >= 1:
    name_friends()
    print("Enter the total bill value:")
    total_bill = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    yes_no = input()
    if yes_no == "Yes":
        random.seed()
        lucky_name = random.choice([n for n in friends])
        print(f"{lucky_name} is the lucky one!")
        for key in friends:
            if key == lucky_name:
                friends[key] = 0
            else:
                friends[key] = split_bill_with_lucky(total_bill)
        print(friends)
    else:
        print("No one is going to be lucky.")
        for key in friends:
            friends[key] = split_bill(total_bill)
        print(friends)
else:
    print("No one is joining for the party")