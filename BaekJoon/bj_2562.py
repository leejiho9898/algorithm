K = []
for i in range (9):
    a=int(input())
    K.append(a)
# for i in range(9):
#     if(K[i]==max(K)):
#         print(K[i],i+1,sep="\n")
print(max(K),(K.index(max(K))+1),sep="\n")