# searching a letter on string
s="geekforgeeks"
l=input("Enter a letter to find:")
for i in s:
    if l==i:
        print(s.index(i))
        break
else:
    print("not found")