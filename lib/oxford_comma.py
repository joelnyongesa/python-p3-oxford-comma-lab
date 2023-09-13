# separator.join(items-to-join)


def oxford_comma(items):
    '''Logic: If length of array is 1, return the item. If the length is 2, return 'item 1 and item 2' else, join the items to a string, grab the last word and append it to the result'''
    if(len(items) == 1):
        return items[0]
    elif(len(items) == 2):
        return f"{items[0]} and {items[1]}"
    else:
        last_word = items[-1]
        return(f"{', '.join(items[0:-1])}, and {last_word}")

print(oxford_comma(["fiddleheads", "okra", "kohlrabi"]))