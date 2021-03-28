def sum_divisible(x,y,z):
    result = 0
    for number in range(x,y+1):
        if number % z == 0:
            result+=number
    return result

print(sum_divisible(1,16,4))