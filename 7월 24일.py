### Unit 34~37

## class

class Person: # class 이름은 보통 대문자로 시작함
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

# example of method
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


class Person:
    bag = []
    def put_bag(self, stuff):
        self.bag.append(stuff)
james = Person()
james.put_bag('책')
maria = Person()
maria.put_bag('열쇠')
print(james.bag)
print(maria.bag)

class Person:
    bag = []
    def put_bag(self, stuff):
        Person.bag.append(stuff)
print(Person.bag)

james.__dict__
Person.__dict__

class Person:
    def __init__(self):
        self.bag = []
    def put_bag(self, stuff):
        self.bag.append(stuff)
james = Person()
james.put_bag('책')
maria = Person()
maria.put_bag('열쇠')
print(james.bag)
print(maria.bag)

class Knight:
    __item_limit = 10
    def print_item_limit(self):
        print(Knight.__item_limit) # class 안에서만 접근 가능
x = Knight()
x.print_item_limit()
print(Knight.__item_limit) # class 바깥에서는 접근 불가능

# docstring
class Person:
    '''사람 클래스입니다.'''
    def greeting(self):
        '''인사 메서드입니다.'''
        print('Hello')
print(Person.__doc__)  # 사람 클래스입니다.
print(Person.greeting.__doc__)  # 인사 메서드입니다.
maria = Person()
print(maria.greeting.__doc__)  # 인사 메서드입니다.

# 정적 method
class Calc:
    @staticmethod # 정적 method
    def add(a, b):
        print(a + b)
    @staticmethod  # 정적 method
    def mul(a, b):
        print(a * b)
Calc.add(10, 20)
Calc.mul(10, 20)

# 클래스 method
class Person:
    count = 0 # 클래스 속성
    def __init__(self):
        Person.count += 1 # 인스턴스가 만들어질 때 클래스 속성 count에 1을 더함.
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count)) # cls로 클래스 속성에 접근
james = Person()
maria = Person()
Person.print_count() # 2명 생성되었습니다.


# inheritance
class Person:
    def greeting(self):
        print('안녕하세요.')
class Student(Person):
    def study(self):
        print('공부하기')
james = Student()
james.greeting() # 안녕하세요. : 기반 클래스 Person의 method 호출
james.study() # 공부하기 : 파생 클래스 Student에 추가한 study method

class Person:
    pass
class Student(Person):
    pass
issubclass(Student, Person)

class Person:
    def greeting(self):
        print('안녕하세요.')
class PersonList():
    def __init__(self):
        self.person_list = [] # 리스트 속성에 Person 인스턴스를 넣어서 관리
    def append_person(self, person): # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장'
james = Student()
print(james.school)
print(james.hello) # 기반 클래스의 속성을 출력하려고 하면 error가 발생함

# 클래스 초기화
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__() # super() 로 기반 클래스(Person)의 __init__ method 호출
        self.school = '파이썬 코딩 도장'
james = Student()
print(james.school)
print(james.hello)

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
class Student(Person):
    pass
james = Student()
print(james.hello)

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()
        self.school = '파이썬 코딩 도장'

# overriding
class Person:
    def greeting(self):
        print('안녕하세요.')
class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
james = Student()
james.greeting()

class Person:
    def greeting(self):
        print('안녕하세요.')
class Student(Person):
    def greeting(self):
        super().greeting() # 기반 클래스의 method를 호출하여 중복을 줄임
        print('저는 파이썬 코딩 도장 학생입니다.')
james = Student()
james.greeting()

class Person:
    def greeting(self):
        print('안녕하세요.')
class University:
    def manage_credit(self):
        print('학점 관리')
class Undergraduate(Person, University):
    def study(self):
        print('공부하기')
james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()

# diamond inheritance (비추천) -> # Method Resolution Order
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')
class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')
class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')
class D(B, C):
    pass
x = D()
x.greeting()  # 안녕하세요. B입니다.
D.mro()

# object class
int.mro()
class X:
    pass
class X(object):
    pass

# abstract class : 상속받는 클래스에서 메서드 구현 강제
from abc import *
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
    @abstractmethod
    def go_to_school(self):
        pass
class Student(StudentBase):
    def study(self):
        print('공부하기')
james = Student()
james.study() # error

from abc import *
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
    @abstractmethod
    def go_to_school(self):
        pass
class Student(StudentBase):
    def study(self):
        print('공부하기')
    def go_to_school(self):
        print('학교가기')
james = Student()
james.study()
james.go_to_school()
james = StudentBase() # error

class AdvancedList(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new
x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)


## 두 점 사이의 거리 구하기

import math
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p1 = Point2D(x=30, y=20)
p2 = Point2D(x=60, y=50)
print('p1: {} {}'.format(p1.x, p1.y))
print('p2: {} {}'.format(p2.x, p2.y))
a = p2.x - p1.x
b = p2.y - p1.y
c = math.sqrt(a**2 + b**2)
print(c)

import math
import collections
Point2D = collections.namedtuple('Point2D', ['x', 'y'])
p1 = Point2D(x=30, y=20)
p2 = Point2D(x=60, y=50)
a = p2.x - p1.x
b = p2.y - p1.y
c = math.sqrt(math.pow(a,2)+math.pow(a,2))
print(c)













