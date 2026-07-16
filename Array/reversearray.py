arr=[1,2,3,4,5]
left=0
right=len(arr)-1
arr1=[0]
for i in range(right,left-1,-1):
    arr1=arr[i]
print(arr1)