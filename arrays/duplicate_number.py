def duplicate_number(arr):
    count={}
    for elem in arr:
        count[str(elem)]=count.get(str(elem),0)+1
    max_value=max(count.values())
    keys=[int(key) for key in count.keys() if count[key]==max_value]
    return keys[0]
print(duplicate_number([0, 1, 5, 5, 3, 2, 4]))
