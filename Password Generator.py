#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
lenght_of_letters = len(letters)
lenght_of_symbols = len(symbols)
lenght_of_numbers = len(numbers)
password = ""
for characters in range (0, nr_letters):
  password = password + letters[random.randint(0, lenght_of_letters-1)]
for characters in range (0, nr_symbols):
  password = password + symbols[random.randint(0, lenght_of_symbols-1)]
for characters in range (0, nr_numbers):
  password = password + numbers[random.randint(0, lenght_of_numbers-1)]
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
l = [*password]
random.shuffle(l)
print("".join(l))
