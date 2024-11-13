def index(c):
    if ord(c) == 32: return 0
    else: return ord(c)-64

def initSkip(p):
    M = len(p)
    for i in range(NUM):
        skip[i] = M
    for i in range(M):
        skip[index(p[i])] = M - i - 1

def BM(p, t, k):
    M = len(p)
    N = len(t) - 1  # 텍스트의 마지막 유효 문자 인덱스 (널 문자 제외)
    initSkip(p)  # 나쁜 문자 규칙 테이블 초기화

    i = k + M - 1  # 텍스트에서 패턴 끝부터 시작 (현재 비교 위치)
    j = M - 1      # 패턴의 끝 인덱스

    while i < N:
        # 패턴과 텍스트의 현재 문자가 일치하는 경우
        while j >= 0 and t[i] == p[j]:
            i -= 1
            j -= 1
        
        # 패턴이 완전히 매칭된 경우
        if j < 0:
            return i + 1

        # 불일치 발생 시, 나쁜 문자 규칙에 따라 이동
        i += max(skip[index(t[i])], M - j)
        j = M - 1  # 패턴의 마지막 문자로 인덱스를 다시 설정

    return N 

NUM = 27
skip = [0] * NUM
text = 'STRING STARTING CONSISTING' + '\0'
pattern = 'STING'
M = len(pattern)
N = len(text)
K = 0
while True:
    pos = BM(pattern, text, K)
    K = pos + 1
    if K <= N - M: print('패턴이 나타난 위치 : ', pos)
    else: break
print('스트링 탐색 종료')