### Unit 41~47

## cooperative routine

def number_coroutine():
    while True:
        x = (yield) # 코루틴을 계속 유지하기 위해 무한 루프 사용
        print(x) # 코루틴을 계속 유지하기 위해 무한 루프 사용
co = number_coroutine()
next(co) # 코루틴 안의 yield까지 코드 실행(최초 실행)
co.send(1) # 코루틴에 숫자 1을 보냄
co.send(2) # 코루틴에 숫자 2을 보냄
co.send(3) # 코루틴에 숫자 3을 보냄

def sum_coroutine():
    total = 0
    while True:
        x = (yield total) # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        total += x
co = sum_coroutine() # 0: 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력
print(next(co))
print(co.send(1)) # 1: 코루틴에 숫자 1을 보내고 코루틴에서 나온 값 출력
print(co.send(2)) # 3: 코루틴에 숫자 2를 보내고 코루틴에서 나온 값 출력
print(co.send(3)) # 6: 코루틴에 숫자 3을 보내고 코루틴에서 나온 값 출력

def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    except GeneratorExit: # 코루틴이 종료 될 때 GeneratorExit 예외 발생
        print()
        print('코루틴 종료')
co = number_coroutine()
next(co)
for i in range(20):
    co.send(i)
co.close() # 코루틴 종료

def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print(e)
        yield total # 코루틴 바깥으로 값 전달
co = sum_coroutine()
next(co)
for i in range(20):
    co.send(i)
print(co.throw(RuntimeError, '예외로 코루틴 끝내기')) # 190 :  코루틴의 except에서 yield로 전달받은 값

def accumulate():
    total = 0
    while True:
        x = (yield)
        if x is None:
            return total
            # raise StopIteration(total)
        total += x
def sum_coroutine():
    while True:
        total = yield from accumulate()
        print(total)
co = sum_coroutine()
next(co)
for i in range(1, 11):
    co.send(i)
co.send(None)
for i in range(1, 101):
    co.send(i)
co.send(None)

def number_coroutine():
    x = None
    while True:
        x = (yield x)  # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        if x == 3:
            return x
def print_coroutine():
    while True:
        x = yield from number_coroutine()  # 하위 코루틴의 yield에 지정된 값을 다시 바깥으로 전달
        print('print_coroutine:', x)
co = print_coroutine()
next(co)
x = co.send(1)  # number_coroutine으로 1을 보냄
print(x)  # 1: number_coroutine의 yield에서 바깥으로 전달한 값
x = co.send(2)  # number_coroutine으로 2를 보냄
print(x)  # 2: number_coroutine의 yield에서 바깥으로 전달한 값
co.send(3)  # 3을 보내서 반환값을 출력하도록 만듬

def find(word):
    result = False
    while True:
        line = (yield result)
        result = word in line
f = find('Python')
next(f)
print(f.send('Hello, Python!'))
print(f.send('Hello, world!'))
print(f.send('Python Script'))
f.close()


## decorator

def trace(func):  # 호출할 함수를 매개변수로 받음
    def wrapper():  # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
        func()  # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper  # wrapper 함수 반환
def hello():
    print('hello')
def world():
    print('world')
trace_hello = trace(hello)  # 데코레이터에 호출할 함수를 넣음
trace_hello()  # 반환된 함수를 호출
trace_world = trace(world)  # 데코레이터에 호출할 함수를 넣음
trace_world()  # 반환된 함수를 호출

def trace(func):  # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
        func()  # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper  # wrapper 함수 반환
@trace  # @데코레이터
def hello():
    print('hello')
@trace  # @데코레이터
def world():
    print('world')
hello()  # 함수를 그대로 호출
world()  # 함수를 그대로 호출


## regular expression

import re
re.match('Hello', 'Hello, world!')     # 문자열이 있으므로 정규표현식 매치 객체가 반환됨
re.match('Python', 'Hello, world!')    # 문자열이 없으므로 아무것도 반환되지 않음
re.search('^Hello', 'Hello, world!')     # Hello로 시작하므로 패턴에 매칭됨
re.search('world!$', 'Hello, world!')    # world!로 끝나므로 패턴에 매칭됨
re.match('hello|world', 'hello')    # hello 또는 world가 있으므로 패턴에 매칭됨
re.match('[0-9]*', '1234')    # 1234는 0부터 9까지 숫자가 0개 이상 있으므로 패턴에 매칭됨
re.match('[0-9]+', '1234')    # 1234는 0부터 9까지 숫자가 1개 이상 있으므로 패턴에 매칭됨
re.match('[0-9]+', 'abcd')    # abcd는 0부터 9까지 숫자가 1개 이상 없으므로 패턴에 매칭되지 않음
re.match('a*b', 'b')      # b에는 a가 0개 이상 있으므로 패턴에 매칭됨
re.match('a+b', 'b')      # b에는 a가 1개 이상 없으므로 패턴에 매칭되지 않음
re.match('a*b', 'aab')    # aab에는 a가 0개 이상 있으므로 패턴에 매칭됨
re.match('a+b', 'aab')    # aab에는 a가 1개 이상 있으므로 패턴에 매칭됨
re.match('H?', 'H')     # H 뒤에 문자가 0개 또는 1개이므로 패턴에 매칭됨
re.match('H?', 'Hi')    # H 뒤에 문자가 0개 또는 1개이므로 패턴에 매칭됨
re.match('H.', 'Hi')    # H 뒤에 문자가 1개 있으므로 패턴에 매칭됨
re.match('h{3}', 'hhhello')   # h가 3개 있으므로 패턴에 매칭됨
re.match('(hello){3}', 'hellohellohelloworld')   #   hello가 3개 있으므로 패턴에 매칭됨
re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-1000')    # 숫자 3개-4개-4개 패턴에 매칭됨
re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-100')   # 숫자 3개-4개-4개 패턴에 매칭되지 않음
re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-100-1000')    # 2~3개-3~4개-4개 패턴에 매칭됨
re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-10-1000')  # 2~3개-3~4개-4개 패턴에 매칭되지 않음
re.match('[a-zA-Z0-9]+', 'Hello1234')    # a부터 z, A부터 Z, 0부터 9까지 1개 이상 있으므로 패턴에 매칭됨
re.match('[A-Z0-9]+', 'hello')    # 대문자, 숫자는 없고 소문자만 있으므로 패턴에 매칭되지 않음
re.match('[가-힣]+', '홍길동')    # 가부터 힣까지 1개 이상 있으므로 패턴에 매칭됨
re.match('[^A-Z]+', 'Hello')    # 대문자를 제외. 대문자가 있으므로 패턴에 매칭되지 않음
re.match('[^A-Z]+', 'hello')    # 대문자를 제외. 대문자가 없으므로 패턴에 매칭됨
re.search('^[A-Z]+', 'Hello')        # 대문자로 시작하므로 패턴에 매칭됨
re.search('[0-9]+$', 'Hello1234')    # 숫자로 끝나므로 패턴에 매칭됨
re.search('\*+', '1 ** 2')                    # *이 들어있는지 판단
re.match('[$()a-zA-Z0-9]+', '$(document)')    # $, (, )와 문자, 숫자가 들어있는지 판단
re.match('\d+', '1234')          # 모든 숫자이므로 패턴에 매칭됨
re.match('\D+', 'Hello')         # 숫자를 제외한 모든 문자이므로 패턴에 매칭됨
re.match('\w+', 'Hello_1234')    # 영문 대소문자, 숫자, 밑줄 문자이므로 패턴에 매칭됨
re.match('\W+', '(:)')    # 영문 대소문자, 숫자, 밑줄문자를 제외한 모든 문자이므로 패턴에 매칭됨
re.match('[a-zA-Z0-9 ]+', 'Hello 1234')     # ' '로 공백 표현
re.match('[a-zA-Z0-9\s]+', 'Hello 1234')    # \s로 공백 표현

p = re.compile('[0-9]+')    # 정규표현식 패턴을 객체로 만듦
p.match('1234')             # 정규표현식 패턴 객체에서 match 메서드 사용
p.search('hello')           # 정규표현식 패턴 객체에서 search 메서드 사용

m = re.match('([0-9]+) ([0-9]+)', '10 295')
m.group(1)    # 첫 번째 그룹(그룹 1)에 매칭된 문자열을 반환
m.group(2)    # 두 번째 그룹(그룹 2)에 매칭된 문자열을 반환
m.group()     # 매칭된 문자열을 한꺼번에 반환
m.group(0)    # 매칭된 문자열을 한꺼번에 반환
m.groups()    # 각 그룹에 해당하는 문자열을 튜플 형태로 반환

m = re.match('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')
m.group('func')    # 그룹 이름으로 매칭된 문자열 출력
m.group('arg')     # 그룹 이름으로 매칭된 문자열 출력

re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8')

re.match('[a-z]+(.[a-z]+)*$', 'hello.world')    # .world는 문자열이므로 패턴에 매칭됨
re.match('[a-z]+(.[a-z]+)*$', 'hello.1234')     # .1234는 숫자이므로 패턴에 매칭되지 않음
re.match('[a-z]+(.[a-z]+)*$', 'hello')          # .뒤에 문자열이 없어도 패턴에 매칭됨

re.sub('apple|orange', 'fruit', 'apple box orange tree')    # apple 또는 orange를 fruit로 바꿈
re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8')    # 숫자만 찾아서 n으로 바꿈

def multiple10(m):        # 매개변수로 매치 객체를 받음
    n = int(m.group())    # 매칭된 문자열을 가져와서 정수로 변환
    return str(n * 10)    # 숫자에 10을 곱한 뒤 문자열로 변환해서 반환
re.sub('[0-9]+', multiple10, '1 2 Fizz 4 Buzz Fizz 7 8')
re.sub('[0-9]+', lambda m: str(int(m.group()) * 10), '1 2 Fizz 4 Buzz Fizz 7 8')

re.sub('([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1', 'hello 1234')    # 그룹 2, 1, 2, 1 순으로 바꿈
re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', '<\\2>\\3</\\2>', '{ "name": "james" }')
re.sub('({\s*)"(?P<key>\w+)":\s*"(?P<value>\w+)"(\s*})', '<\\g<key>>\\g<value></\\g<key>>', '{ "name": "james" }')


## module, package

import math
math.pi
math.sqrt(4)

import math as m
m.pi
m.sqrt(2)

from math import pi
pi

from math import sqrt
sqrt(4)

from math import pi, sqrt
pi
sqrt(2)

from math import *
from math import sqrt as s
from math import pi as p, sqrt as s

import urllib.request as r # crawling
response = r.urlopen('http://www.google.co.kr')
response.status # 200 -> OK

from urllib.request import Request, urlopen    # urlopen 함수, Request 클래스를 가져옴
req = Request('http://www.google.co.kr')       # Request 클래스를 사용하여 req 생성
response = urlopen(req)                        # urlopen 함수 사용
response.status

from urllib.request import *     # urllib의 request 모듈에서 모든 변수, 함수, 클래스를 가져옴
req = Request('http://www.google.co.kr')    # Request를 사용하여 req 생성
response = urlopen(req)                     # urlopen 함수 사용
response.status

from urllib.request import Request as r, urlopen as u
req = r('http://www.google.co.kr')    # r로 Request 클래스 사용
response = u(req)                     # u로 urlopen 함수 사용
response.status


## 10진수, 2진수

bin(13)    # 10진수 13을 2진수로 변환
0b1101     # 2진수 1101을 10진수로 변환
int('1101', 2)    # 2진수로 된 문자열 1101을 10진수로 변환

bin(0b1101 & 0b1001)    # 비트 AND
13 & 9                  # 비트 AND
bin(0b1101 | 0b1001)    # 비트 OR
13 | 9                  # 비트 OR
bin(0b1101 ^ 0b1001)    # 비트 XOR
13 ^ 9                  # 비트 XOR
bin(~0b1101)            # 비트 NOT
~13                     # 비트 NOT


## time

import time
time.time()
time.localtime(time.time())
time.strftime('%Y-%m-%d', time.localtime(time.time()))
time.strftime('%c', time.localtime(time.time()))

import datetime as dt
dt.datetime.today()
import pytz
dt.datetime.now(pytz.timezone('UTC'))

d = dt.datetime(2018, 5, 19)
d
d = dt.datetime.strptime('2018-05-19', '%Y-%m-%d')
d
d.strftime('%Y-%m-%d')
d.strftime('%c')
today = dt.datetime.today()
today.year, today.month, today.day, today.hour, today.minute, today.second, today.microsecond

from datetime import datetime, timedelta
d = datetime(2018, 5, 13)
d - timedelta(days=20)
datetime(2018, 5, 13) - datetime(2018, 4, 1)


## 두 실수값의 차이

0.1 + 0.2 == 0.3 # False

import math, sys
x = 0.1 + 0.2
math.fabs(x - 0.3) <= sys.float_info.epsilon # 시스템상의 허용오차
math.isclose(0.1 + 0.2, 0.3)
