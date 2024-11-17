from collections import Counter


def duplicate_count(text : str) -> str:
    # Your code goes here
    duplicate = []
    text = text.lower()
    
    counter = Counter(text)
    for key, value in counter.items():
        if value > 1:
            duplicate.append(value)
    
    return len(duplicate)

        

    
text = "abcdeaB"
print(duplicate_count(text))