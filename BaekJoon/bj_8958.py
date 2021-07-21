N=int(input())
for i in range(N):
    point=0
    K = input()
    add_point = 0
    for j in range(len(K)):
        if K[j] == 'O':
            add_point+=1
            point = point + add_point
        else:
            add_point=0
    print(point)
