K=[]
for i in range(10):
    K.append(int(input())%42)
K = set(K)
print(len(K))