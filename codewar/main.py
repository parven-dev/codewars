def to_float_array(arr):
    float_arr = [float(string_arr) for string_arr in arr]
    return float_arr


arr = ["1.1", "2.2", "3.3"]
print(to_float_array(arr))