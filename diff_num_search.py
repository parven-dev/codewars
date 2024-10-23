from collections import Counter

def different_digits_number_search(arr):
    
    
    lists = [[] for _ in  range(len((arr)))]
   
    for index, num in enumerate(arr):
        lists[index].append(num)

    index = 0
    my_lists = [[] for _ in  range(len((arr)))]
    while True:
        for item in lists[index]: 
            for items in (str(item)):
                my_lists[index].append(items + ",")
        index+=1
        
        if index == len(lists):
            break
    
    one_value = []
    for  list in my_lists:
        count = Counter(list)
        if all(values == 1 for values in count.values()):
            one_value.append(count.keys())
    
    if len(one_value) == 0:
        return -1
    else:        
        result = [item for item in one_value[0]]
        list_value = "".join(result).replace(",", "")
        string_value =  "".join(list_value)
        return string_value

    
arr = [22, 111]
print(different_digits_number_search(arr=arr))
