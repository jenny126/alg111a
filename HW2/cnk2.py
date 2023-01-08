import random
from re import A

def table(n,k):
    ans=[]
    m=k
    while k>m:
        c=rand(ans,n,k,m)
        print(c)
        ans=c['ans']
        k=c['k']
    print(ans)

def rand(ans,n,k,m):    
    for _ in range(1,m+1):
        save=random.randrange(1,n+1)
        if save in ans:
            k=k+1
            #return
        else:
            k=k-1
            ans.append(save)
        #print(ans)
    return {'ans':ans,'k':k}

#table(10,1)
table(10,9)