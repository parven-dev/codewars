def sort_array(source_array):
    odd = sorted(num for num in source_array if num % 2 != 0)
    
    odd_iter = iter(odd)
    print(list(odd_iter)
 sorted odd numbers in the original positions
    sorted_array = [
        next(odd_iter) if num % 2 != 0 else num for num in source_array
    ]
    
    return sorted_array

# Example usage
sourc_arr = [5, 3, 2, 8, 1, 4, 11]
print(sort_array(sourc_arr))  
