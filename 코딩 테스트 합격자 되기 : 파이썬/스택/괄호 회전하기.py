# 올바른 괄호 문자열은 () [] {} 가 정확히 열리고 닫힌 모양이다
# 문자열 S가 주어졌을 때 S를 x만큼 왼쪽으로 회전시킬 수 있을 때 S가 올바른 괄호 문자열이 되게 하는 x의 개수를 구하라


# 문제 상황
# 

# 풀이 전 분석
# 주어진 s를 왼쪽으로 1회 회전 시키는 함수 A를 구현한다.
# 올바른 괄호 문자열인지 확인하는 함수 B를 구현한다
# S의 길이만큼 A를 실행하면서 B가 True가 되는 순간 answer을 1씩 증가시킨다



def rotate(s):
    return s[1:] + s[0]


def is_correct(s):
    stack = []
    for i in range(len(s)):
        if(s[i] == '(' or s[i] == '[' or s[i] == '{'):
            stack.append(s[i])
        else:
            if(len(stack) == 0):
                return False
            if(s[i] == ')' and stack[-1] == '('):
                stack.pop()
            if(s[i] == ']' and stack[-1] == '['):
                stack.pop()
            if(s[i] == '}' and stack[-1] == '{'):
                stack.pop()

    if(len(stack) == 0): return True
    else: return False
            



def solution(s):
    answer = 0
    for i in range(len(s)):
        s = rotate(s)
       
        if(is_correct(s)):
            answer += 1
    

    return answer


# 테스트 케이스
print(solution('[](){}'))
print(solution('}]()[{'))
print(solution('[)(]'))
print(solution('}}}'))
print(solution('[[[[]]]]'))
print(solution('[[[[]]]'))



# solution('[](){}')
# solution('}]()[{')
# solution('[)(]')
# solution('}}}')
# solution('[[[[]]]]')
# solution('[[[[]]]')
# solution('[[[[]]]')