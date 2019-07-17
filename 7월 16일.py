### Unit 08~12

korean = 92
english = 47
mathematics = 86
science = 81

print(korean >= 50 and english >= 50 and mathematics >= 50 and science >= 50)


s = ''''Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.'''

print(s)


increment = int(input())
t = tuple(range(-10, 10, increment))

print(t)


x = input().split()
del x[-5:]

print(tuple(x))


a, b = input().split()
s = a[1::2] + b[::2]     # 인덱스가 홀수 + 인덱스가 짝수

print(s)


keys = input().split()
values = map(float, input().split())
lux = dict(zip(keys, values))

print(lux)
