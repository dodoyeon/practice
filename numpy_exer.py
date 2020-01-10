# 1
import numpy as np

# 2
# print(np.__version__)
# np.show_config()

# 3
# z=np.zeros(10)
# print(z) # ㅅ null vector

#4
# x = np.zeros((10,10))
# print(x)
# print("%d bytes" %(x.size*x.itemsize)) # x의 사이즈=100, x의 element의 byte = 8

#5
# %run 'python -c "import numpy; numpy.info(numpy.add)"'

# 6
# y = np.zeros(10)
# y[4] = 1
# print(y)

# 7
# w = np.arange(10,50)
# print(w)

# 8
# q = np.arange(6)
# q = q[::-1]
# print(q)

# 9
# a = np.arange(9).reshape(3,3)
# print(a)

# 10
# b = np.nonzero([1,2,0,0,4,0]) # find non zero element's indices 10
# print(b)

#11
# c = np.eye(3)
# print(c)

#12
# d = np.random.random((3,3,3))
# print(d)

#13
# e = np.random.random((10,10))
# min = e.min()
# max = e.max()
# print(min,max)

#14
# f = np.random.random((30))
# mean = f.mean()
# print(mean)

#15
# uu = np.ones((10,10))
# uu[1:-1,1:-1] = 0 #  행렬은 0부터 시작한다. uu의 1행부터 -1행 전까지 0(즉 -1= 마지막 행이니까 그전까지)
# print(uu)

#16
# g = np.ones((5,5))
# print(g)
# gg = np. pad(g, pad_width = 1, mode = 'constant', constant_values = 0) # pad_width는 가에 패딩을 어떤 두께로 할것인가,
# print(gg)                                                              # constant_value는 어떤 수로 패딩을 할 것인가

#17
# print(0 * np.nan) # nan = not a number
# print(np.nan == np.nan)
# print(np.inf > np.nan) # inf = 무한인듯
# print(np.nan - np.nan)
# print(np.nan in set([np.nan]))
# print(0.3 == 3*0.1) # False 왜지...

#18
# h = np.diag(1+np.arange(4), k = 1)
# print(h)

#19
# i = np.zeros((8,8),dtype = int)
# i[1::2,::2] = 1
# i[::2,1::2] = 1
# print(i)

#20
# print(np.unravel_index(99,(6,7,8))) # 100번째 element 의 index는?

# 21 create checkerboard
# i)
# i = np.zeros((8,8),dtype = int)
# i[1::2,::2] = 1
# i[::2,1::2] = 1
# print(i)

#ii)
# j = np.tile(np.array([[0,1],[1,0]]),(4,4)) # 2x2 행렬(tile)을 4x4만큼 합쳐서 8x8 행렬로 만든다.
# print(j)

# 22
# k = np.random.random((5,5))
# k = (k-np.mean(k))/(np.std(k)) # np.std = 표준편차 <- normalization
# print(k)

#23
# color = np.dtype([("r", np.ubyte,1),
#                   ("g", np.ubyte,1),
#                   ("b", np.ubyte,1),
#                   ("a", np.ubyte,1)])

#24
# i)
# l = np.dot(np.ones((5,3)),np.ones((3,2))) # multiplication
# print(l)
# ii)
# m = np.ones((5,3))@np.ones((3,2))
# print(m)

#25
# n = np.arange(11)
# n[(3<n) & (n<=8)] *=-1 # negate : 마이너스를 붙이는 것
# print(n)

#26
# print(sum(range(5),-1))
# print(range(5)) # -1,1,2,3,4 다 더함
# from numpy import *
# print(sum(range(5),-1)) # 1,2,3,4 다 더함
# print(range(5))

#27
# Z = np.array([1,3,4,5])
# print(Z**Z)
# print(2<<Z>>2)
# print(Z <- Z)
# print(1j*Z)
# print(Z/1/1)
# print(Z<Z>Z) # illegal!

#28
# print(np.array(0)/np.array(0)) # 왜?
# print(np.array(0)//np.array(0)) # 왜??
# print(np.array([np.nan]).astype(int).astype(float)) # array의 형을 통째로 변환하고 싶을때 astype사용
                                                      # dtype은 형을 확인할 수 있는 명령어
#29
# o = np.random.uniform(-10,+10,10)
# print(o)
# print(np.copysign(np.ceil(np.abs(o)),o)) # 두번째 (o)의 부호를 앞의 부호로 사용한다. 부호만 가져옴
                                         # np.abs 는 절댓값을 구함
                                         # np.ceil 은 각원소의 소수자리 올림
#30
# p = np.random.randint(0,10,10)
# q = np.random.randint(0,10,10)
# print(np.intersect1d(p,q)) # intersect 1 dimension : 두 array 사이의 같은 원소 찾아줌

#31
# r = np.ones(3) / 0
# defaults = np.seterr(all = 'ignore')
# r = np.ones(3) / 0
# print(r)
# _ = np.seterr(**defaults)

#32
# print(np.sqrt(-1) == np.emath.sqrt(-1)) # False
# # sqrt는 제곱근을 계산(루트를 계산)
# print(np.sqrt(-1)) # nan
# print(np.emath.sqrt(-1)) # 1j가 나옴

#33
# yeaterday = np.datetime64('today', 'D') - np.timedelta64(1,'D')
# today = np.datetime64('today','D')
# tomarrow = np.datetime64('today','D') + np.timedelta64(1,'D')
# print(yesterday, today, tomarrow)

#34
# s = np.arange('2019-07','20219-08',dtype = "datetime64[D]")
# print(s)

#35
# t= np.ones(3)*1
# u= np.ones(3)*2
# v= np.ones(3)*3
# np.add(t,u,out = u)
# np.divide(t,2,out=t)
# np.negative(t,out=t)
# np.multiply(u,t,out=t)
# print(t)

#36
# vv = np.random.uniform(0,10,10) #(low, high, size) 최솟값이 low 최댓값이 high
# print(vv-vv%1) # 소숫점 버림
# print(np.floor(vv)) # 소수점 버림
# print(np.ceil(vv)-1) # 소수점 올림-1
# print(vv.astype(int)) # int형으로 바꿈
# print(np.trunc(vv)) # 반올림

#37
# A = np.zeros((5,5))
# A += np.arange(5)
# print(A)

#38
# def generator() : # generator는 iterator를 생성해주는 함수, 함수 안에 yeild 키워드를 사용함
#     for x in range(10):
#         yield(x) #
# B = np.fromiter(generator(),dtype = float, count = -1)
# print(B)

# 39
# C= np.linspace(0,1,11,endpoint = False)[1:] # 0과 1을 제외하고 0~1tkdldml size가 10인 벡터를 크기순으로 만듦
# print(C)

#40
# D= np.random.random(10)
# D.sort()
# print(D)

#41 - 더빠른 방법으로 더하기
# E= np.arange(10)
# print(np.add.reduce(E))

#42
# F= np.random.randint(0,2,5)
# G= np.random.randint(0,2,5)
# i) 이건 element마다 같은지 다른지를 알려줌
# print(F==G)
#ii)
# equal = np.allclose(G,F)
# print(equal)
#iii)
# equal = np.array_equal(F,G)
# print(equal)

# 43
# H = np.zeros(10)
# H.flags.writeable = False
# H[0] = 1

# 44 -> cartesian coordinate(직교 좌표계) -> polar coordinates (극좌표계)
# I = np.random.random((10,2))
# print(I)
# J,K = I[:,0], I[:,1]
# print(J) # I에서 0번째 열만 빼서 벡터로
# print(K)
# L = np.sqrt(J**2+K**2) # **2 : 제곱
# M = np.arctan2(K,J) # element-wise arctan
# print(L)
# print(M)

# 45
# N = np.random.random(10)
# N[N.argmax()] =0 # 가장큰 값 찾기
# print(N)

#46
# O = np.zeros((5,5),[('x',float),('y',float)]) # x축과 y축
# O['x'],O['y'] = np.meshgrid(np.linspace(0,1,5),np.linspace(0,1,5)) # linspace(start, end, num point=5개칸으로 나눈다는뜻)
# print(O)

#47 - 주어진 배열로 Cauchy matrix를 만든다. @
# X = np.arange(8)
# print(X)
# Y = X-0.5
# C = 1.0/np.subtract.outer(X,Y)
# print(np.linalg.det(C))

#48
# for dtype in [np.int8, np.int32, np.int64] : # 8, 32, 64 bits 전부다 찾기
#               print(np.iinfo(dtype).min) # integer datatype의 정보를 불러옴 int로 표현할 수 있는 수 중 가장작은 값
#               print(np.iinfo(dtype).max)
# for dtype in [np.float32, np.float64]:
             # print(np.finfo(dtype).min) # floating point의 정보를 불러옴
             # print(np.finfo(dtype).max)
             # print(np.finfo(dtype).eps) # esp = 가장 작은 양수의 표현가능한 수 1.0+esp != 1.0

#49
# np.set_printoptions(threshold = np.nan) # threshold = 한계, 임계점이 nan이므로
# Z = np.zeros((16,16))
# print(Z)

#50 vector에서 가장 가까운 값 찾기
# Z = np.arange(100)
# v = np.random.uniform(0,100)
# index = (np.abs(Z-v)).argmin() # 값의 차의 최솟값의 index
# print(Z[index])

#51 - 10개의 요소의 position과 color를 표현하는 행렬 만들기
# Z = np.zeros(10, [('position', [('x',float, 1),
#                                 ('y', float, 1)]),
#                   ('color', [('r', float, 1),
#                              ('g', float, 1),
#                              ('b', float, 1)] )] )
# print(Z)

#52
# i)
# Z = np.random.random((10,2))
# X,Y = np.atleast_2d(Z[:,0],Z[:,1]) # atleast : 이 함수의 input을 적어도 2dimension으로 나눔
# print(Z)
# print(X)
# print(Y)
# D = np.sqrt((X-X.T)**2 + (Y-Y.T)**2)
# print(D) # 10x10 행렬
# ii)
import scipy # much faster
import scipy.spatial
# M = np.random.random((10,2))
# L = scipy.spatial.distance.cdist(M,M)
# print(L)

#53
# Z = np.arange(10, dtype = np.float32)
# W = Z.astype(np.int32, copy = False)
# print(Z)
# print(W)

#54 - read following file
# from io import StringIO
# s = StringIO("""1,2,3,4,5\n6, , ,7,8\n , ,9,10,11\n""") # 그냥 space바는 -1을 의미
# Z = np.genfromtxt(s, delimiter=",", dtype = np.int) # txt를 행렬로 만들어줌 delimiter는 행렬 칸막이 역할
# print(Z)
# A = np.ones((3,5))
# B = A+Z
# print(B)

#55
# Z = np.arange(9).reshape(3,3)
#i)
# for index, value in np.ndenumerate(Z): # multi-dimensional index iterator input: array
#     print(index, value)
#ii)
# for index in np.ndindex(Z.shape): # N dimensional iterator to index array input : shape of array
#     print(index,Z[index])

#56 - generate a generic(포괄적인) 2D gaussian-like array
# X,Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10)) # meshgrid : 좌표벡터로 부터 좌표 행렬을 리턴
# print(X)
# print(Y)
# D = np.sqrt(X*X+Y*Y) # X와 Y사이 거리
# sigma, mu = 1.0,0.0 # mu:mean 평균, sigma**2:표준편차
# G = np.exp(-((D-mu)**2/(2.0*sigma**2))) # 이 식은 probability density(가우시안 분포) (exp = exponential)
# print(G)

#57
# n = 10
# p = 3
# Z = np.zeros((n,n))
# np.put(Z,np.random.choice(range(n*n),1,replace = False),p) #Z에 1개 자리를 랜덤하게 뽑아서 p를 넣는다
# print(Z)

#58
# X = np.random.random((5,10)) #rand(5,10)과 random((5,10))은 같은 것인가
# # print(X)
# Y = X - X.mean(axis=1, keepdims=True) # 최근 버전 넘파이
# Z = X - X.mean(axis=1).reshape(-1,1) # 옛날 버전 넘파이
# print(Y)
# print(Z)

#59 - n번쨰 column으로 sort an array
A = np.random.randint(0,3,(3,10)) # 0~3이전까지의 값중 랜덤, 사이즈는 3X10
print(A)
print(A[A[:,1].argsort()]) # argsort 소팅한 인덱스를 리턴 A[:,1]??

#60
B = np.random.randint(0,3,(3,10))
print((~B.any(axis=0)).any()) # any: iterable한 element의 어느 하나라도 참이면 True리턴

#61
C = np.random.uniform(0,1,10)
c = 0.5
m = C.flat[np.abs(C-c).argmin()] # np.ndarray.flat():
print(m)

#62 - A와 B를 iterator를 사용하여 더해라
D = np.arange(3).reshape(3,1)
E = np.arange(3).reshape(1,3)
it = np.nditer([D, E, None])
for x,y,z in it:
    z[...] = x+y
print(it.operands[2])

print("*****************************************************************")

#63 - name attribute가 있는 class를 만들어라
class NamedArray(np.ndarray):
    def __new__(cls, array, name = "no name"):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj
    def __array_finalize__(self,obj):
        if obj is None : return
        self.info = getattr(obj, 'name', "no name")
G = NamedArray(np.arange(10), "range_10")
print(G.name)

# 64 - 2nd 벡터로 indexed된 elementdp 1을 더하려면?
H = np.ones(10)
I = np.random.randint(0,len(H),20)
H += np.bincount(I, minlength=len(H)) # bincount: 최속밧부터 최댓값까지 숫자가 각 몇개씩있는지
print(H)
np.add.at(H,I,1)
print(H)

# 65 - accumulate(축적하다) 인덱스리스트 I를 바탕으로 행렬F 에서 벡터 X의 element를 축적하려면?
J = [1,2,3,4,5,6]
K = [1,3,9,3,4,1]
L = np.bincount(K,J)
print(L)

# 66 - wxhx3 이미지에 대해 dtype = ubyte unique color의 개수는?
w,h = 16,16
M = np.random.randint(0,2,(h,w,3)).astype(np.ubyte)
N = M[...,0]*256*256 + M[...,1]*256+M[...,2]
n = len(np.unique(N))
print(np.unique(M)) # unique한 원소를 리턴

# 67 - 4 dimensional array
O = np.random.randint(0,10,(3,4,3,4))
sum = O.sum(axis = (-2,-1))
print(sum)
sum = O.reshape(O.shape[:,2]+(-1,)).sum(axis=-1)
print(sum)

# 68 - 1 dimensional vector P ->P의 subset의 평균을 subset인덱스를 이용하여 같은 사이즈인 Q로 계산하라
#i)
p = np.random.uniform(0,1,100)
Q = np.random.randint(0,10,100)
P_sums = np.bincount(Q,weights = P)
P_counts = np.bicount(Q)
P_means = P_sums/P_counts
print(P_means)
#ii) pandas solution more intuitive
import pandas as pd
print(pd.Series(P).groupby(Q).mena())

# 69 - dot product의 diagonal을 구하라
R = np.random.uniform(0,1,(5,5))
S = np.random.uniform(0,1,(5,5))
#i)
np.diag(np.dot(R,S))
#ii)
np.sum(A*B.T, axis=1)
#iii)
np.einsum("ij,ji->i",A,B)