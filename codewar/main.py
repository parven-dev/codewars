def explode(arr):  
    array = []
    for item in arr:
        if type(item) == int:
            for _ in range(item):
                array.append(arr)
                
        if all(isinstance(x, str) for x in arr):
            return "Void!"
            
    return array
arr = ["f", "r"]
print(explode(arr))

