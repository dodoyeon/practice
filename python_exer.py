# ***01장***
# 1. ex) if 4 in [1,2,3,4]: print("there is 4") = [1,2,3,4]중에 4가 있다면 문장을 출력한다라는 뜻
# -> 파이썬은 인간이 이해하기 쉬운 문법을 가진다.
# 2. 파이썬은 오픈소스 (open source) : 저작권자가 소스코드를 공개하여 자유롭게 사용,복제,배포,수정 할수 있는 소프트웨어
# 개발 속도가 빠르고 간결 등의 장점이 있다...

# 파이썬으로 할 수 있는 일
# 1. 시스템 유틸리티(컴퓨터 사용에 도움되는 소프트웨어) 제작
# 2. GUI(Graphic User Interface) -> 화면에 프로그램 동작을 할수 있도록 메뉴나 버튼을 만드는 것
# 3. C나 C++과 결합가능 (빠르게 실행해야 하는것을 C로 구현)
#     * C와 C++ 의 차이점
# 4. 웹프로그래밍 : 게시판이나 방명록 프로그램을 만드는 것
# 5. 수치연산 프로그래밍 : Numpy
#     * Numpy : 파이썬의 수치해석용 라이브러리
#         다차원 행렬 자료구조인 ndarray(list 자료구조)를 기반으로 선형대수 연산에 사용
# 6. 그 외 데이터베이스 프로그래밍, IoT등

# ***02장*** : python 자료형
# 1. 숫자형
# (1) 정수형 integer : 양의 정수, 음의 정수, 0
a = 123
b = -178
c = 0
print(a,b,c)
# (2) 실수형 floating point : 소수점 포함
d= 1.2
e = 4.24E10 # 4.24*10^10
f = 4.24e-10 # 4.24*10^-10
print(d, e, f)
# (3) 8진수(octal)와 16진수(hexadecimal)
#     - 8진수는
g = 0o177
    # -16진수는
h = 0x8ff
i = 0xABC
print(g,h,i)

print("**********************************")
# (4) 숫자형을 활용한 연산자 : 사칙연산
print(a+b)
print(a*b)
print(a/b)
print(a**4) # a^4제곱
print(a%9) # 나눗셈 후 나머지를 반환하는 연산자
print(7/4) # 1.75 소수로 되어있다
print(7//4) # 몫을 반환
print("**********************************")

# 문자열이란 string 문자, 단어 등으로 구성된 집합  "You live only once" 같은 큰따옴표로 이루어짐
# "123"이언 애도 문자열 , 'These' 이런 작은 따옴표도 문자열, """It's too noisy"""나 '''Jonna noisy'''
# 이런 식으로 큰 따옴표나 작은 따옴표를 3개 연속으로 써도 문자열이다.
# 왜 이렇게 4가지 방법이나 생겼을까?
# 1. 문자열 안에 작은따옴표 포함되는 때, 예: python's function
# 이런 경우는 문자열로 만들기 위해서는 큰따옴표를 사용해야함 -> "python's function"
# 2. 문자열 안에 큰 따옴표가 필요할 경우 예: "It is hot" he says.
# 같은 경우 문자열을 작은 따옴표로 감싼다. -> '"It is hot" he says.'
food = 'My favorite food is garnet.'
# food = '"It is hot" he says.'
print(food)

# 3. 백슬레시(\)를 사용해서 작은 따옴표와 큰따옵표를 문자열에 포함시키기
# 백슬래시를 문자열안에 사용되는 작은 따옴표나 큰따옴표 앞에 삽입하면 기호가 아니라 문자로 인식된다
mug = 'Doyeon\'s cup is broken' # 백슬래시를 따옴표 앞에 표기한다.
fuck = "\"I want my diamond.\" he said."

# 여러줄인 문자열을 변수에 대입하고 싶을 때 (한줄로 길게가 아니라)
mumu = "I don't want to die.\nI need that potion." # 1. 엔터를 치는 역할 \n:escape code
# 2. 혹은 작은 따옴표나 큰따옴표 3개씩 사용하기도 한다. 이 방법이 더 깔끔.
lime= '''
Rose is red.
blue os water.
          '''
ooo = """
I really want to buy it....
I'm so sad.
"""
## 이스케이프 코드란?
#\n 얘를 포함한 다양한 백슬래시+문자 : 프로그래밍시 미리 정의해둔 문자 조합
# \n : 문자열 안에서 줄을 바꿀때 엔터할때 사용 *(많이 사용)
# \t : 문자열 사이에 탭 간격을 줄때 *
# \\ : 문자 \를 문자열내에서 그대로 사용할때 *
# \' : 작은 따옴표 표현을 문자열 안에서 그대로 사용할때 *
# \" : 큰 따옴표 표현을 문자열 안에서 그대로 사용할때 *
# \r : 캐리지 리턴 -> 줄바꿈 문자, 현재 커서를 가장 앞으로 이동
# \f : 폼피드-> 줄바꿈 문자, 현재 커서를 다음 줄로 이동
# \a : 출력할때 스피커에서 삑소리가 난다.
# \b : 백스페이스
# \000 : NULL문자

## 문자열 연산하기
# 문자열 더하기: concatenation
head = 'Python'
tail = ' is snack.'
print(head + tail) # python is snack.

# 문자열 곱하기
a = "python"
print(a*2)
# 곱하기 응용
print("="*50)
print("my program")
print("="*50)

# 문자열 길이 구하기
noy = "Hello, i'ts me. I was wondering if afterall this year means nothing"
print(len(noy))

# 문자열 인덱싱과 슬라이싱
# indexing  : 문자에서 한글자마다 인덱스 숫자(0부터 시작)를 붙이는 것
print(noy[19])
print(noy[-1]) # 인덱스에서 마이너스 값은 거꾸로 세기위해서이다.
               # -1 index는 맨마지막 문자를 이야기 한다.

# slicing : 문자열에서 단어만 뽑아내는 방법
# 인덱싱과 슬라이싱기법은 리스트나 튜플에서도 사용가능
print(noy[0:5]) # noy 문자열에서 인덱스번호 0-4까지 뽑아낼 수 있다. 마지막 번호인 5는 포함안됨
print(noy[3:19])
print(noy[23:]) # 끝번호를 생략하면 그 번호부터 끝까지 출력한다.
print(noy[:]) # 시작번호와 끝번호 둘다 생략하면 문자열의 처음부터 끝까지 출력
print(noy[29:-8]) # -8까지라고 쓰면 -9까지 출력된다.
print("********************************************************************")

# 슬라이싱으로 문자열 나누기
mym = "20200101Happy fucking new year"
date = mym[:8]
mess = mym[8:]
print(date)
print(mess) # 두부분으로 자르기
year = mym[:4]
day = mym[4:8]
message = mym[8:] # 세부분으로 자르기
print(year)
print(day)
print(message)

# pithon을 python으로 바꾸려면
nym = "Pithon"
# nym[1] = "y" -> 이렇게 바꾸면 오류가 발생한다. 문자열 자료형의 요소 값은 바꿀수 없다.
P = nym[:1]
t = nym[2:]
print(P+'y'+t) # 이렇게 바꿀수 있다.(새롭게 만드는거나 마찬가지)

# 문자열 포매팅(Formatting) : 문자열안에 특정한 값만 바꾸면 될때 사용-> 문자열안에 어떤 값을 삽입함
me = "I ate %d apples!" % 3 # 여기서 %d나 %s 는 포맷코드
# I ate 3 apples!
ne = "I want %s illustration book! The art of ooo and disease" % "two"
# I want two illustration book! The art of ooo and disease
number =2;
ve = "I want %d vouchers" %number
# I want 2 vouchers

# 2개 이상 값넣기
num = 10
day = "three"
ce = "I waited %d illustration books for %s days" % (num, day)
# I waited 10 illustration books for three days

# 문자열 포맷 코드
# %s ->string (문자열) / %c -> character(글자 한개) / %d -> integer(정수) / %f -> floating point(부동소수점) /  %% -> Literal %(문자 % 자체) 뭔말?
# %s fomat code special
se = "I have %s apples" %3 # 원래 부동소수점은 f고 정수는 d지만 %s는 그런거 생각안해도 된다.
# I have 3 apples
we = "The rate is %s" % 3.234
# The rate is 3.234

#만약 문자열에서 퍼센트를 출력해야하는 상황이 오면 %가 아니라 %%를 사용해야 한다.
qe = "Error is %d%%" % 98
# Error is 98%

# 포맷코드와 숫자 합께 사용하기
# 1. 정렬과 공백
re = "%10s" % "hi" # 전체 길이가 10인 문자열공간에서 대입값을 오른쪽에 배치하라는 의미
#         hi
le = "%-10s 05" % "bye" # 왼쪽에 대입
# bye        05

# 긴 소수르 ㄹ네번째 자리까지만 사용하는 경우
te = "%10.4f" % 3.42123458606645
#     3.42

# 포맷 함수를 사용한 포매팅
" I want {0} books".format(3) # I want 3 books
"I ate my {0} diamonds".format("five") # I ate my five diamonds.
numb = 108
fe = "Do you want to build {0} babilon tower?".format(numb) # Do you want to build 108 babilon tower?
days = 5
ge = "I ate {0} bananas so I was sick for {1} days".format(numb, days) # I ate 108 bananas so I was sick for 5 days -> 2개 이상 값 넣기

he = "you are fucking {number} aliens. and I'm sick of caring you guys for {days} days!".format(number = 20, days = 4) # {0},{1}같은 인덱스 항목도 쓸수 있지마 ㄴname으로 쓰면 더 편하다.
# you are fucking 20 aliens. and I'm sick of caring you guys for 4 days!
je = "you are fucking {0} aliens. and I'm sick of caring you guys for {days} days!".format(3, days = 7) # 인덱스와 name 혼용가능
# you are fucking 3 aliens. and I'm sick of caring you guys for 7 days!

# 왼쪽 정렬 :<10을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다
be = "What the {0:<10} fucking python".format("good") # What the good       fucking python
# 오른 쪽 정렬
de = "What the {0:>10} fucking python".format("good") # What the       good fucking python
# 가운데 정렬
ke =  "What the {0:^10} fucking python".format("good") # What the    good    fucking python

# 공백 채우기
ue = "ill{0:=^10}lli".format("hih") # ill===hih====lli
pe = "***{0:!>10}***".format("hey") # ***!!!!!!!hey***

# 소수점 표현하기
w = 5.483276392
oe = "{0:0.4f}".format(w) # 5.4833 -> 반올림

# { 이나 }를 문자로 표현하기
ie = "I'd like to draw {{ and }} when I was young".format() # .format()은 포맷의 의미가 없는거 아닌가??
# I'd like to draw { and } when I was young
tt = "{}" # 얘도 되넹....

# f 문자열 포매팅 -> python3.7버전부터 사용가능-> 안할래

print("******************************************************")
# 문자열 관련 함수들 -> 문자열 자료형에 내장되어 있는 함수
# 문자열 변수 뒤에.을 붙이고 함수이름을 쓰면된다
# 1. 문자 개수 세기 count
aa = "hobby"
# print(aa.count('b')) # 2 문자열안에서 특정 글자의 개수를 알려준다
# 2. 위치 알려주기1 find
bb = "Fuck you bitch, I really hope we never gonna see each other again."
# print(bb.find('b')) # 9-> 문자열 안에서 b가 처음나온 인덱스 출력
# 3. 위치 알려주기2 index
print(bb.index('t')) # 11(띄어쓰기 포함) 똑같이 문자열안에서 처음나온 인덱스 출력

# 4. 문자열 삽입 join
# print("/".join(bb)) # F/u/c/k/ /y/o/u/ /b/i/t/c/h/,/ /I/ /r/e/a/l/l/y/ /h/o/p/e/ /w/e/ /n/e/v/e/r/ /g/o/n/n/a/ /s/e/e/ /e/a/c/h/ /o/t/h/e/r/ /a/g/a/i/n/.
# 문자열 안의 모든 문자 사이에 /를 삽입한다.

# 5. 소문자를 대문자로 바꾸기 upper
print(aa.upper())
# 6. 대문자를 소문자로 바꾸기 lower
cc = "WHAT THE FUCK!"
print(cc.lower())

# 7. 욉쪽 공백 지우기 lstrip
dd ="   mumu   "
print(dd.lstrip()) #mumu   /
# 8. 오른쪽 공백 지우기 rstrip
print(dd.rstrip()) #   mumu/
# 9. 양쪽 공백 지우기 strip
print(dd.strip()) #mumu/

# 10. 문자열 바꾸기 replace
print(bb.replace("Fuck","Love")) # Love you bitch, I really hope we never gonna see each other again.
# fuck를 love로 바꿨다

# 11. 문자열 나누기 split
print(bb.split()) # ['Fuck', 'you', 'bitch,', 'I', 'really', 'hope', 'we', 'never', 'gonna', 'see', 'each', 'other', 'again.'] -> 괄호안에 아무것도 없으면 띄어쓰기 기준으로 단어를 나눔
ee = "a:s:d:f:r"
print(ee.split(':')) # ['a', 's', 'd', 'f', 'r'] -> 괄호안에 특정 값이 있으면 그것을 구분자로 사용