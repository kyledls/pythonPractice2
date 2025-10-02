import random

letters = ['a', 'b', 'c', 'd']
numbers = ['0', '1', '2']
symbols = ['!', '#', '$']

print("Welcome to PyPassword Generator")
nr_letters = int(input("How many letters? "))
# nr_symbols = int(input("How many symbols?\n"))
# nr_numbers = int(input("How many numbers?\n"))

password = []

for char in range(1, nr_letters+1):
    letters_text = random.choice(letters)
    password.append(letters_text)


password_new = " "

for char in password:
    password_new += char

print(password_new)