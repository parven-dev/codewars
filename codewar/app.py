
def trailing_zeros(n) ->int:
    binary = bin(n)
    my_list = []
    reversed_binary = list(reversed(binary))

    for binary_item in (reversed_binary):
        my_list.append(binary_item)
        if binary_item == "1":
            break
    binary_data = "".join(my_list[:-1])
    if binary_data:
        return len(binary_data)
    else:
        return 0



n = 5
print(trailing_zeros(72))
