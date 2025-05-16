


def grabscrab(said, possible_words):
    to_match_with = "".join(sorted(said))
    sorted_strings = []
    
    for string in possible_words:
        sorted_str = "".join(sorted(string))
        if sorted_str == to_match_with:
            sorted_strings.append(string)
            
    return sorted_strings



said = "ortsp"
possible_words = ["sport", "parrot", "ports", "matey"] 

result = grabscrab(said, possible_words)
print(result)


# matchb  = sorted(match)
# matchc = sorted(a[0])

# print(matchb, matchc)