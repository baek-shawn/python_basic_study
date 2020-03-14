# Q : 입력으로 주어지는 리스트 x 의 첫 원소와 마지막 원소의 합을 리턴하는 함수 solution() 을 완성하세요.
#나의 풀이
def solution(x):
    answer = x[0] + x[-1]
    return answer
#다른풀이 1.
def solution(x):
    answer = x[0] + x[len(n)-1]
    return answer

#출처: https://programmers.co.kr/learn/courses/57 (프로그래머스 :어서와! 자료구조와 알고리즘은 처음이지? 강의 연습문제1번)


