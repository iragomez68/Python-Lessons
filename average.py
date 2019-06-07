def average(numberList):
    total = 0.0
    for number in numberList:
        total = total + number
    count = len(numberList)
    avg = total/count
    return avg 



print(average([1,2,3]))