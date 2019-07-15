def add_one(arr):
    num=""
    for element in arr:
        num+=str(element)
    num=int(num)
    num+=1
    num=str(num)
    arr=[]
    for element in num:
        arr.append(int(element))
    return arr
print(add_one([9,9,9]))
