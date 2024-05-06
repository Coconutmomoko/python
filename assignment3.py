
# 1.
username = "python"
password = "rules"
counts = 0
while counts < 5:
    input_username = input("Enter username:")
    input_password = input("Enter password:")
    if input_username == username and input_password == password:
        print("Welcome")
        break
    else:
        print("Incorrect username or password.Please try again")
        counts += 1

if counts == 5:
    print("Access denied")


# 2.
num_dice = int(input("Enter the number of dice to roll:"))
sum_dice = 0
for x in range(num_dice):
    import random
    roll = random.randint(1, 6)
    print("Dice roll:", roll)
    sum_dice += roll

print("Sum of dice rolls:", sum_dice)


# 3.
numbers = []
while True:
    num = input("Please enter a number. Enter a null value to end:")
    if num == "":
        break
    numbers.append(int(num))

numbers.sort(reverse=True)
top_five_numbers = numbers[:5]
print("The five greatest numbers in descending order are:")
for num in top_five_numbers:
    print(num)


# 4.
cities = []
for i in range(5):
    city = input(f"Enter the name of city{i+1}:")
    cities.append(city)
print("Cities entered:")
for city in cities:
    print(city)


# 5.
import random


def roll_dice():
    return random.randint(1, 6)


while True:
    roll = roll_dice()
    print(f"The dice rolled: {roll}")
    if roll == 6:
        break


# 6.
def convert_to_liters(gallons):
    liters = gallons * 3.78541
    return liters


def run_program():
    while True:
        gallons = float(input("Enter a volume in gallons (negative value to exit): "))
        if gallons < 0:
            return
        liters = convert_to_liters(gallons)
        print(f"{gallons} gallons is equal to {liters} liters.")


run_program()
