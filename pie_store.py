import string
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffe", "Black Bun", "Buko", "Blueberry","Burek", "Tamale","Steak"]
basket = []
for i in range(len(pie_list)):
    print(f"({i}) {pie_list[i]}")

while True:
    pie = int(input("Which pie would you like to bring home? "))
    selection = pie
    basket.append(pie_list[selection])
    print(f"Great will have that {pie_list[selection]} right out for you")
    answer=input("Would you like some more? (y)es/(n)o ")
    if answer != "y":
        break

print("----------------------------------------")
print("-----------order summary----------------")
print(f"You've purchased: {len(basket)} pies")

basket.sort()
basket_output =[]
pie_name = ""
pie_count = 0

for pie in basket:
    if pie_name ==  pie:
        pie_count = pie_count + 1 
    else:
        if pie_name != "":
            basket_output.append(str(pie_count) + " X " + pie_name)
        pie_name = pie
        pie_count = 1
        
basket_output.append(str(pie_count) + " X " + pie_name)

for i in range(len(basket_output)):
    print(f"{basket_output[i]}")