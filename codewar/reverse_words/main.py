def reverse_words(text:str) -> str:
    
    reverse_string  = text[::-1]
    reverse_string = reverse_string.split(" ")
    return " ".join(reverse_string[::-1])

    

text = "The quick brown fox jumps over the lazy dog."
print(reverse_words(text))

