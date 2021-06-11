T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    K= '#' + str(i+1) + ':'
    print('Case',K,A,'+',B,'=',A+B)