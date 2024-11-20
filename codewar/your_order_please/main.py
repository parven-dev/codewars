def order(sentence:str) -> str:
  # code here
  
  # string = sentence.replace(" ", "")
  # to_hex = []
  # for item in string:
  # #   if ord(item )>= 49 and ord(item) <= 59:
  # #     to_hex.append(chr(ord(item)))
  
  
  # # sorted_list = sorted(to_hex)
  
  data = []
  
  words = sentence.split(" ")
  # print(words)
  for items in range(1, len(words) + 1):
    # print(items) 
    index = items - 1
    # print(words[index])
    if str(index) in words:
      # print(str(index))
      data.append("uess")
             
  return data

sentence = "is2 Thi1s T4est 3a"
print(order(sentence))

# Thi1s is2 3a T4est"