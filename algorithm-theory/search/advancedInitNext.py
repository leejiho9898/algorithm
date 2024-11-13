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
# 테스트할 문자열 리스트
patterns = [
    "aaaaaaaaa",  # (1)
    "00000001",   # (2)
    "10100111",   # (3)
    "ababca",     # (4)
    "abababca",   # (5)
    "abcabcabc",  # (6)
    "abcabcacab", # (7)
    "abracadabra" # (8)
]

# 각 문자열에 대해 next 배열 출력
for i, pattern in enumerate(patterns, 1):
    next_array = advancedInitNext(pattern)
    print(f"{i}. 패턴 '{pattern}'의 next 배열: {next_array}")