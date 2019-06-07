# Loop while a condition is being met
run = "y"
loop_size  = 0
step_size = 1
loop_start = 2
while run == "y":
    print("Hi!")

    loop_size = int(input("Enter loop size: "))
    step_size  = int(input("Enter step size: "))
    loop_size = loop_size + loop_start
    for x in range(loop_start,loop_size,step_size):
        print(x)

    loop_start = x + 1
    run = input("To run again. Enter 'y'")