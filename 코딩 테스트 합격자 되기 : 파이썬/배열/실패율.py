# 실패율 = 스테이지에 도달했으나 클리어 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
# 실패율이 동점이면 작은 번호의 스테이지가 먼저 오도록
# N = 전체 스테이지의 개수
# stages = 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열

# 문제 풀기전 분석
# 1.반복문으로 stages를 돌면서 각 스테이지의 실패율을 구한다.
# 2.실패율이 높은 스테이지부터 내림차순으로 정렬한다.
# 3.실패율이 같으면 작은 번호의 스테이지가 먼저 오도록 정렬한다.

# 스테이지 실패율 구하는 방법
# 1. 스테이지보다 높은 플레이어 수를 구한다.
# 2. 스테이지와 같은 플레이어 수를 구해 실패율을 구한다.

def solution(N, stages):
    answer = []

    fails = [0] * (N + 1)
    arrivals = []
    for i in stages:
        fails[i-1] += 1

    # fails의 누적합을 구한다.
    for i in range(N):
        arrivals.append(sum(fails[i:]))
        print(arrivals)
    
    # 실패율을 구한다.

    for i in range(N):
        if arrivals[i] == 0:
            answer.append([i+1, 0])
        else:
            answer.append([i+1, fails[i] / arrivals[i]])

    answer.sort(key=lambda x: (-x[1], x[0]))
    return [x[0] for x in answer] #



        

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages)) # [3,4,2,1,5]