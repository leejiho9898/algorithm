# 정수 배열이 주어지면 두 수를 뽑아 더해서 만들 수 있는 모든 수를 오름차순으로 반환하라

# 문제 풀기 전 분석
# 1. 반복문으로 모든 수를 뽑아서 만든다 -> 시간복잡도 n^2
# 2. set을 사용해서 중복값을 제거한다.
# 3. sort로 정렬한다.

def solution(arr:list):
    added_arr = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            
            added_arr.append(arr[i] + arr[j])
    answer = sorted(list(set(added_arr)))
    return answer

# #TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution([2, 1, 3, 4, 1])) # 반환값 : [2, 3, 4, 5, 6, 7]
print(solution([5, 0, 2, 7])) # 반환값 : [2, 5, 7, 9, 12]

# arr.sort() 와 sorted(arr)의 차이점 : arr.sort()는 arr 원본을 정렬하고, sorted(arr)는 정렬된 새로운 리스트를 반환한다.