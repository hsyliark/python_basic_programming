### Unit 29

## function

def add(a,b):
    print(a+b)
add(10,20)

# docstrings : 설명추가
def add(a,b):
    """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
    print(a+b)
x = add(10,20)
print(x)
print(add.__doc__)

def add(a,b):
    return a+b
x = add(10,20)
x

def one():
    return 1
x = one()
x

def not_ten(a):
    if a == 10:
        return # 함수 중간에 빠져나옴.
    print(a,'입니다.',sep='')
not_ten(5)
not_ten(10)

def add_sub(a,b):
    return a+b, a-b
x, y = add_sub(10,20)
x
y

x = add_sub(10,20):
x


def mul(a, b):
    c = a * b
    return c
def add(a, b):
    c = a + b
    print(c)
    d = mul(a, b)
    print(d)
x = 10
y = 20
add(x, y)

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'









