
array = [3, 2, 2, 2, 2]
from  collections import Counter

def stray(arr: list):
    count = Counter(arr)
    for key, value in count.items():
        print(key, value)
        if value == 1:
            return key
                
            
    
    


print(stray(array))
