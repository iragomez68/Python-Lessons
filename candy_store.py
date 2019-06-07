candy_list = ["sour patch", "kitcat", "oh henry", "reesses", "snickers", "aero", "jolly ranchers"]
for i in range(len(candy_list)):
    print(f"[{i}] {candy_list[i]}")
basket = []
print("choose 5 candies for you basket: [0-6]")
print(candy_list)
allowance = 5

print(".........")

for index, candy in enumerate(candy_list):
    print(f"[{index}] {candy}")

for x in range(allowance):
    candy = int(input(f"Choose your candy  {x + 1} : "))
    if (candy <0 or candy >6):
        print("please choose again")
    else:
        basket.append(candy_list[x]) 
for candies in basket:
    print(f"Your basket is: {basket} ")