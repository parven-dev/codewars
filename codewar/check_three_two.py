def check_three_and_two(array):
    a =[]
    b = []
    c = []
    for chars in array:
        if chars == 'a':
            a.append(chars)
        if chars == "b":
            b.append(chars)
        if chars == "c":
            c.append(chars)
    
    if len(a) in [2, 3] or len(b) in [2, 3] or len(c) in [2, 3]:
        return True
    else:
        return False


array = ["a", "a", "a", "b", "b"]
print(check_three_and_two(array=array))