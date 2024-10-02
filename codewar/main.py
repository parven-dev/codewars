def vaporcode(s:str):
    #your code here
    upper_case = s.upper()
    removed_space = upper_case.replace(' ', "")
    resutl = ""
    for word in removed_space:
        string_with_space  = word + "  " 
        resutl+=string_with_space
    
    return resutl.strip()
            
    
    
s  = "Why isn't my code working"
print(vaporcode(s))