def sort_array(source_array):
    # Extract odd numbers and sort them
    odd = sorted(num for num in source_array if num % 2 != 0)
    
    # Iterator for the sorted odd numbers
    odd_iter = iter(odd)
    print(list(odd_iter)
    
    # Create a new array with sorted odd numbers in the original positions
    sorted_array = [
        next(odd_iter) if num % 2 != 0 else num for num in source_array
    ]
    
    return sorted_array

# Example usage
sourc_arr = [5, 3, 2, 8, 1, 4, 11]
print(sort_array(sourc_arr))  # Output: [1, 3, 2, 8, 5, 4, 11]
