def move_vowels(input): 
    
    front_char = ""
    end_char_vowels = ""
    
    for item in input:
        if item in "aeiou":
            end_char_vowels+=item
        else:
            front_char+=item
    
    word_with_vowels =  front_char + end_char_vowels
    return word_with_vowels

input = "programming"
print(move_vowels(input=input))