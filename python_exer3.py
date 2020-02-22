# 집합 자료형 : set
# no = set(['Agent of sheild', 'Agent carter', 'Harry porter']) 이렇게는 안된다
n = set([1,2,3])
print(n)

m = set("Finn and Jake Adventure Time")
print(m) # {'t', 'a', 'J', ' ', 'd', 'e', 'v', 'n', 'r', 'm', 'A', 'u', 'T', 'F', 'i', 'k'}
# 비어있는 집합 자료형은 s = set()으로 만들수 있다

# 집합 자료형의 특징
# set("Finn and Jake Adventure Time")의 결과가 이상하다!
# 집합의 특징 : 1. 중복 허용하지 않음 2. 순서가 없음
# 리스트나 튜플은 순서가 있어서 인덱싱으로 자료를 얻을 수 있지만 집합은 인덱싱으로 자료 얻을수 없다
# ** 딕셔너리도 순서가 없는 자료형이기 때문에 인덱싱을 지원하지 않는다!
# print(n[1]) # TypeError: 'set' object does not support indexing

qq = set([5,6,17,48,3,26])
ff = set([57,26,9,7,10,5])

# !. 교집합
print(qq & ff) # {26, 5}
print(qq.intersection(ff)) # 같은 결과

# 2. 합집합
print( qq|ff ) # {3, 5, 6, 7, 9, 10, 48, 17, 57, 26}
print(qq.union(ff)) # 같은 결과

# 3. 차집합
print(qq-ff) # {48, 17, 3, 6}
print(ff-qq) # {9, 10, 57, 7}
print(qq.difference(ff)) # {48, 17, 3, 6}
print(ff.difference(qq)) # {9, 10, 57, 7}

# 집합 자료형과 관련된 함수들
# 1. 집합에 값 1개 추가하기
qq.add(91)
# print(qq) # {3, 5, 6, 48, 17, 26, 91}

# 2. 값 여러 개 추가하기
qq.update([42,56,8])
print(qq) # {3, 5, 6, 8, 42, 48, 17, 56, 26, 91}

# 3. 특정 값 제거하기
qq.remove(56)
qq.remove(5)
qq.remove(8)
qq.remove(42)
print(qq) # {3, 6, 48, 17, 26, 91}

print("*************************************************")

# bool 자료형 : True(참)와 False(거짓) 2가지 값만을 나타내는 표현형
a = True
b = False

# 자료형 확인
print(type(a))
print(type(b)) # b.type()이거 불가능 한가보다...

# 특정 값의 참과 거짓
# "python" : 참  /  "" : 거짓  /  [1,2,3] : 참  /  [], {}, () : 거짓  /  1 : 참  /  0:거짓  / None : 거짓
# 문자열, 리스트, 튜플, 딕셔너리 모두 비어있으면 거짓, 비어있지 않으면 참이 된다.
# 숫자는 그값이 0이 되면 거짓이 된다.

# Boolean 자료형이 어디에 쓰일까?
while qq: # qq는 집합 자료형이다 그런데 가능!
    print(qq.pop()) # qq가 참인 경우 pop()을 계속 실행하라는 의미
    # qq가 비게 되면 거짓이 되어 while문이 중지된다
# while 조건문:
#    수행할 문장

# if[] : # (비어있으므로) 거짓 이면
#     print("TRUE") # 참이라고 출력 (??)
# else :
#     print("FALSE")

# Boolean의 내장함수
print(bool('Power Puff Girl')) # 빈 문자열은 거짓이 나온다.
print(bool(''))

print("*************************************************")

# 자료형의 값을 저장하는 공간, 변수
# 우리가 쓰는 a, b, qq 같은 것이 변수이다. 이때 = (assignment)기호를 사용
# 파이썬은 저장된 값을 스스로 판단하여 자료형을 스스로 지정하여 편하다

# 변수 = 객체! 객체란 우리가 지금까지 본 자료형 같은 것들이다....?
# a =[1,2,3]라고 하면 [1,2,3]의 값을 가지는 객체가 메모리에 생성되고 변수 a에는 메모리의 주소가 저장된다.
# 메모리 주소를 확인
print(id(qq)) # 2560228152712 <- qq의 주소값

#리스트를 복사할떄
a = [1, 2, 3, 4]
b =a # 이러면 a의 리스트 값이 복사가 될까?
print(b) # [1, 2, 3, 4] b는 a와 완전 동일하지만
# [1, 2, 3, 4] 리스트를 참조(?)하는 변수가 a변수 1개에서 2개로 늘어났다는 것
print(id(a)) # 1483045137224
print(id(b)) # 1483045137224 이 둘은 주소도 동일하다!!
print(a is b) # True <- a와 b의 객체는 동일한가? 예
# 그래서
a[1] = 6
print(a) # [1, 6, 3, 4]
print(b) # [1, 6, 3, 4] 둘 중 하나만 바뀌어도 둘 다 바뀐다

# 그렇다면 b에 a값을 복사 하면서도 다른 주소를 가리키도록 할수는 없을까?
# 1. [:] 이용
bb = a[:] # 리스트 전체를 가리키는 방법
print(id(a)) # 1483045137224
print(id(bb)) # 1483045110920 서로 다르다!

# 2. copy모듈 이용
from copy import copy
bbb = copy(a)
print(a is bbb) # False

# 변수를 만드는 여러가지 방법?
r,t = ('rick','morty') # 튜플로 대입
(rr,tt) = 'blossum', 'bubble' # 튜플은 괄호를 생략해도 된다.
[rrr,ttt] = ['buttercup','eleven'] # 리스트로 만들수도 있다.
rrrr = tttt = 'daisy' # 그냥 같은 값 대입

# 두 변수 값을 바꾸는 방법
rt = 'chloe'
tr = 'rose'
rt, tr = tr,rt
print(rt) # rose
print(tr) # chloe
