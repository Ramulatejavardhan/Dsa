str="hello"
str1=[]
for i in range(len(str)-1,-1,-1):
    str1.append(str[i])
str1="".join(str1)
print(str1)