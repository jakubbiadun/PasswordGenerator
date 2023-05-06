# Password Generator
import random

lowerCharacters = "abcdefghijklmnoprstwqxz"
upperCharacters = "ABCDEFGHIJKLMNOPRSTWQXZ"
digits = "123456789"
symbols = "_+=-!@#$%^&*?,."
characters = lowerCharacters + upperCharacters + digits + symbols

length = int(input("Enter the length of the password: "))

password = []
for i in range(length):
    password.append(random.choice(characters))

print("".join(password))