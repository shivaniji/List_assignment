
# 1

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digits[::-1])

# 4
a=[1,3,2,1,2,4,6,7]
i=0
c=[]

while i< len (a):
    if a[i] not in c:
        c.append(a[i])
    i=i+1
print(c)

# 5
a=[2,4,3,5,4,3]
b=[2,5,3,2,9,7]
c=(a+b)

# 2 mean
a=[2,3,4,1,4,33,2,12,34,56,9,87,7]
i=0
sum=0
av=0
while i < len (a):
  
    sum=sum+a[i]
    

print(sum//len(a))



# 2 median
a=[2,4,5,7,6,5,9]
i=0
me=0
if len(a) % 2 != 0 :
    me = a[(len(a) - 1) // 2]
else:
    me = (a[len(a) // 2 - 1] + a[len(a) // 2]) // 2

print(me)
