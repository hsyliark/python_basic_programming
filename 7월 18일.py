### Unit 22~


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



