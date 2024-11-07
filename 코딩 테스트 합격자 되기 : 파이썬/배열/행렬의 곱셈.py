# 2차원 행렬 arr1과 arr2를 더한 값을 반환하라

# 행렬의 행과 열이 100 이하이다.
# n^3 이하의 시간복잡도로 풀어야한다.

# 문제 풀기전 분석
# 1. 새 배열을 만든다
# 2. 반복문으로 더한 값을 새 배열에 추가한다.
# 3. 새 배열을 반환한다.


def solution(arr1:list, arr2:list):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[0])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)
        
    return answer

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution([[1,2],[2,3]], [[3,4],[5,6]])) # 반환값 : [[4, 6], [7, 9]]
print(solution([[1],[2]], [[3],[4]])) # 반환값 : [[4], [6]]
print(solution([[1,2,3],[2,3,4]], [[3,4,5],[5,6,7]])) # 반환값 : [[4, 6, 8], [7, 9, 11]]