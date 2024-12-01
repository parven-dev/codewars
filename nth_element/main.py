def nth_smallest(arr, pos):
    #your code 
    arr1 = sorted(arr)
    print(arr1)

    for _ in range( pos):
        
        return arr1[pos-1]
        

arr=[-5,-1,-6,-18]
pos = 4

print(nth_smallest(arr=arr, pos=pos))