from operator import index
import random

def table(n,k):
    ans=[]
    k=re(ans,n,k)
    print(k)
    while k!=0:
        k=re(ans,n,k)
        return k
    print(ans)

def re(ans,n,k):
    for _ in range(1,k+1):
        save=random.randrange(1,n+1)
        if save not in ans:
            ans.append(save)
            k=k-1
        else:
            #print(j)
            k=k+1
    print(k)
    return k


table(10,9)
table(10,1)


