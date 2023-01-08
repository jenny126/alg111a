def CNK(nA, k):
    chooses = []
    n=len(nA)
    #print("a",chooses,"a")
    c(nA, n, k, chooses)
    


def c(nA, n, k, chooses, m):
    if len(chooses) == m:
        #print("b",chooses,"b")
        print(chooses)
        return
    elif n <= 0: 
        #print("n",n,"n") 
        return
    else:
        c(nA, n-1, k, chooses, m)
        #print("app",n,nA[n-1])
        chooses.append(nA[n-1])
        c(nA, n-1, k-1, chooses, m)
        #print("c",chooses[-1],chooses,"c")
        del chooses[-1]

CNK([1,2,3,4,5], 3)