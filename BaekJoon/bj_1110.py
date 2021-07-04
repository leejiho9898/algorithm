# A = int(input()) #26
# B = A #26이 될 수
# count = 0 #while 돈 횟수
# while True:
#     C=B//10         #2 
#     D=B%10          #6
#     E=C+D           #8
#     B=(D*10)+(E%10)      #68
#     count+=1
#     if A==B: break

# print(count)


def solution(A: int, B: int) -> int:
    count = 0
    while True:
        C=B//10         #2 
        D=B%10          #6
        E=C+D           #8
        B=(D*10)+(E%10)      #68
        count+=1
        if A==B: 
            break
    return count


if __name__ == "__main__":
    A = int(input())
    B = A
    print(solution(A, B))