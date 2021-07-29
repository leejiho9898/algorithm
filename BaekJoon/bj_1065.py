def isHan(Num) :
    if Num <= 99:
        return True
    else:
        K=[]
        K.extend([Num//100,(Num%100)//10,Num%10])
        if K[0] - K[1] == K[1] - K[2]:
            return True
        else:
            return False

Hansu=0
Num = int(input())
for i in range(1,Num+1):
    if isHan(i)==True:
        Hansu+=1

print(Hansu)
