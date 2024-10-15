def move_ten(st: str):
    char_string = ""
    for string in st:
        char = ord(string) + 10
        if char > 122:
            chars = char - 122 
            move_chars = chr(chars+96)
            char_string+=move_chars
        else:
            chars_refine  = chr(char)
            char_string+=chars_refine
    
    return char_string
        
# print(chr(97))
# print(ord("g"))
s = "exampletesthere"
print(move_ten(s))