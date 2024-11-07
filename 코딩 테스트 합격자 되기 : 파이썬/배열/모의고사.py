#  수포자가 문제를 다 찍습니다
#  1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
#  2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
#  3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 정답 배열 answer이 주어졌을 때 가장 많이 맞춘사람을 배열에 담아 반환하라
# 시험문제는 10,000문제 이하이다.
# 문제의 정답은 1, 2, 3, 4, 5 중 하나이다.
# 여럿이라면 오름차순으로 정렬한다.

# 문제 풀기전 분석
# 1. 수포자들의 찍는 패턴을 분석해서 배열로 저장한다
# 2. 반복문으로 답을 비교해서 변수에 계속 더함
# 3. 가장 많이 맞춘 사람을 찾는다.
# 4. 오름차순으로 정렬한다.

# 숫자 배열
def solution(answer:list):
    supoja1 = [1,2,3,4,5]
    supoja2 = [2,1,2,3,2,4,2,5]
    supoja3 = [3,3,1,1,2,2,4,4,5,5]

    scores = [0,0,0] 


    while len(supoja1) != len(answer):
        supoja1 += supoja1
        if(len(supoja1) > len(answer)):
            supoja1 = supoja1[:len(answer)]

    while len(supoja2) != len(answer):
        supoja2 += supoja2
        if(len(supoja2) > len(answer)):
            supoja2 = supoja2[:len(answer)]
    
    while len(supoja3) != len(answer):
        supoja3 += supoja3
        if(len(supoja3) > len(answer)):
            supoja3 = supoja3[:len(answer)]

    
        

    for i in range(len(answer)):
        if supoja1[i] == answer[i]:
            scores[0] += 1
        if supoja2[i] == answer[i]:
            scores[1] += 1
        if supoja3[i] == answer[i]:
            scores[2] += 1

    max_score = max(scores)
    
    answer = []

    for index, score in enumerate(scores):
        if(score == max_score):
            answer.append(index+1)

    return answer


print(solution([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]))
