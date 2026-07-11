li=[10,10,10,11]
li=list(set(li))
li.sort()
a=li[:-1]
b=li[:-2]
if a==b:
    print(-1)
else:
    print(li[-2])