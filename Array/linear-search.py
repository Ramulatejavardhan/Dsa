arr=[1,2,3,4]
index=0
find=11
if find in arr:
    for i in arr:
        if i==find:
            print(index)
        else:
            index=index+1
else:
    print(-1)