a=(1,2,3,4,5)
b=list(a)
count=0
for i in b:
    b[count] +=1
    count+=1
print(b)