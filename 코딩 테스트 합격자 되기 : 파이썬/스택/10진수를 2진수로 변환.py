# 10진수를 2진수로 변환 하는 함수를 만드시오
# 제약조건 없음. 시간복잡도 신경 안써도 됨

# 풀기 전 분석
# 1. 주어진 10진수를 2로 계속 나누고, 나머지를 저장한다
# 2. 나온 나머지를 역순으로 출력한다
# 3. 스택을 사용해도 되고 배열을 사용해도 될거 같은데 그래도 스택단원이니 스택을 사용해보자


def solution(n):
    if(n == 0):
        return '0'
    decimal = n
    stack = []
    while decimal > 1:
        stack.append(decimal % 2)
        decimal = decimal // 2
    if(decimal == 1):
        stack.append(decimal)
    
    answer = ''

    while stack:
        answer += str(stack.pop())
    return answer



# 테스트 케이스
# 27
# 10
# 300
# 200000
# 1
# 0
# 999999

print(solution(27))
print(solution(10))
print(solution(300))
print(solution(200000))
print(solution(1))
print(solution(0))
print(solution(999999))
