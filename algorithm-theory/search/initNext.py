def init_next(p):
    M = len(p)  # 패턴의 길이
    next = [-1] * M  # next 배열 초기화, next[0]은 -1로 시작
    j = -1  # 접두사 인덱스 초기화

    for i in range(1, M):  # i는 1부터 M-1까지 반복
        # 불일치가 발생할 경우, j를 next[j]로 갱신
        while j >= 0 and p[i] != p[j + 1]:
            j = next[j]

        # 일치하는 경우, j를 증가시키고 next[i]에 저장
        if p[i] == p[j + 1]:
            j += 1
            next[i] = j
        else:
            next[i] = -1  # 일치가 없으면 -1로 초기화

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
    next_array = init_next(pattern)
    print(f"{i}. 패턴 '{pattern}'의 next 배열: {next_array}")