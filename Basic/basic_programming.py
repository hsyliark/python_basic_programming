# -*- coding: utf-8 -*-
"""
Python basic programming
site : http://pythonstudy.xyz/

"""

a = 1
b = 2
c = a + b

print(c)

x = 1

if x > 0 :
    a = 1
    b = 2
    c = a + b
else :
    a = -1
    b = -2
    c = a - b
    
print(c)    


import math
n = math.sqrt(9.0)
print(n)

# https://www.python.org/dev/peps/
# https://www.python.org/dev/peps/pep-0008

int(3.5) # 3
2e3 # 2000.0
float("1.6") # 1.6
float("inf") # 무한대
bool(0) # False. 숫자에서 0만 False임
bool(-1) # True
bool("False") # True
a = None 
a is None

v = 2 + 3j
v.real # 2
v.imag # 3

5 % 2 # 1
5 // 2 # 2

if a != 1 :
    print("1이 아님")

a = a * 10
a *= 10 # 위와 동일한 표현

x = True
y = False

if x and y :
    print("Yes")
else :
    print("No")
    
a = 8 # 0000 1000
b = 11 # 0000 1011
c = a & b # 0000 1000 (8)
d = a ^ b # 0000 0011 (3)

print(c)
print(d)    
    
a = [1,2,3,4]
b = 3 in a # True
print(b)    

a = "ABC"
b = a
print(a is b) # True    

s = '가나다'
s = "가나다"

s = '''아리랑
아리랑
아라리요
'''
print(s)

s = '아리랑\n아리랑\n아라리요'
print(s)

p = "이름: %s 나이: %d" % ("김유신",65)
print(p)
p = "X = %0.3f, Y = %10.2f" % (3.141592,3.141592)
print(p)

## Conversion Specifier
# %s :	문자열 (파이썬 객체를 str()을 사용하여 변환)
# %r :	문자열 (파이썬 객체를 repr()을 사용하여 변환)
# %c :	문자(char)
# %d 또는 %i :	정수 (int)
# %f 또는 %F	 : 부동소수 (float) (%f 소문자 / %F 대문자)
# %e 또는 %E	 : 지수형 부동소수 (소문자 / 대문자)
# %g 또는 %G	 : 일반형: 값에 따라 %e 혹은 %f 사용 (소문자 / 대문자)
# %o 또는 %O	 : 8진수 (소문자 / 대문자)
# %x 또는 %X	 : 16진수 (소문자 / 대문자)
# %% : 	% 퍼센트 리터럴    

s = "ABC"
type(s) # class 'str'
v = s[1] # B
type(s[1]) # class 'str'
v

path = r'D:\Workplace\python_programming\Basic'
print(path)

s = ','.join(['가나','다라','마바'])
print(s)
s = ''.join(['가나','다라','마바'])
print(s)

items = '가나,다라,마바'.split(',')
print(items)

departure, _, arrival = "Seattle-Seoul".partition('-')
print(departure)

# 위치를 기준으로 한 포맷팅
s = "Name: {0}, Age: {1}".format("강정수",30)
print(s)

# 필드명을 기준으로 한 포맷팅
s = "Name: {name}, Age: {age}".format(name="강정수",age=30)
print(s)

# object의 인덱스 혹은 키를 사용하여 포맷팅
area = (10,20)
s = "width: {x[0]}, height: {x[1]}".format(x = area)
print(s)

# 조건문
x = 2
if x < 10:
    print(x)
    print("한자리수")
    
x = 10
if x < 10:
    print("한자리수")
elif x < 100:
    print("두자리수")
else:
    print("세자리 이상")
    
n = 3
if n < 10:
    pass
else:
    print(n)

# 반복문
i = 1
while i <= 10:
    print(i)
    i += 1    

sum = 0
for i in range(11):
    sum += i
    print(sum)
    
list = ["This","is","a","book"]
for s in list:
    print(s)    
    
i = 0
sum = 0
while True:
    i += 1
    if i == 5:
        continue
    if i > 10:
        break
    sum += i
    
print(sum)    

numbers = range(2,11,2)
for x in numbers:
    print(x)

for i in range(10):
    print("Hello")    

    
