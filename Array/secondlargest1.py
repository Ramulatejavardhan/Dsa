arr=[1,2,3,6,5,7,6,4]
largest=0
secondlarge=0
arr=list(set(arr))
print(arr)
for i in arr:
    if i>largest:
        largest=i
    else:
        break
for j in arr:
    if j>secondlarge and largest>j:
        secondlarge=j
    else:
        break
print(secondlarge)