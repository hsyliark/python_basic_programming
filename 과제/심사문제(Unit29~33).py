## Unit 29
# 표준 입력으로 숫자 두 개가 입력됩니다.
# 다음 소스 코드를 완성하여 두 숫자의 덧셈, 뺄셈, 곱셈, 나눗셈의 결과가 출력되게 만드세요.
# 이때 나눗셈의 결과는 실수라야 합니다.

x, y = map(int, input().split())
def calc(x, y):
    return x + y, x - y, x * y, float(x / y)
a, s, m, d = calc(x, y)
print('덧셈 : {0}, 뺄셈 : {1}, 곱셈 : {2}, 나눗셈 : {3}'.format(a, s, m, d))



## Unit 30
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
# 다음 소스 코드를 완성하여 가장 높은 점수, 가장 낮은 점수,
# 평균 점수가 출력되게 만드세요. 평균 점수는 실수로 출력되어야 합니다.

korean, english, mathematics, science = map(int, input().split())

import numpy as np
set_score = dict(zip(['korean','english','mathematics','science'],
                     [korean,english,mathematics,science]))
def get_min_max_score(*score):
    minScore = min(score)
    maxScore = max(score)
    return minScore, maxScore
def get_average(**set_score):
    score = []
    for kw, arg in set_score.items():
        score.append(arg)
    avgScore = np.mean(score)
    return avgScore

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))



## Unit 31
# 표준 입력으로 정수 한 개가 입력됩니다(입력 값의 범위는 10~30).
# 다음 소스 코드를 완성하여 입력된 정수에 해당하는 피보나치 수가 출력되게 만드세요.
# 피보나치 수는 0과 1로 시작하며, 다음 번 피보나치 수는 바로 앞의 두 피보나치 수의 합입니다.

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    count = 1
    prog = [0,1]
    for i in range(2,n+1):
        prog.append(prog[i-2]+prog[i-1])
        count += 1
    return prog[n]
n = int(input())
print(fib(n))



## Unit 32
# 표준 입력으로 숫자.확장자 형식으로 된 파일 이름 여러 개가 입력됩니다.
# 다음 소스 코드를 완성하여 파일 이름이 숫자 3개이면서 앞에 0이 들어가는 형식으로 출력되게 만드세요.
# 예를 들어 1.png는 001.png, 99.docx는 099.docx, 100.xlsx는 100.xlsx처럼 출력되어야 합니다.
# 그리고 람다 표현식을 사용해야 하며 출력 결과는 리스트 형태라야 합니다.
# 람다 표현식에서 파일명을 처리할 때는 문자열 포매팅과 문자열 메서드를 활용하세요.

files = input().split()
print(list(map(lambda x: '%03d.' % int((x.split('.')[0])) + x.split('.')[1], files)))



## Unit 33
# 표준 입력으로 정수가 입력됩니다.
# 다음 소스 코드를 완성하여 함수 c를 호출할 때마다 숫자가 1씩 줄어들게 만드세요.
# 여기서는 함수를 클로저로 만들어야 합니다.
# 정답에 코드를 작성할 때는 def countdown(n):에 맞춰서 들여쓰기를 해주세요.

def countdown(n):
    i = n + 1
    def discount():
        nonlocal i
        i -= 1
        return i
    return discount

n = int(input())
c = countdown(n)
for i in range(n):
    print(c(), end=' ')





    



