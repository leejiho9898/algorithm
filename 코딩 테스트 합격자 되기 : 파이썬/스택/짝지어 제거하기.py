# 짝지어 제거하기
# 알파벳 소문자로 문자열이 주어진다.
# 문자열에서 같은 알파벳이 2개 붙어 있는 것을 짝이라고 하는데, 이 짝이 지어지면 제거한다.
# 이 과정을 계속 반복해서 문자열을 모두 제거할 수 있는지 판단하고, 가능하다면 1을 불가능하다면 0을 출력하시오.


# 풀기 전 분석
# 문자열을 앞에서 부터 검사하여 스택의 첫번째에 넣고, 다음 문자열이 스택의 첫번째와 같다면 스택의 첫번째를 제거한다. 그리고 처음부터 다시 검사한다
# 다르다면 스택에 추가한다


def solution(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    return 1 if not stack else 0

# 테스트 케이스
print(solution('baabaa'))
print(solution('cdcd'))
print(solution('aabbccdd'))
print(solution('aabbccdde'))
print(solution('aabbccddeee'))
print(solution('aabbccddeeee'))
print(solution('aabbccddeeeee'))
print(solution('aabbccddeeeeee'))
