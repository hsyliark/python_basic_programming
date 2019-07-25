### Unit 40

## generator

def number_generator():
    yield 0
    yield 1
    yield 2
for i in number_generator():
    print(i)
g = number_generator()
g
dir(g)
g.__next__()

def number_generator():
    yield 0
    yield 1
    yield 2
g = number_generator()
a = next(g)
print(a)
b = next(g)
print(b)
c = next(g)
print(c)

def one_generator():
    yield 1
    return 'return에 지정한 값'
try:
    g = one_generator()
    next(g)
    next(g)
except StopIteration as e:
    print(e) # return에 지정한 값

def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1
for i in number_generator(3):
    print(i)
g = number_generator(3)
next(g)




