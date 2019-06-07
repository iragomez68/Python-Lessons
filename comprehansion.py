import string

word = "Comprehansion"
letters = []
lettes = [letter for letter in word]
print(lettes)

capital_letters = []
capital_letters = [letter.upper() for letter in word]
print(capital_letters)

july_temp = [87, 85, 90, 79, 91]
hot_days = []
hot_days = [temp for temp in july_temp if temp >= 90]
print(hot_days)

guestnames = []
for _ in range(5):
    name = input("Please enter the name of someone you know: ")
    guestnames.append(name)

invitations = [f"Dear {name.title()}, please to our weading" for name in guestnames]

for invitation in invitations:
    print(invitation)