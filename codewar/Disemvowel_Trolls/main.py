def disemvowel(string_: str) -> str:
    vowels = ["a", "i", "e", "o", "u"]

    
    data = [char for char in string_ if char.lower() not in vowels]
    return "".join(data)
    
    
   


string_ = "This website is for losers LOL!"
print(disemvowel(string_=string_))
