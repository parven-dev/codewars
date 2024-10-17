def words_to_marks(s):
    
    words = {}
    for x, chars in enumerate(range(97, 122+1)):
        words[chr(chars)] = x+1
      
    total = 0  
    for word in  s:
        if word in words:
            # valuess = words.get(word)
            # total+=valuess
            total+=words.get(word)
               
    return total
    
s = "cqavtqnrlosxzcupr"
print(words_to_marks(s))