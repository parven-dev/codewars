def capitals(word : str) -> str:
    #your code here
    string_index = [item for item in range(len(word)) if word[item].isupper()]
    return string_index

word = "BOKFxWJvDCoTVHhLZyfSSUheg"
output = "[0, 1, 2, 3, 5, 6, 8, 9, 11, 12, 13, 15, 16, 19, 20, 21]"
print(output)
print(capitals(word=word))