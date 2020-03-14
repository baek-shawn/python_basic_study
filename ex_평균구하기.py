# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# 나의 풀이
def solution(arr):
    a=0
    for i in arr:
        a = a + i
        av = a / len(arr)
    answer = av
    return answer
# 다른풀이1
def average(list):                      # 파이썬의 내장 함수인 sum 함수를 이용하면 간단하게 풀 수 있다.
    return (sum(list) / len(list))


# 다른풀이2
def average(list):                      # if 함수를 넣어서 list가 0일때 나눗셈의 오류를 막아준다.
    if len(list) == 0:
            return 0

        return sum(list) / len(list)