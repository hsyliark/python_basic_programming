## Unit 22


# 다음 소스 코드를 완성하여 리스트 a에 들어있는 문자열 중에서
# 길이가 5인 것들만 리스트 형태로 출력되게 만드세요(리스트 표현식 사용).

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo',
     'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]
b


# 표준 입력으로 정수 두 개가 입력됩니다
# (첫 번째 입력 값의 범위는 1~20, 두 번째 입력 값의 범위는 10~30이며
# 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다).
# 첫 번째 정수부터 두 번째 정수까지를 지수로 하는 2의 거듭제곱 리스트를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).
# 단, 리스트의 두 번째 요소와 뒤에서 두 번째 요소는 삭제한 뒤 출력하세요.
# 출력 결과는 리스트 형태라야 합니다.

start, stop = map(int,input().split())
test_list = []
for i in range(start,stop+1):
    test_list.append(2**i)
print(test_list)



## Unit 23


# 다음 소스 코드를 완성하여 높이 2, 세로 크기 4, 가로 크기 3인 3차원 리스트를 만드세요(리스트 표현식 사용).

[[[0 for col in range(3)] for row in range(4)] for depth in range(2)]


# 표준 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고 그 다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다.
# 이때 2차원 리스트 안에서 *는 지뢰이고 .은 지뢰가 아닙니다.
# 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).
# 여러 줄을 입력 받으려면 다음과 같이 for 반복문에서 input을 호출한 뒤 append로 각 줄을 추가하면 됩니다
# (list 안에 문자열을 넣으면 문자열이 문자 리스트로 변환됩니다).
# matrix = []
# for i in range(row):
#     matrix.append(list(input()))

# col, row = map(int,input('가로, 세로 입력>').split())
# matrix = []
# for i in range(row):
#     matrix.append(list(input()))

import numpy as np
col, row = 3, 3
matrix = [['.','*','.'],
          ['.','*','*'],
          ['*','*','.']]
answer = [[np.nan for i in range(col)] for k in range(row)]
for i in range(col):
    for k in range(row):
        if matrix[i][k] == '.':
            if 0 <= i-1 <= col-1 and 0 <= k-1 <= row-1:
                side1 = matrix[i-1][k-1]
            else:
                side1 = ''
            if 0 <= i-1 <= col-1 and 0 <= k <= row-1:
                side2 = matrix[i-1][k]
            else:
                side2 = ''
            if 0 <= i-1 <= col-1 and 0 <= k+1 <= row-1:
                side3 = matrix[i-1][k+1]
            else:
                side3 = ''
            if 0 <= i <= col-1 and 0 <= k-1 <= row-1:
                side4 = matrix[i][k-1]
            else:
                side4 = ''
            if 0 <= i <= col-1 and 0 <= k+1 <= row-1:
                side5 = matrix[i][k+1]
            else:
                side5 = ''
            if 0 <= i+1 <= col-1 and 0 <= k-1 <= row-1:
                side6 = matrix[i+1][k-1]
            else:
                side6 = ''
            if 0 <= i+1 <= col-1 and 0 <= k <= row-1:
                side7 = matrix[i+1][k]
            else:
                side7 = ''
            if 0 <= i+1 <= col-1 and 0 <= k+1 <= row-1:
                side8 = matrix[i+1][k+1]
            else:
                side8 = ''
            side = ''.join([side1,side2,side3,side4,
                            side5,side6,side7,side8])
            answer[i][k] = side.count('*')
        else:
            answer[i][k] = '*'
from pprint import pprint
pprint(answer,indent=6,width=20)



## Unit 24


# 다음 소스 코드를 완성하여 파일 경로에서 파일명만 출력되게 만드세요.
# 단, 경로에서 폴더의 깊이가 달라지더라도 파일명만 출력할 수 있어야 합니다.

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
# Case 1
x = path.split('\\')
filename = x[-1]
# Case 2
x = path.split('\\')
x.reverse()
filename = x[0]
# Case 3
filename = path[path.rfind('\\') + 1:]


# 표준 입력으로 문자열이 입력됩니다.
# 입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).
# 단, 모든 문자가 소문자인 'the'만 찾으면 되며 'them', 'there', 'their' 등은 포함하지 않아야 합니다.

read = '''the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, 
whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. 
That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. 
I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. 
Grown-ups never understand anything by themselves, 
and it is tiresome for children to be always and forever explaining things to the.'''
import string
x = read.strip(string.punctuation).split(' ')
for i in range(len(x)):
    x[i] = x[i].strip(',.').strip('\n').strip("'")
x.count('the')


# 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
# 입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
# 이때 가격은 길이를 9로 만든 뒤 오른쪽으로 정렬하고 천단위로 ,(콤마)를 넣으세요.

price = '51900;83000;158000;367500;250000;59200;128500;1304000'
def my_price(price):
    price_1 = list(map(int, price.split(';')))
    for i in range(0, len(price_1) - 1):
        for k in range(i + 1, len(price_1)):
            if price_1[i] < price_1[k]:
                price_1[i], price_1[k] = price_1[k], price_1[i]
    for j in range(len(price_1)):
        print('{0:>9,}'.format(price_1[j]))
my_price(price)



