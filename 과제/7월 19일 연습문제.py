## Q1
# 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부른다.
# 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 이다.
# 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마인가?

set_A = []
set_B = []
set_C = []

for i in range(100,1000):
    A = i
    for k in range(100,1000):
        B = k
        C = A * B
        str_C = str(C)
        if list(str_C) == list(reversed(str_C)):
            set_A.append(A)
            set_B.append(B)
            set_C.append(C)
            
ans_A = set_A[set_C.index(max(set_C))]
ans_B = set_B[set_C.index(max(set_C))]
ans_C = set_C[set_C.index(max(set_C))]

ans = dict(zip(['A','B','C'],[ans_A,ans_B,ans_C]))
print(ans)



## Q2
# 시저 암호는, 고대 로마의 황제 줄리어스 시저가 만들어 낸 암호인데,
# 예를 들어 알파벳 A를 입력했을 때, 그 알파벳의 n개 뒤에 오는 알파벳이 출력되는 것이다.
# 예를 들어 바꾸려는 단어가 'CAT"고, n을 5로 지정하였을 때 "HFY"가 되는 것이다.
# 어떠한 암호를 만들 문장과 n을 입력했을 때 암호를 만들어 출력하는 프로그램을 작성하시오.
# - 입력 : 화면에서 문자열과 n값을 입력받는다. (예: ROSE 5)
# - 출력 : 암호화된 문자열을 출력

word = str(input())
n = int(input())

from string import ascii_uppercase
alphabet = list(ascii_uppercase)

answer = []
for i in range(len(word)):
    ind = alphabet.index(word[i]) + n
    if ind > 25:
        answer.append('*') # 범위를 벗어난 경우는 '*'표시 처리
    else:
        answer.append(alphabet[ind])
    print(answer[i],end='')
    
    

## Q3
# Linux 명령어인 grep 을 윈도우스에서 만들어 보시오.
# 입력 형태
# 찾을 문자열: public
# 찾을 파일명: f:/Workspace/Egov/xxx.java
# 출력 형태
# 13: public class ClassA {
# 16:     public int number;

# 모범답안
word, filename = input('찾고자 하는 문자열과 파일명> ').split()
lineNo = 1
with open(filename, 'r', encoding='UTF-8') as file:
    for line in file:
        if line.find(word) >= 0:
            print('%2d:' % lineNo, line, end='')
        lineNo += 1



## Q4
# 텍스트를 파일에서 읽은 후 단어의 개수를 세는 프로그램 Word Count를 작성하시오.
# 입력은 텍스트 파일이고, 구분자는 마침표(‘.’), 쉽표(‘,’), 공백(‘ ’)이다.
# 출력은 총 단어수와 가장 많이 나온 순서대로 단어 10개와 그 단어의 빈도이다.

import string
import os
os.chdir("D:/Workplace/python_programming/과제")
with open('words.txt','r') as file:
    words = file.read()

def WordCount(words):
    words_split = words.split()
    for i in range(len(words_split)):
        words_split[i] = words_split[i].strip('\n').strip(string.punctuation).lower()
    words_list = list(set(words_split))  # 중복없음
    words_count = []
    for j in words_list:
        words_count.append((j,words_split.count(j)))
    n = 0
    for k in sorted(words_count, reverse=True):
        print(k[0], ' ', ':', ' ', k[1])
        n += 1
        if n > 10:
            break
WordCount(words)

os.chdir('D:/Workplace/python_programming/과제')



## Q5
# 다음의 지시대로 폴더와 파일을 프로그램에서 만드시오.
# 1. 랜덤으로 1, 2, 3 중 하나를 내용으로 갖는 txt 파일 100개를
# 하나의 디렉토리(c:/Temp/Ex04) 안에 생성하는 코드를 작성하시오.
# (파일 제목은 4자리 정수를 랜덤으로 할당. ex - 1382.txt , 0201.txt , 9012.txt , ......... )
# 2. 제목이 0000~3333 인 txt 파일은 low 폴더로, 3334~6666인 txt 파일은 mid 폴더로,
# 6667~9999 인 파일은 high 폴더로 이동시키는 코드를 작성하시오.
# 3. low, mid, high 폴더 안에 제목이 1, 2, 3 인 폴더를 각각 만들고,
# txt 파일 안의 내용에 따라 txt파일을 폴더안으로 이동시켜 분류하시오.
# - 결론적으로 c:/Temp/Ex04 폴더 밑에는 low, mid, high 폴더 3개가 생기고,
# 이 각각의 폴더에는 1, 2, 3 폴더가 각각 생기고 이 폴더밑에 파일이 들어 있어야 함.

import os
import random as rd
level = ['low','mid','high']
label = list(map(str,list(range(1,4))))
base = "C:/Temp/Ex04/"

for i in range(3):
    for k in range(3):
        path = base + level[i] + "/" + label[k]
        os.makedirs(path)

for i in range(100):
    a = rd.randint(0,9999) # txt 파일 제목의 숫자
    b = rd.randint(1,3) # txt 파일 내용에 들어갈 숫자
    if 0 <= a <= 3333:
        path = base + "low" + "/" + str(b)
        os.chdir(path)
        with open(str(a) + '.txt', 'w') as file:
            file.write(str(b))
    elif 3334 <= a <= 6666:
        path = base + "mid" + "/" + str(b)
        os.chdir(path)
        with open(str(a) + '.txt', 'w') as file:
            file.write(str(b))
    else:
        path = base + "high" + "/" + str(b)
        os.chdir(path)
        with open(str(a) + '.txt', 'w') as file:
            file.write(str(b))
            
os.chdir('D:/Workplace/python_programming/과제')



## Q6
# Binary 파일을 16진수 값으로 출력하는 HexaDump 프로그램을 작성하시오.
# 입력 형태
# 찾을 파일명: C:/Temp/james.p
# 출력 형태
# 00000000:  00 01 44 E4 00 01 64 E4  41 42 43 11 00 61 F4 E4  ..D...d. ABC..a..
# 00000010:  41 42 63 13 00 62 F4 E5  00 01 46 E9 FF 01 65 E2  ABc..b.. ..F...e.
# 00000020:
# 참고자료
# import pickle
# name = 'james'
# age = 17
# address = '서울시 서초구 반포동'
# scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
# with open('james.p', 'wb') as file:  # binary write mode
#     pickle.dump(name, file)
#     pickle.dump(age, file)
#     pickle.dump(address, file)
#     pickle.dump(scores, file)
# with open('james.p', 'rb') as file:  # binary write mode
#     name = pickle.load(file)
#     age = pickle.load(file)
#     address = pickle.load(file)
#     scores = pickle.load(file)
#     print(name)
#     print(age)
#     print(address)
#     print(scores)

