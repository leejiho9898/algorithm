# 문제: 괄호 짝 맞추기

# 소괄호가 정상으올 열고 닫히는지 확인하는 함수를 작성하시오
# 열린 괄호는 가장 가까운 닫힌 괄호와 짝을 이룬다
# 열린 괄호가 먼저 와야한다.

# 스택을 이용하여 열린 괄호를 저장하고 닫힌괄호가 나오면 pop 하여 스택이 비는지 확인

def solution(value):
    stack = []
    for i in value:
        if(i == '('):
            stack.append(i)
        if(i ==")"):
            if(len(stack)==0):
                return False
            stack.pop()
    if(len(stack)==0):
        return True
    else:
        return False
    


print(solution("()()")) # True
print(solution("(())")) # True
print(solution("(()))")) # False
print(solution("(()()")) # False
print(solution(")(")) # False
print(solution("((()))")) # True
print(solution("((())")) # False
print(solution("(()))")) # False
print(solution("((()")) # False
print(solution("()()")) # True
