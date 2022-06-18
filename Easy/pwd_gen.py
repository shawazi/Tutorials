import random

print("Welcome to your password generator!")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

number = input("Amount of passwords to generate: ")
number = int(number)

length = input("Input your password length: ")
length = int(length)

print("\nHere are your passwords: ")

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)