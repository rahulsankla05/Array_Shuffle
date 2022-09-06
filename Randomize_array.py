# To reshuffle an array//
import random 
a=[1,3,5,67,87,90]
n=len(a)
for i in range(n-1,0,-1):
    j=random.randint(0,i)
    a[i],a[j]=a[j],a[i]
print(a)

