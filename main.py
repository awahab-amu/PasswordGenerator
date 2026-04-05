import random
import string

letters = list(string.ascii_uppercase + string.ascii_lowercase)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["!", "@", "#", "$", "%", "&", "*"]


print("Welcome to Password Generator!")

nr_letters = int(input("How many letters do you want in your password? "))
nr_symbols = int(input("How many symbols do you want? "))
nr_numbers = int(input("How many numbers do you want? "))

password = ""
for i in range(nr_letters):
    password += random.choice(letters)
for i in range(nr_symbols):
    password += random.choice(symbols)
for i in range(nr_numbers):
    password += str(random.choice(numbers))

# shuffled_password = "".join(random.sample(password, len(password)))
# print(shuffled_password)

password_list = list(password)
random.shuffle(password_list)
shuffled_password = "".join(password_list)
print(shuffled_password)
