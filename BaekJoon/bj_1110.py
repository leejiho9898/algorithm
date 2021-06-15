A = int(input()) #26
B = A #26이 될 수
count = 0 #while 돈 횟수
while True:
    C=B//10         #2 
    D=B%10          #6
    E=C+D           #8
    B=(D*10)+(E%10)      #68
    count+=1
    if A==B: break

print(count)
