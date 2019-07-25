### 7월 25일 시험



## Q3
a, b = map(int, input().split())
sum = 0
for i in range(a, b+1):
    if i % 2 != 0:
        sum += i
print(sum)



## Q4
p = float(input())
mul = 1
count = 0
while True:
    mul *= (1 + p/100)
    count += 1
    if mul >= 2:
        break
print(mul, count)



## Q5
bts = ['RM', '진', '슈가', '제이홉', '지민', '뷔', '정국']
# 1)
print(bts[5])
# 2)
bts[0]
# 3)
print(bts[5:])
# 4)
print(bts[2:5])
# 5)
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
from pprint import pprint
col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
pprint(matrix, indent=2)

def tile(i, k):
    for r in range(i-1, i+2):
        for c in range(k-1, k+2):
            if r < 0 or r >= row or c < 0 or c >= col:
                continue
            if matrix[r][k] == matrix[i][k] or matrix[i][c] == matrix[i][k]:
                return '*'
            else:
                return matrix[i][k]
for i in range(row):
    for k in range(col):
        print(tile(i, k), end='')
    print()



## Q9
a = [1, 3, 5, 7, 9]
b = list(map(lambda x: x**2 , a))
print(b)



