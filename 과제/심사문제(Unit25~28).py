## Unit 25
# 표준 입력으로 문자열 여러 개와 숫자 여러 개가 두 줄로 입력되고,
# 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성합니다.
# 다음 코드를 완성하여 딕셔너리에서 키가 'delta'인 키-값 쌍과 값이 30인 키-값 쌍을 삭제하도록 만드세요.
# 입력
# alpha bravo charlie delta
# 10 20 30 40
# alpha bravo charlie delta echo foxtrot golf
# 30 40 50 60 70 80 90

keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

x = {keys: values for keys, values in x.items() if values != 30}
x = {keys: values for keys, values in x.items() if keys != 'delta'}

print(x)



## Unit 26
# 표준 입력으로 양의 정수 두 개가 입력됩니다.
# 다음 소스 코드를 완성하여 두 숫자의 공약수를 세트 형태로 구하도록 만드세요.
# 단, 최종 결과는 공약수의 합으로 판단합니다.

n1, n2 = map(int, input('양의 정수 두 개 입력>').split())
a = {i for i in range(1,n1+1) if n1 % i == 0}
b = {j for j in range(1,n2+1) if n2 % j == 0}
divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)



## Unit 27
# 문자열이 저장된 unit27.txt 파일이 주어집니다(문자열은 한 줄로 저장되어 있습니다).
# unit27.txt 파일에서 문자 c가 포함된 단어를 각 줄에 출력하는 프로그램을 만드세요.
# 단어를 출력할 때는 등장한 순서대로 출력해야 하며 ,(콤마)와 .(점)은 출력하지 않아야 합니다.
# 입력내용
# Fortunately, however, for the reputation of Asteroid B-612,
# a Turkish dictator made a law that his subjects, under pain of death,
# should change to European costume. So in 1920 the astronomer gave his demonstration all over again,
# dressed with impressive style and elegance. And this time everybody accepted his report.

import string
import os
os.chdir("D:\Workplace\python_programming\과제")
with open('unit27.txt','r') as file:
    words = file.read()
words_split = words.split()
for i in range(len(words_split)):
    words_split[i] = words_split[i].strip(string.punctuation).lower()
    for letter in words_split[i]:
        if 'c' in letter:
            print(words_split[i])
os.chdir("D:\Workplace\python_programming")



## Unit 28
# 단어가 줄 단위로 저장된 words.txt 파일이 주어집니다.
# words.txt 파일에서 회문인 단어를 각 줄에 출력하는 프로그램을 만드세요.
# 단어를 출력할 때는 등장한 순서대로 출력해야 합니다.
# 그리고 파일에서 읽은 단어는 \n이 붙어있으므로 \n을 제외한 뒤 회문인지 판단해야 하며
# 단어를 출력할 때도 \n이 출력되면 안 됩니다(단어 사이에 줄바꿈이 두 번 일어나면 안 됨).
# 입력내용
# apache
# decal
# did
# neep
# noon
# refer
# river

import string
import os
os.chdir("D:\Workplace\python_programming\과제")
with open('unit28.txt','r') as file:
    words = file.read()
words_split = words.split('\n')
for word in words_split:
    for i in range(len(word)//2):
        if word[i] == word[-1-i]:
            print(word)
os.chdir("D:\Workplace\python_programming")





