### Unit 30~31

def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)
print_numbers(10, 20, 30)

# unpacking
x = [10, 20, 30]
print_numbers(*x)
print_numbers(*[10, 20, 30])
print_numbers(*[10, 20]) # error

# 가변 인수 함수
def print_numbers(*args):
    for arg in args:
        print(arg)
print_numbers(10,20,30,40)
x = [10,20,30,40]
print_numbers(*x)

def print_numbers(a, *args):
    print(a)
    print(args)
print_numbers(1)
print_numbers(1,10,20)
print_numbers(*[10,20,30])

# 키워드 인수
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동')

# dictionary unpacking
x = {'name':'홍길동', 'age':30, 'address':'서울시 용산구 이촌동'}
personal_info(**x)

def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
x = {'name':'홍길동', 'age':30, 'address':'서울시 용산구 이촌동'}
personal_info(**x)

def personal_info(**kwargs):
    if 'name' in kwargs:
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])

def personal_info(name, **kwargs):
    print(name)
    print(kwargs)







