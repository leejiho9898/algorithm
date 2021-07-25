C= int(input())
for i in range(C):
    K =list(map(int,input().split()))
    Average = (sum(K[1:]))/(K[0])
    overAverage = 0
    for score in K[1:]:
        if score > Average:
            overAverage += 1
    Answer = overAverage/K[0]*100
    print(f'{Answer:.3f}%') 
