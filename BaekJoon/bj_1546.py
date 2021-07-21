N=int(input())
K = list(map(int,input().split()))
New_Average=sum(K,0)/max(K)/len(K)*100
print(round(New_Average,3))