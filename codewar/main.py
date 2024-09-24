def high_and_low(numbers: str):
  split_num = numbers.split(" ")
  num = [int(items) for items in split_num ]
  max_num =  str(max(num))
  min_num = str(min(num))
  combine_num = max_num + " " + min_num
  return combine_num
  
 

numbers = ("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
print(high_and_low(numbers=numbers))