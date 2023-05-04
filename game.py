import string
import random


def bot_move(count):
    if count == 1:
        return 1
    if (count - 4) % 4 == 2:
        return 1
    if (count - 4) % 4 == 3:
        return 2
    if count % 4 == 0:
        return 3

    return random.randint(1, 3)


print("How many pencils would you like to use:")
pencils = input()

while True:
    if len(list(filter(lambda item: item not in string.digits, pencils))) > 0:
        print("The number of pencils should be numeric")
        pencils = input()
    elif int(pencils) <= 0:
        print("The number of pencils should be positive")
        pencils = input()
    else:
        break

pencils = int(pencils)
names = ["John", "Jack"]
print(f"Who will be the first ({', '.join(names)}):")
name = input()

while name not in names:
    print(f"Choose between '{' and '.join(names)}'")
    name = input()

bot_index = 1
name_index = names.index(name)

while pencils > 0:
    print("".join(["|"] * pencils))
    print(f"{names[name_index]}'s turn:")

    if name_index == bot_index:
        minus = bot_move(pencils)
        print(minus)
    else:
        minus = input()

        while True:
            if minus not in ['1', '2', '3']:
                print(f"Possible values: '1', '2' or '3'")
                minus = input()
            elif int(minus) > pencils:
                print("Too many pencils were taken")
                minus = input()
            else:
                break

    pencils -= int(minus)
    name_index = 0 if name_index == len(names) - 1 else name_index + 1

print(f"{names[name_index]} won!")
