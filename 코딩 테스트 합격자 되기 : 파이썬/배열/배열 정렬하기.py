# 정수 배열의 길이는 2 이상 10^5 이하이다.
# 정수 배열의 각 데이터값은 -100,000 이상 100,000 이하이다.

# 문제 풀기전 분석
# 배열의 길이가 10^5 까지이므로 n^2의 시간복잡도로 풀면 시간초과가 발생한다.
# 따라서 nlogn의 시간복잡도를 가지는 정렬을 사용해야한다.

def solution(arr:list):
   arr.sort()
   return arr

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution([1,-5,2,4,3])) # 반환값 : [-5, 1, 2, 3, 4]
print(solution([2,1,1,3,2,5,4])) # 반환값 : [1, 1, 2, 2, 3, 4, 5]
print(solution([1,6,7])) # 반환값 : [1, 6, 7]
