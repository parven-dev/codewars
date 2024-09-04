def distinct(seq):

    removed_duplicate = []
    for item in seq:
        if item not in removed_duplicate:
            removed_duplicate.append(item)     

        
    return removed_duplicate


seq = [1, 1, 2]
print(distinct(seq=seq))