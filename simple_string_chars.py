

def solve(s:str):
    upper = ""
    lower = ""
    number = ""
    special_char = ""
    for string in s:
        if string.isupper():
            upper+=string
        elif string.islower():
            lower+=string
        elif string.isdigit():
            number+=string
        else:
            special_char+=string
            
    return [len(upper), len(lower), len(number), len(special_char)]


s = "Codewars@codewars123.com"
print(solve(s))