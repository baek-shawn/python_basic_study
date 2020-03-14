def solution(L, x):
    a=0
    while a<len(L):
        L.insert(a+1,x)
    return L
fire = solution([1,5,7,9,13],10)
print(fire)
