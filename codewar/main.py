def longest_consec(strarr, k):
    
    string_length = ""
    if k < len(strarr) and k > 0:
        for string in range(len(strarr)):
            string_added = strarr[string:string+k]
            if len(string_added) == k:
                strin = "".join(string_added)
                string_length+=strin + ","
    if k  == 0 or k > len(strarr) or k < 0:
        return ""
    
    
    split_str = string_length.split(',')
    len_stinng = []
    for item in split_str:
        len_stinng.append(len(item))
    return len_stinng

starr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
k = 0

print(longest_consec(starr, k))