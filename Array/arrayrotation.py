# left rotation
arr=[1,2,3,4,5]
last=len(arr)-1
temp=arr[0]
j=1
for i in range(0,last):
    if j>len(arr):
        break
    else:
        arr[i]=arr[j]
        j=j+1
arr[last]=temp
print(arr)