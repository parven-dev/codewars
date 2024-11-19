def order(sentence:str) -> str:
  # code here
  
  string = sentence.replace(" ", "")
  to_hex = []
  for item in string:
    if ord(item )>= 49 and ord(item) <= 59:
      to_hex.append(chr(ord(item)))
  
  
  sorted_list = sorted(to_hex)
  print(sorted_list[0])
  
  for i, items in enumerate(sentence.split(" ")):   
    string_data =  str(sorted_list[i])
    print(string_data)

    if string_data in items:
      print(sorted_list[i])
    
    # if sorted_list[items] in sentence[items]:
      
    #   print(sentence[items])
        
            
  return sorted_list




sentence = "is2 Thi1s T4est 3a"
print(order(sentence))

# Thi1s is2 3a T4est"