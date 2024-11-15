# 좌표평면에서 처음으로 걸어본 길의 길이를 구하는 문제

# 풀이전 분석
# 1. 좌표 평면을 만들고 지나간 길의 시작과 끝점을 배열에 저장한다. 
# 2. 배열을 set으로 변환하여 중복을 제거한다.
# 3. set의 길이를 반환한다.

def solution(dirs):
    ans = set()

    visited = []
    x, y = 5, 5

    for d in dirs:
        if(d == 'U'):
            if(y < 10):
                visited.append([x, y, x, y+1])
                visited.append([x, y+1, x, y])
                y += 1

        elif(d == 'D'):
            if(y > 0):
                visited.append([x, y, x, y-1])
                visited.append([x, y-1, x, y])
                y -= 1
        elif(d == 'R'):
            if(x < 10):
                visited.append([x, y, x+1, y])
                visited.append([x+1, y, x, y])
                x += 1
        elif(d == 'L'):
            if(x > 0):
                visited.append([x, y, x-1, y])
                visited.append([x-1, y, x, y])
                x -= 1       

    for i in visited:
        ans.add(tuple(i))

    



    return len(ans)/2


dirs = 'LULLLLLLU'
print(solution(dirs)) # 7
