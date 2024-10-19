from collections import Counter

def find_key(nums):
    
    lists = [[] for _ in range(len(nums))]
    index = 0
    while True:
        for  num in nums:
            first_digit = str(num)[index]
            lists[index].append(first_digit)  
        index+=1
        if len(nums) == index:
            break
    result = ""
    for index in range(index): 
        count = Counter(lists[index])
        for key , value in count.items():
            if value == 1:
                result+=key
        
    return result
            
nums = [232326, 232363, 232523, 235323, 242323, 432323]

print(find_key(nums=nums))