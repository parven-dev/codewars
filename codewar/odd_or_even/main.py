import math

def odd_or_even(arr):
    sum_of_num = 0
    for num in arr:
        sum_of_num+=num
    
    
    result = math.floor(sum_of_num)
    if result % 2 == 0:
        return "even"
    else:
        return "odd"

arr = [0, 1, 2]
print(odd_or_even(arr))