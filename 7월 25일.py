### Unit 38~39

## exception

def ten_div(x):
    return 10 / x
ten_div(2)
ten_div(0) # error

try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except:
    print('예외가 발생했습니다.')

y = [10,20,30]
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError as e: # e에 저장된 에러 메세지 출력
    print('숫자를 0으로 나눌 수 없습니다.', e)
except IndexError as e:
    print('잘못된 인덱스입니다.', e)
except Exception as e:
    print('예외가 발생했습니다.', e)

try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')
else:
    print(y)
finally: # 예외 발생 여부와 상관없이 항상 실행됨
    print('코드 실행이 끝났습니다.')

try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:
        raise Exception('3의 배수가 아닙니다.') # x가 3의 배수가 아니면 예외를 발생시킴
    print(x)
except Exception as e:
    print('예외가 발생했습니다.', e)

def three_multiple():
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:
        raise Exception('3의 배수가 아닙니다.')
    print(x)
try:
    three_multiple()
except Exception as e:
    print('예외가 발생했습니다.', e)
three_multiple() # error

def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    except Exception as e: # 함수 안에서 예외를 처리함
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김
try:
    three_multiple()
except Exception as e: # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('스크립트 파일에서 예외가 발생했습니다.', e)

x = int(input('3의 배수를 입력하세요: '))
assert x % 3 == 0, '3의 배수가 아닙니다.' # 3의 배수가 아니면 예외 발생
print(x) # 3의 배수이면 그냥 넘어감

# 예외 만들기
class NotThreeMultipleError(Exception): # Exception을 상속받아서 새로운 예외를 만듬
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')
def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:
            raise NotThreeMultipleError
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)
three_multiple()


## iterator

dir([1,2,3])
it = [1,2,3].__iter__()
it.__next__()

class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration
for i in Counter(3):
    print(i, end=' ')
a, b, c, d, e = Counter(5)
print(a, b, c, d, e)

class Counter:
    def __init__(self, stop):
        self.stop = stop
    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError
print(Counter(3)[0], Counter(3)[1], Counter(3)[2])
for i in Counter(3):
    print(i, end=' ')

import random
it = iter(lambda : random.randint(0, 5), 2)
next(it)
for i in iter(lambda : random.randint(0, 5), 2):
    print(i, end=' ')
while True:
    i = random.randint(0, 5)
    if i == 2:
        break
    print(i, end=' ')

it = iter(range(3))
next(it, 10)



