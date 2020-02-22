# def : 함수를 만들 때 사용하는 예약어
# 함수 이름뒤에 괄호안의 값은 인풋!
def add(a,b):
    return a+b
# c= add(23,4)
# print(c)

# 매개변수(parameter)와 인수(argument)
# 위의 add함수에서 a,b는 매개변수 -> 함수에서 입력된 실제값을 받는 변수
# 23,4는 인수 -> 함수를 호출할때 전달하는 실제입력값

# 함수는 입력값과 결과값의 존재유무에 따라 4가지 유형으로 나뉜다.
# 1) def 함수이름(매개변수):
#     ...
#     return 결과값 # 일반 함수의 전형적인 예
# 2) 입력값이 없는 함수
# def say():
#     return 'Hello'
# aa = say()
# print(aa) # Hello
# 3) 결과값이 없는 함수 -> return 하는 값은 없어도 프린트를 하기는 한다.
# 프린트는 수행할 함수의 문장중 하나이지 결과값을 나타내지는 않는다
# 결과는 오직 return으로만 받을수 있다
# def add1(a,b):
#     print("Fucking Rick and morty!")
# add1(34,66) # Fucking Rick and morty!

# 4) 입력값도 결과값도 없는 함수
# def say1():
#     print("Hello pinn the human and jake the dog?")
# say1() # Hello pinn the human and jake the dog?

# 매개변수를 지정해서 호출하여 보자! -> 위의 add 함수를 이용
result = add(b = 19, a=37) # 이때는 매개변수의 순서가 상관없다!
print(result)

# 입력값이 여러개이고 몇개일지 모르는 상황일때는
# 예를 들면 사용자가 원하는 입력값을 모두 더해주는 함수 : input값에 (*매개변수)라고 표현하면 된다!
def add_many(*args): # 이렇게 *매개변수는 입력값을 전부모아 튜플로 만들어주기 때문에 좋다
    result = 0       # args는 임의로 정한 argument의 약자로 관례적으로 자주 사용한다
    for i in args:   # 꼭 args를 사용하지 않고 *python, *ele 이런 거도 괜찮다.
        result += i
    return result
d = add_many(13,32,86,5,65,44,93)
print(d) # 338

def add_mul(choice, *args):
    if choice == 'add':
        res = 0
        for i in args:
            res += i
    elif choice =='mul':
        res = 1
        for i in args:
            res *= i
    return res
res = add_mul('mul',32,33,4,2,17) # 143616
print(res)

# 키워드 파라미터 : **kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1) # {'a': 1}
print_kwargs(name='Rick',age='102') # {'name': 'Rick', 'age': '102'}
# 이런 식으로 모두 딕셔너리 꼴로 만들어져서 출력됨

# 함수의 결과값은 언제나 1개이다!!!
def addmul(a,b):
    return a+b, a*b
print(addmul(13,4)) # 결과값은 2개지만 이를 묶어서 튜플값으로 돌려준다
# 하지만 튜플값을 두개의 값으로 받고싶다면
res1, res2 = addmul(b=8, a= 3)
print(res1, res2) # res1 = 11, res2 = 24
# def addmul(a,b) # 이런식으로 한다면 어떨까?
#     return a+b # 처음에 이렇게 리턴한다면 여기서 함수가 끝나고
#     return a*b #  뒤의 리턴은 동작을안한다

# 매개변수에 초깃값을 미리 설정하기!
def say_interest(name, age, female = True): # 매개변수에서 female은 초기화되어있다
    print("my namen is ",name,".")     # 초기화를 해야하는 매개변수는 항상 맨뒤에 놓는다!!
    print("my age is ",age,".")
    print(""""Rick and Morty,
    Adventure time: pinn and jake
    Crystal germ : Steven Universe
    We bear bears
    MARBLE : Agent of S.H.E.I.L.D
    """)
    if female ==True:
        print("I'm a woman")
    else:
        print("i'm a man")
say_interest('Doyeon', 24, False)

# 함수안에서 선언한 변수의 효력범위
# 함수 안에있는 변수는 함수 안에서만 사용되고 함수밖에서는 따로 불러올수 없다!

# 함수 안에서 함수 밖에 있는 변수를 변경하는 방법
def vartest(a):
    a+=1
    return a
#vartest 함수를 사용하서 함수 밖의 변수a를 1만큼 증가시키기
# 1) return 사용
a =1
a = vartest(a)
print(a)

# 2) global 변수를 이용해서 명령어 사용하기
aa = 13
# def vartest1():
#     global aa #  프로그래밍시에 글로벌변수를 사용하는것은 좋지 않다!
#               함수는 글로벌변수를 포함하지 않는 독립적인 상태가 좋다
#               외부변수에 종속적인 함수는 좋지않다
#     aa+=1
# vartest1()
# print(aa) # 14

# lambda : 함수를 생성할 때 사용하는 예약어 def과 비슷한 역할
# 보통 함수를 한줄로 단순하게 만들거나 def를 쓸수 없을때 사용

mul = lambda a,b : a*b # 람다로 만든 함수는 따로 리턴을 하지 않아도 리턴이 된다
resu = mul(12,7)
print(resu)

print("************************************************************************")

# 사용자의 입력과 출력
#1. 사용자가 입력한 값을 어떤 변수에 대입하고 싶을때
# s = input() # input 함수 사용하기
# print(s)
# 프롬프트를 띄워서 사용자 입력받기
# 프롬프트를 띄운다는것은 예를들면,"숫자를 입력하세요" 이런 명령어가 나오는 것
# num = input("숫자를 입력하세요")
# print(num)

# print 자세히 알기
# print("I""love""You") # 이것과 아래는 동일하게 콘캣해서 프린트한다
# print("I"+"love"+"U")
# print("I","love","you") # ,가 문자열 사이에 있으면 띄어쓰기

# 한줄에 결과값을 전부 출력하기
# for i in range(0,12): # 0 1 2 3 4 5 6 7 8 9 10 11
#     print(i,end=' ') # print에서 end는 출력할 요소끝에 원하는 끝문자를 설정할 수 있다

# print("************************************************************************")

# 파일 읽고 쓰기 :파일을 통한 입출력 방법
f = open("new.txt",'w') # 프로그램을 실행한 디렉토리에 새로운 파일이 생김! w= write쓰기모드
f.close() # f는 파일 객체
# 파일 열기의 모드에는 여러가지가 있다.
# 1. r : 읽기모드, 파일을 읽기만 함
# 2. w : 쓰기모드 , 파일에 내용을 씀 -> 해당파일이 이미 존재할경우 쓰기모드로 열면 원래있던 내용이 다 사라진다
# 3. a : 추가모드 , 파일의 마지막에 새로운 내용 추가(수정?)

# 파일을 쓰기모드로 열어 출력값 적기
# fff = open("r.txt", 'w')
# for i in range(1,11):
#     data = "%d번쨰 줄입니다" %i
#     fff.write(data) # 메모장에 출력
#     print(data) # 프롬프트에 출력
# f.close()

# with 문과 함께 사용하기
# f = open("foo.txt",'w')
# f.write("rick and morty")
# f.close()

# with open("foo.txt",'w') as f: # open한 파일을 자동으로 닫을 수 있따.
#     f.write("rick and morty")

# sys 모듈로 매개변수 주기
# ex) C;/type a.txt : type 바로 뒤에 파일이름을 인수로 받아 내용을 출력하는 명령 프롬프트 멸령어
# import sys # sys모듈을 사용하여 파이썬에서 매개변수를 직접 주어 프로그램 실

#1
def is_odd(a):
    if a%2 == 0:
        print("even")
    else:
        print("odd")
is_odd(13)
#2
def mean(*args):
    total = 0
    for i in args:
        total += i
    return total/len(args)
print(mean(18,21,43,23,17))

#3
input1 = input("첫번째 숫자를 입력하세요")
input2 = input("두번째 숫자를 입력하세요")

total1 = int(input1) + int(input2)
print("두 수의 합은 ",total1,"입니다")

# 4. 3번
print("".join(["you","need","python"]))
# 5.
f1 = open("text.txt",'w')
f1.write("life is too short")
f1.close() # 메모장을 닫지 않으면 read할때 프린트가 되지 않는다
f2 = open("test.txt",'r')
print(f2.read())
f2.close()

#with 구문
with open("test.txt",'w') as f1:
    f1.write("life is too short")

with open("test.txt",'r') as f2:
    print(f2.read())

# 6
aa = input("저장할 내용:")
f = open("test.txt",'a')
f.write(aa)
f.write("\n")
f.close()

#7
f3 = open("text.txt",'w')
f3.write("Life is too short")
f3.write("\n")
f3.write("you need java")
f3.close

f4 = open("test.txt",'r')
body = f4.read()
f4.close()

body = body.replace('java','python')
f5 = open("test.txt",'w')
f5.write(body)
f5.close()

#####################################
#5장. 파이썬 날개달기 - 파이썬의 꽃
# 클래스 : 코딩의 필수요소는 아님. class a가 있고 a로 만든 cal1 cal2가 있으면
# 이 cal1과2는 객체라고 부른다 즉, 과자틀은 클래스, 그걸로 만든 과자는 객체
# 동일한 클래스로 만든 객체들은 서로 영향을 전혀 주지않는다
# class cookie:라고 하면 a=cookie()라고 선언하면 된다

# 객체(object)와 인스턴스(instance) 차이!
# 그런데 클래스로 만든 객체를 인스턴스라고도 한다. a는 객체.
# 인스턴스라는 말은 특정 객체 a가 어떤 클래스의 객체인지 관계를 위주로 설명할때 사용

# 사칙연산 클래스 만들기
# 클래스를 무작정 만들지 말구 클래스로 만든 객체를 중심으로 어떤식으로 동작할 것인지 구상
class cc:
    pass
s=cc()
type(s)

class Fourcal:
    def setdata(self,fir,sec): # 클래스안에 구현된 함수는 다른 단어로 method메소드라고 한다
        self.fir = fir # setdata 메소드의 수행문
        self.sec = sec
                        # setdata 메소드는 매개변수로 self, fir, sec 3개를 받는다
                        # 하지만 실제로 setdta메소드가 받는 변수는 2개!
                        # self는 나중에 a.setdata(2,4)에서 a를 담당한다
                        # 즉, self는 setdat메소드를 호출한 객체a 가 자동으로 전달된다

# 생성자 Constructor : 객체에 초기값을 설정해야할 때, 생성자를 구현한다.
# 생성자는 객체가 생성될때 자동으로 호출되는 메소드를 의미한다.
# __init__ 을 이용하면 이 메소드는 생성자가 된다
    def __init__(self,fir,sec): # 얘는 setdata와 이름만 다르고 모두 같다
        self.fir = fir          # 단, 매소드 이름이 __init__이므로 객체를 만들때 자동으로 호출된다
        self.sec = sec          # 그러면 a=Fourcal(), a.setdata(4,2)이라고 할 필요없이 a = Fourcal(4,2)라고하면 됨

    def add(self):
        result = self.fir+self.sec
        return result

    def sub(self):
        result = self.fir-self.sec
        return result
    def mul(self):
        result = self.fir*self.sec
        return result
    def div(self):
        result = self.fir/self.sec
        return result

# aa = Fourcal()
# aa.setdata(4,3)
# print(aa.add())

# 클래스의 상속(Inheritance) : '물려받다'
# = 어떤 클래스를 만들때 다른 클래스의 기능을 물려받을수 있도록 하는 상속의 기능이 있다
# '상속'을 이용해 m^n을 구현해보쟈
class Morecal(Fourcal): # 이런식으로 상속할 클래스를 괄호안에 넣는다
                        # = More은 Fourcal클래스의 모든 메소드를 사용할 수 있어야한다.
    def pow(self):
        result = self.fir ** self.sec # **이 제곱 = fir^sec
        return result

# 메소드 오버라이딩(overriding):덮어쓰기
class safe(Fourcal):
    def div(self): # 이렇게 부모클래스에 있는 함수를 동일한 이름으로 덧씌워서 만들때 오버라이딩이라한다.
        if self.sec ==0:
            return 0
        else:
            return self.fir/self.sec

        # 클래스 변수 : 객체 변수와는 성질이 다름
        # 객체변수는 다른객체에 영향을 받지않고 그 값을 유지
class Family:
    last_name = 'kim' # 클래스 변수 : 같은 클래스를 가진 객체들이 공유하는 변수
print(Family.last_name)

a = Family()
b = Family()
print(id(a.last_name))
print(id(b.last_name))