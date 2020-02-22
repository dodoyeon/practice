def add_a(a,b):
    return a+b
def sub_a(a,b):
    return a-b

#if 모듈1에 프린트를 추가하면? import를 하는순간 프린트를 해버린다
# print(add_a(1,4))
# print(sub_a(4,1))

# 그러므로
if __name__ == "__main__":  #을 사용하면 이 module1.py를 실행할때만 실행되고
    print(add_a(1,4))       #다른 파일에서 import로 부를때는 if다음 문장이 실행되지 않는다
    print(sub_a(4,1))

# __name__변수란? 파이썬이 내부적으로 사용하는 특별한 변수이름
# 만약 module1.py 파일을 실행시키면 __name__변수에는 __main__값이 저장된다
# 하지만 다른 파이썬 모듈(파일)에서 import로 실행하면 __name__변수에 module1.py의 모듈이름값 module1이 저장된다

# 클래스나 변수를 포함한 모듈
PI = 3.141592
e = 2.718281

class Math:
    def __init__(self,r):
        self.r =r

    def solv(self):
        return PI*(self.r**2)

    def sols(self):
        return PI*2*self.r

def add_b(a,b):
    result = a+b
    return result