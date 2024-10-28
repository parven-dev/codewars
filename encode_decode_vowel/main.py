def encode(st : str):
    vowels = {"a":1, "e": 2, "i" : 3, "o": 4, "u": 5}
        
    data = []
    for key, value in vowels.items():
        if key in st:
            st = st.replace(key, str(value))
            data.append(st)
            
    if len(data) == 0:
        return st
    else:
        data[-1]
    
st = 'cpxssksmvtwvj'
# print(encode(st))
                    
def decode(st):
    vowels = {"a":1, "e": 2, "i" : 3, "o": 4, "u": 5}
    data =[]
    
    for key, value in vowels.items():
        if str(value) in st:
            st = st.replace(str(value), key)
            data.append(st)
            
    if len(data) == 0:
        return st
    else:
        return data[-1]




st = 'rxg3syjg12bwyxxrxvvcrnxxcl1xpv'
print(decode(st))