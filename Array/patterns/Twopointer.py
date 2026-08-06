n=[2,5,11,15]
target=7
left=0
right=len(n)-1
while left<right:
    if (n[left]+n[right]==target):
        print(f"{n[left]}&{n[right]}")
        break
    elif n[left]+n[right]>target:
        right=right-1
    else:
        left=left+1
time complexity is :O(n)
space complexity is :O(1) but actually the sp