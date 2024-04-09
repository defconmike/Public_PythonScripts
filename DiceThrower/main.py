#          Name: DiceThrower
#   DateCreated: 04-08-24
#  DateModified: 04-08-24
#       Version: 01.00.01
#        Author: defconmike
#
import random
from collections import Counter
reroll = "yes"
msg_welcome = 'Lets roll some dice!'
msg_exit = "Have a nice day!"
print(msg_welcome)
while reroll == "yes" or reroll == "y":
    nodieprompt = input('How many dice would you like to throw?')
    try:
        nodieinput = int(nodieprompt)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue
    if nodieinput <= 0:
            break
    elif (nodieinput == 1):
        nosideprompt = input('How many sides to your die?')
    elif (nodieinput > 1):
        nosideprompt = input('How many sides to your dice?')
    try:
        nosideinput = int(nosideprompt)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    my_list = []
    for _ in range(nodieinput):
        dice = random.randint(1, nosideinput)
        my_list.append(dice)
        # print(dice)
    # print(my_list)
    sorted_results = sorted(my_list)
    dieresults = Counter(sorted_results)
    print("Occurrences of each number:")
    for dienumber, count in dieresults.items():
        print(f"{dienumber}: {count}")
    reroll = input("Press 'y' or 'yes' to roll again.")
print(msg_exit)
