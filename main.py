import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "(){}[],;.;:/-?+@#"

upper = input("voulez vous des majuscules ? oui/non")
lower = input("voulez vous des minuscules ? oui/non")
nums = input("voulez vous des chiffres ? oui/non")
syms = input("voulez vous des symboles ? oui/non")

all = ""

if upper == "oui":
  all += uppercase_letters
if lower == "oui":
  all += lowercase_letters
if nums == "oui":
  all += digits
if syms == "oui":
  all += symbols

lenght = int(input("quelle longueur souhaitez-vous ?"))
amount = int(input("combien de mdp souhaitez-vous ?"))


for x in range(amount):
  password = "".join(random.sample(all, lenght))
  print(password)


