### Unit 13~


### if 조건문

x = 10
if x === 10:
    print('10입니다.')

x = 10
if x == 10:
    pass      # TODO: x가 10일 때 처리가 필요함.

x = 10

if x == 10:
    print('x에 들어있는 숫자는')
        print('10입니다.')    # unexpected indent error

if x == 10:
    print('x에 들어있는 숫자는')
    print('10입니다.')

x = 15

if x >= 10:
    print('10 이상입니다.')

    if x == 15:
        print('15입니다.')

    if x == 20:
        print('20입니다.')

x = 5
if x == 10:
    print('10입니다.')
else:
    print('10이 아닙니다.')

x = int(input())  # 입력받은 값을 변수에 저장

if x == 10:  # x가 10이면
    print('10입니다.')  # '10입니다.'를 출력

if x == 20:  # x가 20이면
    print('20입니다.')  # '20입니다.'를 출력

x = 5
y = x if x == 10 else 0
y

if True:
    print('참')  # True는 참
else:
    print('거짓')

if False:
    print('참')
else:
    print('거짓')  # False는 거짓

if None:
    print('참')
else:
    print('거짓')  # None은 거짓

if 0:
    print('참')
else:
    print('거짓')  # 0은 거짓

if 1:
    print('참')  # 1은 참
else:
    print('거짓')

if 0x1F:  # 16진수
    print('참')  # 0x1F는 참
else:
    print('거짓')

if 0b1000:  # 2진수
    print('참')  # 0b1000은 참
else:
    print('거짓')

if 13.5:  # 실수
    print('참')  # 13.5는 참
else:
    print('거짓')

if 'Hello':  # 문자열
    print('참')  # 문자열은 참
else:
    print('거짓')

if '':  # 빈 문자열
    print('참')
else:
    print('거짓')  # 빈 문자열은 거짓

if '0':
    print('True')
else:
    print('False')

if not 0:
    print('참')  # not 0은 참

if not None:
    print('참')  # None은 참

if not '':
    print('참')  # not 빈 문자열은 참

x = 10
y = 20
if x == 10 and y == 20:
    print('T')
else:
    print('F')

if x > 0 and x < 20:
    print('20보다 작은 양수입니다.')
if 0 < x < 20:
    print('20보다 작은 양수입니다.')

x = 20
if x == 10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')
else:
    print('10도 20도 아닙니다.')



### for 반복문

for i in range(100):
    print('Hello, world!', i)

range(10)
list(range(10)) # 버전2와 버전3의 차이

for i in range(11,20):
    print('Hello, world!',i)

for i in range(0,10,2):
    print('Hello, world!',i)

for i in range(10,0,-1):
    print('Hello, world!',i)

for i in reversed(range(10)):
    print('Hello, world!',i)

count = int(input('반복할 횟수를 입력하세요: '))
for i in range(count):
    print('Hello, world!',i)

a = [10,20,30,40,50] # list
for i in a:
    print(i)

fruits = ('apple','orange','grape') # tuple
for fruit in fruits:
    print(fruit)

lux = {'health':490,'mana':334,'melee':550,'armor':18} # dictionary
for key in lux:
    print(key,'=',lux[key])

for letter in 'Python':
    print(letter,end=' ')

for letter in reversed('Python'):
    print(letter,end=' ')

a.list = [10,20,45,67,83]
for a in a.list:
    print(a)

sum = 0
for i in range(1,101):
    sum += i
print(sum)

factorial = 1
for i in range(1,11):
    factorial *= i
nominator = factorial
factorial = 1
for i in range(1,6):
    factorial *= i
denominator = factorial
nominator/(denominator**2)



### while 구문

import random
random.random()
random.randint(1,6)

import random as rd
i = 0
while i != 3:
    i = rd.randint(1,6)
    print(i)

while True:
    dice = rd.randint(1,6)
    print(dice)
    if dice == 3:
        break

count = 0
while True:
    a = rd.randint(1,6)
    b = rd.randint(1,6)
    print(a,b)
    count += 1
    if a + b >= 10:
        break
print("Process finished with exit code ",count)

for i in range(100):
    if i % 2 == 0:
        continue   # loop의 초기위치로 돌아감.
    print(i,end=' ')

for i in range(1,6):
    for k in range(i):
        print('*',end='')
    print()

for i in range(5):          # 5번 반복. 바깥쪽 루프는 세로 방향
    for j in range(5):      # 5번 반복. 안쪽 루프는 가로 방향
        print('j:', j, sep='', end=' ')    # j값 출력. end에 ' '를 지정하여 줄바꿈 대신 한 칸 띄움
    print('i:', i, '\\n', sep='')    # i값 출력, 개행 문자 모양도 출력
                                     # 가로 방향으로 숫자를 모두 출력한 뒤 다음 줄로 넘어감
                                     # (print는 기본적으로 출력 후 다음 줄로 넘어감)

for i in range(5):
    for k in range(5):
        if k == i:
            print('*',end='')
        else:
            print(' ',end='')
    print()

for i in range(5):
    for j in range(5):
        if j == 4 - i:
            print('*',end='')
        else:
            print(' ',end='')
    print()

for i in reversed(range(5)):
    for k in range(i):
        print(' ',end='')
    print('*')

# bubble sort
aList = list(map(int,input('숫자를 입력하세요>').split()))
def bubble_sort(aList):
    for i in range(0, len(aList) - 1):
        for k in range(i + 1, len(aList)):
            if aList[i] > aList[k]: # 부등호 바뀌면 내림차순
                aList[i], aList[k] = aList[k], aList[i]
    print(aList)
print(bubble_sort(aList))

# FizzBuzz
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
for i in range(1,101): # code golf
    print('Fizz'*(i % 3 == 0) + 'Buzz'*(i % 5 == 0) or i)


### turtle graphics

import turtle as t
t.shape('turtle')
for i in range(5):
    t.forward(100)
    t.right(360/5)

n = 6
t.shape('turtle')
t.color('red')
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.right(360 / n)
t.end_fill()























































