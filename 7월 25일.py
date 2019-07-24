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






