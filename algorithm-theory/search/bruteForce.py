def bruteForce(p, t, k):
    M = len(p)  # 패턴의 길이
    N = len(t)  # 텍스트의 길이
    i = k       # i를 K 위치에서 시작
    j = 0       # 패턴 인덱스 초기화

    # 패턴 매칭 루프
    while i < N and j < M:
        if t[i] != p[j]:  # 불일치가 발생했을 때
            i = i - j + 1  # i를 다음 위치로 이동
            j = 0          # j 초기화
        else:  # 일치할 때
            i += 1
            j += 1

    # 패턴이 완전히 일치한 경우
    if j == M:
        return i - M  # 패턴이 시작된 위치 반환
    else:
        return N
    
text = 'ababababcababababcaabbabababca' 
pattern = 'abababca'
M = len(pattern)
N = len(text)
K = 0
while True:
    pos = bruteForce(pattern, text, K)
    K = pos + M
    if K < N: print('패턴이 나타난 위치 : ', pos)
    else: break
print('스트링 탐색 종료')