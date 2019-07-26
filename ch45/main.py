import os
os.getcwd()
os.chdir("D:/Workplace_HSY/python_programming/make module")

### make module
## 반드시 모듈과 실행스크립트는 같은 파일 안에 있어야 함.

from ch45 import square2  # import로 square2 모듈을 가져옴
print(square2.base)  # 모듈.변수 형식으로 모듈의 변수 사용
print(square2.square(10))  # 모듈.함수() 형식으로 모듈의 함수 사용

from ch45 import person  # import로 person 모듈을 가져옴
# 모듈.클래스()로 person 모듈의 클래스 사용
maria = person.Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()

from ch45.person import Person
maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()

from ch45 import hello  # hello 모듈을 가져옴
print('main.py __name__:', __name__)  # __name__ 변수 출력

from ch45 import calc
calc.add(50, 60)
calc.mul(50, 60)


### make package

import ch45.calcpkg.operation as op  # calcpkg 패키지의 operation 모듈을 가져옴
import ch45.calcpkg.geometry as geo  # calcpkg 패키지의 geometry 모듈을 가져옴

print(op.add(10, 20))  # operation 모듈의 add 함수 사용
print(op.mul(10, 20))  # operation 모듈의 mul 함수 사용

print(geo.triangle_area(30, 40))  # geometry 모듈의 triangle_area 함수 사용
print(geo.rectangle_area(30, 40))  # geometry 모듈의 rectangle_area 함수 사용

from ch45.calcpkg.operation import add, mul
add(10, 20)
mul(10, 20)

import sys
sys.path

import ch45.calcpkg as calcpkg

print(calcpkg.operation.add(10, 20))  # operation 모듈의 add 함수 사용
print(calcpkg.operation.mul(10, 20))  # operation 모듈의 mul 함수 사용

print(calcpkg.geometry.triangle_area(30, 40))  # geometry 모듈의 triangle_area 함수 사용
print(calcpkg.geometry.rectangle_area(30, 40))  # geometry 모듈의 rectangle_area 함수 사용

from ch45.calcpkg import *   # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴

print(add(10, 20))  # operation 모듈의 add 함수 사용
print(mul(10, 20))  # operation 모듈의 mul 함수 사용

print(triangle_area(30, 40))  # geometry 모듈의 triangle_area 함수 사용
print(rectangle_area(30, 40))  # geometry 모듈의 rectangle_area 함수 사용