

def longest(a:str, b:str):

    not_exist_data = ""
    for data in (a + b):
        if data not in not_exist_data:
            not_exist_data+=data

    sorted_data = sorted(not_exist_data)
    return "".join(sorted_data)

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

print(longest(a, b))
