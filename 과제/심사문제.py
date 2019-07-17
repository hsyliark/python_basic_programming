### Unit 08

korean = 90
english = 81
mathematics = 86
science = 80
print(korean >= 90 and english > 80 and mathematics > 85 and science >= 80)

korean = 90
english = 80
mathematics = 85
science = 80
print(korean >= 90 and english > 80 and mathematics > 85 and science >= 80)



### Unit 09

s = ''''Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.'''
print(s)



### Unit 10

def mylist(s):
    print(tuple(range(-10,10,s)))
mylist(2)
mylist(3)



### Unit 11

# Q1
x = input().split()
del x[5:]
print(tuple(x))

# Q2
a = input()
b = input()
print(a[1::2] + b[0::2])



### Unit 12

key = list(map(str,input().split()))
ability = list(map(float,input().split()))
game = dict(zip(key,ability))
print(game)



### Unit 13

def discount(pay,cash):
    if cash == 'Cash3000':
        pays = pay - 3000
    elif cash == 'Cash5000':
        pays = pay - 5000
    else:
        pays = pay
    print(pays)
    
pay1 = 27000
cash1 = 'Cash3000'
discount(pay1,cash1)
pay2 = 72000
cash2 = 'Cash5000'
discount(pay2,cash2)



### Unit 14

def judge(kor,eng,math,sci):
    average = (kor + eng + math + sci)/4
    if kor < 0 or kor > 100 or eng < 0 or eng > 100 or math < 0 or math > 100 or sci < 0 or sci > 100:
        print('Wrong score')
    elif average >= 80:
        print('pass')
    else:
        print('fail')
judge(89,72,93,82)
judge(100,79,68,71)
judge(99,85,101,90)



### Unit 15

age = int(input())
balance = 9000
if 7 <= age <= 12:
    print(balance - 650)
elif 13 <= age <= 18:
    print(balance - 1050)
else:
    print(balance - 1250)
    
   
   
### Unit 16

for i in range(2,10):
    print(i, '단')
    for k in range(1,10):
        print(i, ' ', '*', ' ', k, ' ', '=', i * k)
        
        

### Unit 17

cash = 10000
while cash >= 0:
    cash -= 1350
    if cash < 0:
        break
    print(cash)
    
cash = 13500
while cash >= 0:
    cash -= 1350
    if cash < 0:
        break
    print(cash)



### Unit 18

start, stop = map(int,input().split())
i = start
while True:
    if i == stop:
        break
    elif i % 10 == 3:
        print('',end='')
    else:
        print(i,end=' ')
    i += 1



### Unit 19

def mountain(i):
    for i in range(1, i+1):
        for k in range(4 - i):
            print(' ', end='')
        for m in range(2 * i - 1):
            print('*', end='')
        for k in range(4 - i):
            print(' ', end='')
        print()
mountain(3)
mountain(5)



### Unit 20

start, stop = map(int,input().split())
for i in range(start, stop + 1):
    if i % 5 == 0 and i % 7 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)
        
        
        
### Unit 21

import turtle as t
def star(n,p):
    t.shape('turtle')
    for i in range(n):
        t.forward(p)
        t.right((360 / n) * 2)
        t.forward(p)
        t.left(360 / n)
star(5,150)
star(6,100)

    
    
        
        
    

    
        
    
    
    
    


    

        
    

