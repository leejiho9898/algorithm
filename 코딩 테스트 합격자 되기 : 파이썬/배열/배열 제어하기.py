# 배열의 중복값 제거하고 내림차순 정렬하기

# 문제 풀기전 분석 
#  1. 배열의 중복값을 제거한다.
#  2. 배열을 내림차순으로 정렬한다.

def solution(arr:list):
    unique_arr = list(set(arr))
    unique_arr.sort(reverse=True)
    return unique_arr

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution([4, 2, 2, 1, 3, 4])) # 반환값 : [4, 3, 2, 1]
print(solution([2, 1, 1, 3, 2, 5, 4])) # 반환값 : [5, 4, 3, 2, 1]


# set의 시간복잡도 = N 보장이므로 내장된거 잘 쓰자