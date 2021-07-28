import sys
A,B,V=map(int, sys.stdin.readline().split())

height = 0
day = 0

while True:
    day+=1
    height+=A
    if V > height:
        height-=B
    else:
        break
    
print(day)