def words_to_marks(s):
    
    words = {}
    
    for x, chars in enumerate(range(97, 122)):
        words[chr(chars)] = x+1
      
      
    total = 0  
    for word in  s:
        if word in words:
            valuess = words.get(word)
            total+=valuess
            
        
    return total
        
    
    
s = "attitude"
print(words_to_marks(s))