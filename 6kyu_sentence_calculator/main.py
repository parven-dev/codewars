def letters_to_numbers(s):
        alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
        total = 0
        
        
        for i in range(len(s)):
            if s[i].islower():
                if s[i].islower() in alphabet_dict.values():
                    total+=alphabet_dict[s[i]]
                          
            elif s[i].isupper():
                lower_value = s[i].lower()
                if lower_value in alphabet_dict:
                    total+=alphabet_dict[lower_value] * 2
            elif s[i].isdigit():
                total+=int(s[i])

        return total
        
# s =  "I Love You"
s = 'Give me 5!'

print(letters_to_numbers(s))