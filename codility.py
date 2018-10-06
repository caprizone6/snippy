import string

N = 4

def solution(N):
    cols = ("A", "B", "C", "D")
    for i in range(N):
        pos = `i+1` + cols[i]
        print pos
        pass

solution(N)