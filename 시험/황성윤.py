### 7월 25일 시험



## Q3
a, b = map(int, input().split())
if a > b:
    a, b = b, a
sum = 0
for i in range(a, b+1):
    if i % 2 != 0:
        sum += i
print(sum)



## Q4
p = float(input('rate(%)>'))
p /= 100
mul = 1
year = 0
while True:
    mul *= (1 + p/100)
    year += 1
    if mul >= 2:
        break
print(mul, year)



## Q5
bts = ['RM', '진', '슈가', '제이홉', '지민', '뷔', '정국']
# 1)
print(bts[5])
# 2)
print(bts[0:1])
# 3)
print(bts[5:])
# 4)
print(bts[2:5])
# 5)
print(bts[::2])
a = []
for i in range(len(bts)):
    if i % 2 != 0:
        continue
    else:
        a.append(bts[i])
print(a)



## Q6
def my_print(**dic):
    for kw, arg in sorted(dic.items(), key=lambda x: x[1], reverse=True):
        print(kw, ':', '{0:>7,}'.format(arg))
vegetables = {'가지':800, '오이':600, '수박':15000, '호박':1000, '깻잎':500}
my_print(**vegetables)



## Q7
set_X = []
set_Y = []
set_Z = []
for i in range(100, 1000):
    X = i
    for k in range(100, 1000):
        Y = k
        Z = X * Y
        str_Z = str(Z)
        if list(str_Z) == list(reversed(str_Z)):
            set_X.append(X)
            set_Y.append(Y)
            set_Z.append(Z)
ans_X = set_X[set_Z.index(max(set_Z))]
ans_Y = set_Y[set_Z.index(max(set_Z))]
ans_Z = set_Z[set_Z.index(max(set_Z))]
ans = dict(zip(['X', 'Y', 'Z'], [ans_X, ans_Y, ans_Z]))
print(ans)



## Q8
# 모범답안
import random as rd
from pprint import pprint
tile = []
for i in range(5):
    row = []
    for k in range(5):
        tmp = rd.randint(1, 4)
        row.append(tmp)
        print(tmp, end=' ')
    tile.append(row)
    print()
#pprint(tile, indent=2)
tpTile = [list(x) for x in zip(*tile)]

def findPung(line):  # 한 라인을 매개변수로 받아, 결과, 시작, 끝 인덱스 반환
    start = 0
    stop = 0
    pung = False
    for i in range(3):
        if line[i] != line[i+1] or line[i+1] != line[i+2]:
            continue
        pung = True
        start = i
        stop = i+2
        if i == 2:
            break
        if line[i+2] != line[i+3]:
            break
        stop = i+3
        if i == 1:
            break
        if line[i+3] == line[i+4]:
            stop = i+4
        break
    return pung, start, stop

def copyLine(pung, start, stop, line):
    newLine = line.copy()
    if pung:
        for i in range(start, stop+1):
            newLine[i] = 8
    return newLine

rowResult = []
for i in range(5):
    pung, start, stop = findPung(tile[i])
    #print(pung, start, stop, tile[i])
    rowResult.append(copyLine(pung, start, stop, tile[i]))
#pprint(rowResult, indent=2)

colResult = []
for i in range(5):
    pung, start, stop = findPung(tpTile[i])
    #print(pung, start, stop, tpTile[i])
    colResult.append(copyLine(pung, start, stop, tpTile[i]))
#pprint(colResult, indent=2)
tpColResult = [list(x) for x in zip(*colResult)]

print('   ==>')
for i in range(5):
    for k in range(5):
        if rowResult[i][k] == 8 or tpColResult[i][k] == 8:
            tile[i][k] = '*'
            print('*', end=' ')
        else:
            tile[i][k] = str(tile[i][k])
            print(tile[i][k], end=' ')
    print()
#pprint(tile, indent=2)


## Q9
a = [1, 3, 5, 7, 9]
b = list(map(lambda x: x**2 , a))
print(b)



