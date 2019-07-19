### Unit 25~28


## dictionary

x = {'a':10, 'b':20, 'c':30, 'd':40}
x.setdefault('e')
x
x.setdefault('f',100)
x
x.setdefault('a',90)
x
x.update(e=50)
x

x = {'a':10, 'b':20, 'c':30, 'd':40}
x.update(a=90)
x
x.update(e=50)
x
x.update(a=900,f=60)
x

y = {1:'one', 2:'two'}
y.update({1:'ONE',3:'THREE'})
y
y.update([[2,'TWO'],[4,'FOUR']])
y
y.update(zip([1,2],['one','two']))
y

x = {'a':10, 'b':20, 'c':30, 'd':40}
x.pop('a')
x
x.pop('z',0)
del x['b']
x

x = {'a':10, 'b':20, 'c':30, 'd':40}
x.popitem()
x
x.clear()
x

x = {'a':10, 'b':20, 'c':30, 'd':40}
x.get('a')
x.get('z',0)
x.items()
x.keys()
x.values()

keys = ['a','b','c','d']
x = dict.fromkeys(keys)
x
y = dict.fromkeys(keys,100)
y

x = {'a':10, 'b':20, 'c':30, 'd':40}
x['z']
from collections import defaultdict
y = defaultdict(int)
y['z']
int()
z = defaultdict(lambda:'python')
z['a']
z[0]

x = {'a':10, 'b':20, 'c':30, 'd':40}
for i in x:
    print(i,end=' ')
for key, value in x.items():
    print(key, value)
for i in x:
    print(i,x[i])
for key in x.keys():
    print(key,end=' ')
for value in x.values():
    print(value, end=' ')
for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items():
    print(key, value)

def return_python():
    return 'python'
return_python()
y = defaultdict(return_python)
y['a']
y[0]

keys = ['a','b','c','d']
x = {key: value for key, value in dict.fromkeys(keys).items()}
x

y = {key:None for key in keys}
y

{key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()}
{value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()}

x = {'a':10, 'b':20, 'c':30, 'd':40}
for key, value in x.items():
    if value == 20:
        del x[key]
print(x)

x = {key: value for key, value in x.items() if value != 20}
x

# dictionary in dictionary
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
print(terrestrial_planet['Venus']['mean_radius'])


## set

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
fruits

fruits = {'orange','orange','cherry'}
fruits  # 중복될 수 없음.

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits[0]) # error
fruits['strawberry'] # error
'orange' in fruits
'peach' in fruits
'orange' not in fruits
'peach' not in fruits

a = set('apple')
a

b = set(range(5))
b

c = set()
c

c = {}
type(c)
c = set()
type(c)

set('안녕하세요')
a = {{1, 2}, {3, 4}} # error : 세트 넣기 불가능
# frozenset : 내용변경 불가 집합
a = frozenset(range(10))
a
a |= 10 # error
a.update({10}) # error

a = {1,2,3,4}
b = {3,4,5,6}
a | b
set.union(a,b)
a & b
set.intersection(a,b)
a - b
set.difference(a,b)
a ^ b
set.symmetric_difference(a,b)

a = {1,2,3,4}
a |= {5}
a
a = {1,2,3,4}
a.update({5})
a

a = {1,2,3,4}
a &= {0,1,2,3,4}
a
a = {1,2,3,4}
a.intersection_update({0,1,2,3,4})
a

a = {1, 2, 3, 4}
a -= {3}
a
a = {1, 2, 3, 4}
a.difference_update({3})
a

a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
a
a = {1, 2, 3, 4}
a.symmetric_difference_update({3, 4, 5, 6})
a

a = {1, 2, 3, 4}
a <= {1, 2, 3, 4}
a.issubset({1, 2, 3, 4, 5})

a = {1, 2, 3, 4}
a < {1, 2, 3, 4, 5}

a = {1, 2, 3, 4}
a >= {1, 2, 3, 4}
a.issuperset({1, 2, 3, 4})

a = {1, 2, 3, 4}
a > {1, 2, 3}

a = {1, 2, 3, 4}
a == {1, 2, 3, 4}
a == {4, 2, 1, 3} # True

a = {1, 2, 3, 4}
a != {1, 2, 3}

a = {1, 2, 3, 4}
a.isdisjoint({5, 6, 7, 8})       # 겹치는 요소가 없음
a.isdisjoint({3, 4, 5, 6})    # a와 3, 4가 겹침

a = {1,2,3,4}
a.add(5)
a
a.remove(3)
a
a.discard(2)
a
a.discard(3)
a

a = {1,2,3,4}
a.pop()
a
a.clear()
a
a = {1,2,3,4}
len(a)

a = {i for i in 'apple'}
a
a = {i for i in 'pineapple' if i not in 'apl'}
a


## file
# Open -> Write/Read/Update -> Close

import os
os.getcwd() # 현재 작업위치 출력
os.chdir("D:/Workplace_HSY/python_programming") # 작업위치 변경
os.mkdir("C:/Temp/Ex04",2345) # 파일 만들기
os.listdir() # 파일 확인

file = open('hello.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
file.write('Hello, world!')      # 파일에 문자열 저장
file.close()                     # 파일 객체 닫기

file = open('hello.txt', 'r')    # hello.txt 파일을 읽기 모드(r)로 열기. 파일 객체 반환
s = file.read()                  # 파일에서 문자열 읽기
print(s)                         # Hello, world!
file.close()                     # 파일 객체 닫기

# auto closing
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    s = file.read()                     # 파일에서 문자열 읽기
    print(s)                            # Hello, world!

# 문자열 여러 줄을 파일에 쓰기
with open('hello.txt', 'w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))

# 리스트에 들어있는 문자열을 파일에 쓰기
lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
with open('hello.txt', 'w') as file:
    file.writelines(lines)

# 파일의 내용을 한 줄씩 리스트로 가져오기
with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# 파일의 내용을 한 줄씩 읽기
with open('hello.txt', 'r') as file:
    line = None # 변수 line을 None으로 초기화
    while line != '':
        line = file.readline()
        print(line.strip('\n')) # 파일에서 읽어온 문자열에서 \n 삭제하여 출력
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    for line in file:    # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력
file = open('hello.txt', 'r')
a, b, c = file # iterator
a, b, c

# 객체를 파일에 저장하기, 가져오기
import pickle
name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
with open('james.p', 'wb') as file: # binary write mode
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)
with open('james.p', 'rb') as file: # binary write mode
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)


## 회문(palindrome) : 거꾸로 읽어도 제대로 읽음.

word = input('단어를 입력하세요: ')
is_palindrome = True
for i in range(len(word) // 2): # 버림 나눗셈
    if word[i] != word[-1-i]:
        is_palindrome = False
        break
print(is_palindrome)

word = input('단어를 입력하세요: ')
print(word == word[::-1]) # 원래 문자열과 반대로 뒤집은 문자열을 비교

word = 'level'
list(word) == list(reversed(word))

word = 'level'
word == ''.join(reversed(word))


## N-gram : 문자열에서 N개의 연속된 요소 추출

# 2-gram character
text = 'Hello'
for i in range(len(text)-1):
    print(text[i],text[i+1],sep='')

# 2-gram word
text = 'this is python script'
words = text.split()
for i in range(len(words) - 1):
    print(words[i], words[i + 1])

# 2-gram character, word (zip)
text = 'hello'
two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep='')
text = 'hello'
list(zip(text, text[1:]))
text = 'this is python script'
words = text.split()
list(zip(words, words[1:]))

# N-gram
text = 'hello'
[text[i:] for i in range(3)]
list(zip(['hello', 'ello', 'llo']))
list(zip(*['hello', 'ello', 'llo'])) # 각 요소를 콤마로 구분
list(zip(*[text[i:] for i in range(3)]))







