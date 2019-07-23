### Unit 34

## class

class Person:
    def greeting(self):
        print('Hello')
james = Person()
james.greeting() # call method

# example of class
a = int(10)
a
b = list(range(10)) # object, instance of list class
b
c = dict(x=10, y=20)
c

# example of mathod
b = list(range(10))
b.append(20)
b

# checking type
a = 10
type(a)
b = [0,1,2]
type(b)
c = {'x':10, 'y':20}
type(c)
maria = Person()
type(maria)

class Person:
    pass
james = Person()
isinstance(james, Person)

class Person:
    def greeting(self):
        print('Hello')
    def hello(self):
        self.greeting() # self.method() 형식으로 클래스 안의 메서드 호출
james = Person()
james.hello() # Hello

def factorial(n):
    if not isinstance(n, int) or n < 0: # n이 정수가 아니거나 음수이면 함수를 끝냄
        return None
    if n == 1:
        return 1
    return n * factorial(n-1)

# make attribute
class Person:
    def __init__(self):
        self.hello = '안녕하세요.'
    def greeting(self):
        print(self.hello)
james = Person()
james.greeting() # 안녕하세요.

class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))
maria = Person('마리아',20,'서울시 서초구 반포동')
maria.greeting()
print('이름:', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)

class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]
maria = Person(*['마리아',20,'서울시 서초구 반포동'])

class Person:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']
maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})

class Person:
    pass
maria = Person()
maria.name = '마리아'
maria.name
james = Person()
james.name # error

class Person:
    def greeting(self):
        self.hello = '안녕하세요.'
maria = Person()
maria.hello # error
maria.greeting()
maria.hello

class Person:
    __slots__ = ['name','age'] # name, age만 허용(다른 속성은 생성 제한)
maria = Person()
maria.name = '마리아'
maria.age = 20
maria.address = '서울시 서초구 반포동' # error

# private attribute
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.__wallet -= 10000 # error

class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet
    def pay(self, amount):
        self.__wallet -= amount
        print('이제 {0}원 남았네요.'.format(self.__wallet))
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)

class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet
    def pay(self, amount):
        if amount > self.__wallet:
            print('돈이 모자라네...')
            return
        self.__wallet -= amount
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(20000)


class Person:
    def __greeting(self):
        print('Hello')
    def hello(self):
        self.__greeting()  # 클래스 안에서는 비공개 메서드를 호출할 수 있음
james = Person()
james.__greeting()  # 에러: 클래스 바깥에서는 비공개 메서드를 호출할 수 없음


### Unit 35








