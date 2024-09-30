def count(s : str ):
    # The function code should be here
    
    count_string = {}
    
    for string in s:
        if string in count_string:
            count_string[string]+=1
        else:
            count_string[string] =1
            
    return count_string
            
s  = 'aabb'
print(count(s))