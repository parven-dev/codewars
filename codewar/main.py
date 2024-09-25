def get_count(sentence):
    get_vowl = ''
    for vowl in sentance:
        if vowl in "aeiou":
            get_vowl+=vowl
            
    return len(get_vowl)
sentance  = "abracadabra"
print(get_count(sentence=sentance))


