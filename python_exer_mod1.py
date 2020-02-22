# 모듈 : 함수나 변수, 클래스를 모아놓은 파이썬 파일이다
# module1.py = 파이썬 확장자인 .py로 만든 파이썬 파일은 모두 모듈이라고 할수 있다
import module1
print(module1.add_a(4487,152)) # 4639
# import는 이미 만들어놓은 파이썬 모듈을 사용할 수 있도록 만든 명령어잉다
# add_a(a,b)를 그냥 쓰면 안되고 앞에 반드시 module1.add_a()를 써야한다.
# module1은 모듈이름이다!
# 만약 add_a를 그냥 모둘없이 쓰고싶을떄는 from module1(모듈이름) import add_a(함수이름)
from module1 import add_a, sub_a
print(add_a(2,3))
# 혹은 from module1 import * 을 사용하면 모듈에 있는 모든 함수를 사용한다는 뜻
# *은 '모든 것'이라는 뜻이다

print(module1.PI)
q = module1.Math(2) # q는 클래스 Math의 객체
print(q.solv()) # 12.566368
print(module1.add_b(module1.PI,2))

# 다른 파일에서 모듈 불러오기

# 패키지란 무엇인가
#Package는 파이썬 모듈의 .로 이루어진 계층적 구조(디렉토리 구조)를 다룰수잇게해준다
# ex) a.b모듈 = a패키지의 b모듈이 된다
# Game/
#     __init__.py
#     Sound/
#         __init__.py
#         Wave.py
#         Echo.py
#     Graphic/
#         __init__.py
#         Rendering.py
#         Screen.py
#     Play/
#         __init__.py
#         Run.py
#         Test.py
# 게임, 사운드, 그래픽, 플레이는 디렉토리 이름
# 게임이 이 패키지의 루트 디렉토리이고 사운드, 그래픽, 플레이는 서브 디렉토리이다
# 확장자가 .py 인 애들은 파이썬 모듈이다

# eco.py 파일의 함수를 사용하기 위해서는 첫번째 방법
import game.sound.echo
game.sound.echo.echo_test()

# 두번째 방법
from game.sound import echo
echo.echo_test()

#세번째 방법
from game.sound.echo import echo_test
echo_test()

#import game
#game.sound.echo.echo_test() 는 불가능하다
#import game을 하면 game에잇는 모듈만 사용가능하거나 게임 디렉토리의 __init__.py에 정의하는 것만 사용가능하다
#import game.sound.echo.echo_test() 도 불가
#도트연산자.을 사용해서 import를 할때 디렉토리의 맨마지막은 항상 패키지나 모듈이어야한다

#__init__.py 파일은 해당 디렉토리가  패키지에 포함됨을 알려주는 역할
# 즉,게임,사운드,그래픽등의 패키지에 포함된 디렉토리안에 이닛 폴더가 없다면 그것을 패키지로 인식하지 못한다