arr=[1,2,3,4]
del arr[1]
print(arr)

#delete an array if it is present in arr (occurence)
a=10
if a in arr:
    arr.remove(a)
else:
    print("num not present")