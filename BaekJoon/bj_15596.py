def notSelfNum(A):
    ans = A + A//1000 + ((A%1000)//100) + ((A%100)//10) + (A%10)
    return ans


    
T=[]
K = set()
for i in range (10000):
    K.add(notSelfNum(i))

for j in range(10000):
    if j not in K:
        print(j)
