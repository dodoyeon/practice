## 프로그램의 구조를 쌓는다. : 제어문
# money = True
# if money :
#     print("Taxi")
# else: # else문은 if문 없이 독립적으로 사용할 수 없다
#     print("Walk")


# 조건문 뒤에는 : 을 꼭 붙여야 한다.
# 들여쓰기를 할때는 스페아스바 4개! 혹은 탭
# 조건문 : 참과 거짓을 판단하는 문장
# 비교연산자
# x != y -> x는 y와 같지않다
x = 8
y = 4
print(x>=y) # True
# 만약 3000원 이상ㅇ의 돈을 가지고 있으면 택시를 타고 아니면 걸어가라
cash = 1000
card = 10 # 참이다
# if cash>=3000 or card: # card가 참일때
#     print("taxi")
# else:
#     print("walk")
# x or y : x와 y 둘중 하나만 참이면 참이다
# x and y : x와 y 둘다 참이어야 참이다
# not x : x가 거짓이면 참이다

# x in s : 여기서 s는 리스트, 튜플, 문자열이 될 수 있다
# x not in s :
# s = 5
# print(s in [1,3,4,5,6,7]) # True
# print(s not in ('a','c','w',5)) # False

# 주머니에 돈이 있으면 택시를 타고 아니면 타지말아라.
# pocket = ['Rick and morty', 'wallet', 'smartphone']
# if 'money' in pocket:
#     # pass
#     print("Taxi")
# elif 'wallet' in pocket:
#     print("Bus")
# else :
#     print("walk")

#  조건문에서 아무것도 하지않고 싶을때 :  pass를 적용가능 그냥 조건이 적용되는 칸에 다른 문 안쓰면 패쓰된다
# elif는 else if와 같다 // 다중조건판단

# while문 : 반복문이라고도 한다
# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1 # treeHit+=1와 같다
#     print("나무를", treeHit, "번 찍었습니다")
#     if treeHit == 10:
#         print("나무가 넘어갑니다")

# treehit = 0;
# while treehit < 10:
#     treehit +=1
#     print("나무를", treehit, '번 찍었습니다.')
#     if treehit == 10:
#         print("나무를 처치했습니다 +1")

# prac = """
# 1. Add
# 2. delete
# 3.list
# 4.quit
#
# enter the number: """
# number = 0
# a = 31
# b = 86
# while number != 4:
#     print(prac)
#     number = int(input())
#     if number == 1:
#         print(a + b)
#         break
#     elif number == 2:
#         print("Delete")
#         break
#     elif number == 3:
#         list = [a, b]
#         print(list.sort())
#         break

# while 강제로 빠져나가기 = break
# money_ = 300
coffee = 10
# while coffee:
#     # if coffee != 0 :
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee - 1
#     print("남은 커피의 개수는",coffee,"개 입니다.")
#     # else
#     if coffee == 0:
#         print("썩 꺼지십시오")
#         break
# #
# while True:  # 이건 뭐지? -> 무한루프
#     money = int(input("돈을 넣어 주세요 : "))
#     if money == 300:
#         print("순순히 커피를 줍니다")
#         coffee = coffee - 1
#     elif money > 300:
#         change = money - 300
#         print("커피와 잔돈", change,"를 줍니다")
#         coffee = coffee - 1
#     else :
#         print("썩꺼져")
#         break
#     if coffee == 0:
#         print("커피의 재고가 모두 소진되었습니다")
#         break

# while문 맨 첫번째로 되돌아가기 = continue 문
# 1-10까지 숫자중 홀수만 출력하도록 한다.

# num = 0
# while num < 10:
#     num = num + 1  # num이 10보다 작은동안은 계속 num이 커진다.
#     if num % 2 == 0: continue  # num이 짝수이면 그냥 통과하고 바로 다시 while문 처음으로 돌아간다!!
#     # 왠지 여기있어야할거 같은데?? -> 아니다.
#     print(num)

# 무한루프 loop는 방금 본 while True 는 무한 루프의 기본꼴이다.

# while True:
#     print("ctrl+c를 눌러야 빠져나갈수 있습니다.")
# #

# # for 문 : 리스트, 튜플, 문자열의 첫번째 부터 마지막 원소까지 차례로
# # 변수에 대입되어 수행되어야할 코드가 수행된다. for 변수 in 리스트 :
# test = ['one', 'two', 'three']
# for i in test:
#     print(i)
# #
# # 다양한 포문 사용하기
# la = [(9, 2), (3, 4), (6, 7)]
# for (first, second) in la:
#     print(first + second)
#
# # 응용 : 밑에꺼는 딕셔너리 스타일로 하고싶었는데 생각해보니 포 문은 딕셔너리는 사용불가!!
# # class = {('rick',100),('blossum',90),('finn',35),('colson',65),('otis',45)}
# #
# # for (name,score) in class:
# #     if 'rick'
# #     print()
#
# # 응용2
marks = [100, 90, 35, 65, 45]
# numb = 0
# for mark in marks:
#     numb += 1
#     if mark >= 60:
#         print(numb, " 합격")
#     else:
#         print(numb, " 불합격")

# # 응용3 :격 혹은 불합격이면 아예 메세지를 보내ㅐ지 않도록
# numb = 0
# for marking in marks:
#     numb += 1
#     if marking < 60:
#         continue
#     else: print("합")

# for문과 같이 다니는 range 함수  -> 숫자리스트를 자동으로 만들어주는 함수이다
# aa = range(10) -> aa는 range(0,10)
# range에서 시작과 끝 숫자를 지정하려면 range(시작, 끝 숫자)

add = 0;
for i in range(1, 11):
    print(i)
    add += 13
print(add)
#
# # 위의 예제도 range함수로 바꿀수 있다.
# num = 0
# for score in range(len(marks)):
#     num +=1
#     if marks[score] >=60:
#         print(num,"번 학생 합격을 축하합니다")
#     else:
#         continue

# for와 range르 이용한 구구단
# for i in range(1,10): # range(1,10) 이면 1-9 까지라는 뜻!
#     for j in range(1,10):
#         print(i*j, end = " ") # 프린트 함수에서 매개변수 end는 결과값을 다음줄로 출력하지 않고 그줄에 계속 출력
#     print("\n")

# 리스트 내포 (List comprehension)사용하기
# aa = [1,3,4,5]
result = []
# for i in aa:
#     result.append(i*3)
# print(result) # [3, 9, 12, 15] # 곱해져서 그대로 다른 리스트에 들어감

# result = [i*3 for i in aa if i%2 == 1] # if 조건을 만족한다면 for 문에 대해 행한다.
# print(result) # [3, 9, 15]             # 조건에 만족하지 않는다면 result안에 들어가지도 않는다

# result = [x*y for x in range(1,10)
#               for y in range(1,10)]
# print(result)