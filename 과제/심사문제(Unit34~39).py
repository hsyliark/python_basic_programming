## Unit 34
# 표준 입력으로 게임 캐릭터 능력치(체력, 마나, AP)가 입력됩니다.
# 다음 소스 코드에서 애니(Annie) 클래스를 작성하여
# 티버(tibbers) 스킬의 피해량이 출력되게 만드세요.
# 티버의 피해량은 AP * 0.65 + 400이며
# AP(Ability Power, 주문력)는 마법 능력치를 뜻합니다.

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    def tibbers(self):
        print('티버: 피해량', self.ability_power * 0.65 + 400)
health, mana, ability_power = map(float, input().split())
x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()



## Unit 35
# 표준 입력으로 시:분:초 형식의 시간이 입력됩니다.
# 다음 소스 코드에서 Time 클래스를 완성하여 시, 분, 초가 출력되게 만드세요.
# from_string은 문자열로 인스턴스를 만드는 메서드이며
# is_time_valid는 문자열이 올바른 시간인지 검사하는 메서드입니다.
# 시간은 24시까지, 분은 59분까지, 초는 60초까지 있어야 합니다.
# 정답에 코드를 작성할 때는 class Time:에 맞춰서 들여쓰기를 해주세요.

time_string = input()

class Time:
    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour <= 24 and minute <= 59 and second <= 60
    class From_string:
        def __init__(self, time_string):
            self.time_string = time_string
        hour, minute, second = map(int, time_string.split(':'))

if Time.is_time_valid(time_string):
    t = Time.From_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')



## Unit 36
# 다음 소스 코드에서 동물 클래스 Animal과 날개 클래스 Wing을 상속받아
# 새 클래스 Bird를 작성하여 '먹다', '파닥거리다', '날다', True, True가
# 각 줄에 출력되게 만드세요.

class Animal:
    def eat(self):
        print('먹다')
class Wing:
    def flap(self):
        print('파닥거리다')
class Bird(Animal, Wing):
    def fly(self):
        print('날다'

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))



## Unit 37
# 표준 입력으로 x, y 좌표 4개가 입력되어 Point2D 클래스의 인스턴스 리스트에 저장됩니다.
# 여기서 점 4개는 첫 번째 점부터 마지막 점까지 순서대로 이어져 있습니다.
# 다음 소스 코드를 완성하여 첫 번째 점부터 마지막 점까지 연결된 선의 길이가 출력되게 만드세요.

import math
class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())
for i in range(0,3):
    length += math.sqrt((p[i+1].x - p[i].x)**2+(p[i+1].y - p[i].y)**2)
print(length)



## Unit 38
# 표준 입력으로 문자열이 입력됩니다.
# 다음 소스 코드를 완성하여 입력된 문자열이 회문이면 문자열을 그대로 출력하고,
# 회문이 아니면 '회문이 아닙니다.'를 출력하도록 만드세요.
# palindrome 함수와 NotPalindromeError 예외를 작성해야 합니다.

class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')
def palindrome(word):
    if list(word) != list(reversed(word)):
        raise NotPalindromeError
    else:
        print(word)

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)



## Unit 39
# 표준 입력으로 정수 세 개가 입력됩니다
# (첫 번째 정수는 시작하는 초, 두 번째 정수는 반복을 끝낼 초,
# 세 번째 정수는 인덱스이며 입력되는 초의 범위는 0~100000,
# 입력되는 인덱스의 범위는 0~10입니다).
# 다음 소스 코드에서 시간 값을 생성하는 이터레이터를 만드세요.
# 1) 시간 값은 문자열이고 시:분:초 형식입니다.
# 만약 숫자가 한 자리일 경우 앞에 0을 붙입니다(예: 12:01:08).
# 2) 1초는 00:00:01입니다.
# 23:59:59를 넘길 경우 00:00:00부터 다시 시작해야 합니다.
# 3) 시간은 반복을 끝낼 초 직전까지만 출력해야 합니다
# (반복을 끝낼 초는 포함되지 않음).

class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.stop:
            if self.start < 86400:
                r = self.start
            else:
                r = self.start - 86399
            minute, second = divmod(r, 60)
            hour, minute = divmod(minute, 60)
            self.start += 1
            return '%02d' % hour + ':' + '%02d' % minute + ':' + '%02d' % second
        else:
            raise StopIteration

start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')