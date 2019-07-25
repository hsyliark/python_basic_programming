### Unit 41

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

