def find_short(s:str):
    
    string_len = []
    split_string = s.split()
    for string in split_string:
        string_len.append(len(string))
   
    small_integer = min(string_len)
    return small_integer


s = "bitcoin take over the world maybe  q who knows perhaps"
print(find_short(s))