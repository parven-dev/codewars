def alphabet_position(text:str):
    # 97 = a, 122 = x
    
    # 'b' ord('b') - ord('a') = 1
    # 't' ord('t') - ord('a') = 19

    data = []
    for  nums in text.lower():
        nums = ord(nums)
        if nums >= 97 and nums <= 122:
            data.append(chr(nums))
    result = []
    for num in data:
        nums = ord(num)
        positioned = nums- ord("a") + 1
        result.append(str(positioned))
        
    return  " ".join(result)

text = "The sunset sets at twelve o' clock."
print(alphabet_position(text))