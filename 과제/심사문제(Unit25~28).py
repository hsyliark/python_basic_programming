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
# 