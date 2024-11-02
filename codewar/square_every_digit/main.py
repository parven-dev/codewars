def square_digits(num):
    # Your code here
    
    square_data = []
    for digit in str(num):
        square = int(digit) * int(digit)
        square_data.append(str(square))
    
    str_data = "".join(square_data)
    return int(str_data)

print(square_digits(num=9119))