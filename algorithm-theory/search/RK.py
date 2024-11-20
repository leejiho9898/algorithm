def index(c):
    if ord(c) == 32: return 0
    else: return ord(c)-64

def RK(p, t, k):
    dM = 1      
    h1 = 0      
    h2 = 0      
    M = len(p)  
    N = len(t)  

    
    for i in range(1, M):
        dM = (d * dM) % q

    
    for i in range(M):
        h1 = (h1 * d + index(p[i])) % q

    
    for i in range(k, k + M):
        h2 = (h2 * d + index(t[i])) % q

    i = k
    while h1 != h2:
        
        if i + M >= N:
            return N

        h2 = (h2 + d * q - index(t[i]) * dM) % q
        h2 = (h2 * d + index(t[i + M])) % q
        i += 1
        if i > N - M:
            return N
    return i


    



q = 33554393
d = 32
text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION' + '\0'
pattern = 'ATION'
M = len(pattern)
N = len(text)
K = 0
while True:
    pos = RK(pattern, text, K)
    K = pos + 1
    if K <= N - M: print('패턴이 나타난 위치 : ', pos)
    else: break
print('스트링 탐색 종료')