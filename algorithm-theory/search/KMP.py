def advancedInitNext(p):
    M = len(p)  # 패턴의 길이
    next = [-1] * M  # next 배열 초기화
    j = -1  # 접두사 인덱스 초기화

    for i in range(1, M):
        # 일치가 실패할 경우, j를 next[j]로 갱신하여 돌아감
        while j >= 0 and p[i] != p[j + 1]:
            j = next[j]

        # j ≠ -1 이고 p[i] == p[j+1] 일 경우
        if j != -1 and p[i] == p[j + 1]:
            next[i] = next[j]
        else:
            next[i] = j + 1

        # j를 증가시켜 다음 위치로 이동
        if p[i] == p[j + 1]:
            j += 1

    return next

def KMP(p, t, k):
    M = len(p)  # 패턴의 길이
    N = len(t)  # 텍스트의 길이
    next = advancedInitNext(p)  # 패턴의 next 배열 생성
    i = k  # 텍스트에서의 현재 위치
    j = 0  # 패턴에서의 현재 위치

    # 텍스트 탐색
    while i < N:
        # 패턴의 j번째 문자와 텍스트의 i번째 문자가 일치하지 않으면
        while j >= 0 and t[i] != p[j]:
            j = next[j]  # j를 next[j]로 이동하여 불필요한 비교를 피함

        # 일치하는 경우 i와 j를 각각 증가
        i += 1
        j += 1

        # 패턴이 완전히 일치한 경우
        if j == M:
            return i - M  # 패턴이 시작된 위치 반환

    # 패턴이 발견되지 않은 경우
    return N

next = [0] * 50
text = 'ababababcababababcaabbabababca' + '\0'
pattern = 'abababca'
M = len(pattern)
N = len(text)
K = 0
while True:
    pos = KMP(pattern, text, K)
    K = pos + 1
    if K <= N - M: print('패턴이 나타난 위치 : ', pos)
    else: break
print('스트링 탐색 종료')