
def sum_of_integer(number):
    if number == 0:
        return 0
    else:
        return int(number%10) + sum_of_integer(int(number//10))
        
print(sum_of_integer(114411))
