### Unit 22~24


## list, tuple

a = [10,20,30]
a.append(500)
a
len(a)

a = []
a.append(10)
a

a = [10,20,30]
a.append([500,600])
a
len(a) # 리스트를 한 요소로 보고 추가함.

# 약수
divisor = []
n = 60
for i in range(1,n+1):
    if n % i == 0:
        divisor.append(i)
divisor

a = [10,20,30]
a.extend([500,600])
a
len(a)

a = [10,20,30]
a.insert(2,500)
a
len(a)

a = [10, 20, 30]
a.insert(0, 500) # 맨 처음에 요소 추가
a

a = [10, 20, 30]
a.insert(len(a), 500) # 맨 끝에 요소 추가
a

a = [10,20,30]
a.insert(1,[500,600])
a

a = [10,20,30]
a[1:1] = [500,600]
a
a.pop() # 맨 끝의 요소 삭제
a.pop(0)

a = [10,20,30]
a.remove(20) # 특정값을 찾아서 삭제
del a[0]

# stack : Last in First out
# queue : First in First out
from collections import deque    # collections 모듈에서 deque를 가져옴
a = deque([10, 20, 30])
a
deque([10, 20, 30])
a.append(500)    # 덱의 오른쪽에 500 추가
a
deque([10, 20, 30, 500])
a.popleft()     # 덱의 왼쪽 요소 하나 삭제
10
a
deque([20, 30, 500])

a = [10,20,30,40,50,60]
a.index(20)

a = [10,20,20,30]
a.index(20)
a.count(20)
if 21 in a:
    a.index(21)

a = [10, 20, 30, 15, 20, 40]
a.reverse()
a

a = [10, 20, 30, 15, 20, 40]
a.sort() # a.sort(reverse=False) # 오름차순
a
a.sort(reverse=False) # 내림차순

a = [10, 20, 30, 15, 20, 40]
a.sort()    # a의 내용을 변경하여 정렬
a
[10, 15, 20, 20, 30, 40]
b = [10, 20, 30, 15, 20, 40]
sorted(b)    # 정렬된 새 리스트를 생성

a = [10,20,30]
a.clear() # del a[:]

a = [10,20,30]
a[len(a):] = [500]
a

if not len(seq):    # 리스트가 비어 있으면 True
if len(seq):        # 리스트에 요소가 있으면 True

if not seq:  # 리스트가 비어 있으면 True
if seq:  # 리스트에 내용이 있으면 True

seq = [10, 20, 30]
seq[-1]

seq = []
if seq:               # 리스트에 요소가 있는지 확인
    print(seq[-1])    # 요소가 있을 때만 마지막 요소를 가져옴


## list 할당, 복사

a = [0]*5
b = a
b[2] = 99
b
a # a까지 변화

a = [0]*5
b = a.copy()
a is b # False : 서로 다른 객체
a == b # True : 서로 같은 요소
b[2] = 99
a
b

a = [38,21,53,62,19]
for i in a:
    print(i)
for index, value in enumerate(a):
    print(index, value)
for index, value in enumerate(a):
    print(index+1, value)
for index, value in enumerate(a, start=1):
    print(index, value)


## max, min

a = [38,21,53,62,19]
min(a)
max(a)
sum(a)


## 표현식

a = [i in for i in range(10)]
a
b = list(i for i in range(10))
b
c = [i+5 in for i in range(10)]
c
d = [i*2 in for i in range(10)]
d

a = [i for i in range(10) if i % 2 == 0]
a
b = [i+5 for i in range(10) if i % 2 == 1]
b

a = [i*k for k in range(2,10) for i in range(1,10)]
a

a = [i**2 for i in range(0,11) if i % 2 == 1]
a


## map

a = [1.2, 2.5, 3.7, 4.6]
# for i in range(len(a)):
#     a[i] = int(a[i])
# a
a = list(map(int,a))
a

a = list(map(str,range(10)))
a

# input().split() : 문자(str)형태로 데이터 불러들임
a = map(int,input().split())
a
list(a)


## 2차원 list

a = [[10,20],[30,40],[50,60]]
a
a = [[10,20],
     [30,40],
     [50,60]]
a
# 2차원 리스트의 사각형 구조를 유지하도록 출력
from pprint import pprint
pprint(a, indent=4, width=20)

a = [[10,20],
     [30,40],
     [50,60]]
a[0][0]
a[1][1]
a[2][1]
a[0][1] = 1000

# jagged list
a = [[10, 20],
     [500, 600, 700],
     [9],
     [30, 40],
     [8],
     [800, 900, 1000]]
a

a = [[10,20],
     [30,40],
     [50,60]]
for x in a:
    print(x)
for x, y in a:
    print(x, y)
for i in a:
    for k in i:
        print(k, end=' ')
    print()
for i in range(len(a)):            # 세로 크기
    for k in range(len(a[i])):     # 가로 크기
        print(a[i][k], end=' ')
    print()


## 반복문 list

a = []
for i in range(3):
    line = []
    for k in range(2):
        line.append(0)
    a.append(line)
print(a)

a = [[0 for k in range(2)] for i in range(3)]
a
a = [[0]*2 for i in range(3)]
a

a = [3, 1, 3, 2, 5]  # 가로 크기를 저장한 리스트
b = []  # 빈 리스트 생성
for i in a:  # 가로 크기를 저장한 리스트로 반복
    line = []  # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(i):  # 리스트 a에 저장된 가로 크기만큼 반복
        line.append(0)
    b.append(line)  # 리스트 b에 안쪽 리스트를 추가
print(b)
a = [[0]*i for i in [3,1,3,2,5]]
a

students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]
print(sorted(students, key=lambda student: student[1]))  # 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(sorted(students, key=lambda student: student[2]))  # 안쪽 리스트의 인덱스 2를 기준으로 정렬

a = [[10,20],[30,40]]
b = a
b[0][0] = 500
a
b

a = [[10,20],[30,40]]
b = a.copy()
b[0][0] = 500
a
b

a = [[10,20],[30,40]]
import copy
b = copy.deepcopy(a)
b[0][0] = 500
a
b

f = ['apple', 'pear', 'grape', 'pineapple', 'orange']
g = []
for item in f:
    g.append(item.upper())
g


## 문자열

'Hello, world!'.replace('world', 'Python')
s = 'Hello, world!'
s = s.replace('world!', 'Python')
s

table = str.maketrans('aeiou','12345')
'apple'.translate(table)

'apple pear grape pineapple orange'.split()
'apple, pear, grape, pineapple, orange'.split(', ')
' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
'-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])

'python'.upper()
'PYTHON'.lower()

'   Python   '.lstrip() # 왼쪽 공백 삭제
'   Python   '.rstrip() # 오른쪽 공백 삭제
'   Python   '.strip() # 양쪽 공백 삭제

', python.'.lstrip(',.') # 왼쪽의 특정문자 삭제
', python.'.rstrip(',.') # 오른쪽의 특정문자 삭제
', python.'.strip(',.') # 양쪽의 특정문자 삭제

# 구두점 삭제
import string
', python. '.strip(string.punctuation)
', python.'.strip(string.punctuation + ' ')
', python.'.strip(string.punctuation).strip()
string.punctuation

'python'.ljust(10) # 왼쪽 정렬 (길이 10)
'python'.rjust(10) # 오른쪽 정렬 (길이 10)
'python'.center(10) # 가운데 정렬 (길이 10)

'python'.rjust(10).upper()

'35'.zfill(4)        # 숫자 앞에 0을 채움
'3.5'.zfill(6)       # 숫자 앞에 0을 채움
'hello'.zfill(10)    # 문자열 앞에 0을 채울 수도 있음

'apple pineapple'.find('pl')
'apple pineapple'.find('xy')
'apple pineapple'.rfind('pl')
'apple pineapple'.rfind('xy')
'apple pineapple'.index('pl')
'apple pineapple'.rindex('pl')
'apple pineapple'.count('pl')


## string formatting

'I am %s.' % 'James' # %s : 문자열 (string)
'I am %d years old.' % 20 # %d : 숫자 (decimal integer)

'%f' % 2.3 # %f : 소수점으로 된 실수 포함 (6자리) (fixed point)
# '%.자릿수f' % 숫자
'%.2f' % 2.3
'%.3f' % 2.3
# %길이s (오른쪽 정렬)
'%10s' % 'python'
# %길이d (오른쪽 정렬)
'%10d' % 150
'%10d' % 15000
# %길이.자릿수f (오른쪽 정렬)
'%10.2f' % 2.3
'%10.2f' % 2000.3
# %-길이s (왼쪽 정렬)
'%-10s' % 'python'

# '%d %s' % (숫자, '문자열')
'Today is %d %s.' % (3, 'April')

# '{인덱스}'.format(값)
'Hello, {0}'.format('world!')
'Hello, {0}'.format(100)
'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)
'{0} {0} {1} {1}'.format('Python', 'Script')
'Hello, {} {} {}'.format('Python', 'Script', 3.6)
'Hello, {language} {version}'.format(language='Python', version=3.6)
language = 'Python'
version = 3.6
f'Hello, {language} {version}' # f:formatting

# 중괄호 출력
'{{ {0} }}'.format('Python')

# '{인덱스:<길이}'.format(값)
'{0:<10}'.format('python')
'{0:>10}'.format('python')
'{:>10}'.format('python')





















