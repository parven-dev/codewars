data = []
x = 10
for num in range(1, x+1):
    # Loop to jump in powers of 2
    square_num = num*num
    data.append(square_num)
    
    while True:
        if num < x:
            print(num)