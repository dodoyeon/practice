# LIST : 숫자나 글자의 집합 // 꼴 : list이름 = [element1, element2, element3, ...]
# a = [1,3,5,7] / g = [] / i = ['life', 'is', 'short'] / u = ['germ', 'sapire', '8', '27'] / n = [1, 2, ['low', 'high', 'med']](리스트 자체를 요솟값으로 가짐)
# 리스트는 어떤 자료형도 요솟값으로 가질 수 있다.
# 비어있는 리스트는 d = list() 로 만들수 있다.

# 리스트의 인덱싱 indexing
a = [1,3,5,7,45,38,56]
# print(a[0]) # 1
# print(a[1]+a[3]) # 3+7 =10
# print(a[-1]) # 7 : 리스트에서 맨마지막 요소

n = [19, 26, ['low', 'high', 'med']]
# print(n[-1]) # ['low', 'high', 'med']
# 리스트의 리스트에서의 값을 출력하려면?
print(n[-1][0]) # low
# 삼중 리스트 -> 리스트를 중첩해서 쓰면 혼돈
m = [1,4,['f', 'k', ['ruby', 'quats', 'pearl']]] # pearl
print(m[-1][-1][2])

# 리스트의 슬라이싱 slicing
print(a[0:2]) # [1, 3]
print(a[:4]) # [1, 3, 5, 7]
print(a[3:]) # [7, 45, 38, 56] -> 문자열이랑 똑같다

# 중첩된 리시트에서 슬라이싱 하기
v = [1, 4, ['ruby', 'quats', 'pearl'], 15, 32, 47]
print(v[2][:2]) # ['ruby', 'quats']
print(v[1:][:2]) # [4, ['ruby', 'quats', 'pearl']] <- 펄도 들어간다...

# 리스트 연산하기
aa = [1,2,3]
bb = [6,8,9]
print(aa+bb) # [1, 2, 3, 6, 8, 9]

# 리스트 반복
print(aa*4) # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 길이 구하기
print(len(aa))  # 3

# 리스트 연산 오류
#"3hi"를 표현하기 위해 aa[2] + "hi" 이렇게 하면 안된다.
print(str(aa[2]) + "hi") # 이렇게 리스트의 element를 string으로 바꿔야한다.

# 리스트에서 값을 수정
aa[1] = 18
print(aa) # [1, 18, 3]

# 리스트에서 값을 삭제하기 : del
del(aa[1:])
print(aa)

# 리스트 관련 함수 : 문자열과 같이 리스트이름.함수 하여 리스트 관련 함수를 사용할 수 있다
# 1. 리스트에 맨마지막에 element 추가
aa.append(21)
aa.append(18)
aa.append(8)
aa.append(45)
# aa.append([3,45,16]) # aa.append(['ce', 'thw', 'ui'])#는 출력이 안된다 왜?
#  print(aa) # [1, 21, 18, 8, 45, [3, 45, 16]]

# 2. 리스트 정렬(sort)
aa.sort()
print(aa) # [1, 8, 18, 21, 45] -> 리스트안에 리스트가 있으면 sort가 안된다
# s = ['thw','ui', 'de','fuck']
# s.sort()
# print(s) # ['de', 'fuck', 'thw', 'ui']
ss = ['t','u', 'd','f']
ss.sort()
print(ss) # ['d', 'f', 't', 'u']

# 3. 리스트 뒤집기(reverse) : 역순으로 정렬하는것이 아니라 현재 리스트의 순서를 뒤집는다.
aa.reverse()
print(aa)

# 4. 위치(index) 반환 : 리스트에서 x 값이 있으면 x의 위치(인덱스)를 리턴한다.
print(aa.index(8))

# 5. 리스트에 요소삽입 (insert) : 리스트의 a번째 위치에 b를 삽입
aa.insert(3,17)
print(aa) # [45, 21, 18, 17, 8, 1]

# 6. 리스트 요소 제거(remove) : 리스트에서 첫번째 x element를 삭제하는 함수
aa.remove(1)
print(aa) # [45, 21, 18, 17, 8]

# 7. pop : 리스트의 맨 마지막 element를 return하고 그 element는 삭제
print(aa.pop()) # 8
print(aa) # [45, 21, 18, 17]

# 8. 리스트에 포함된 특정 x의 개수 리턴
print(aa.count(18)) # 18의 개수 = 1개

# 9. 리스트를 확장 : extend(x) 에서는 x는 리스트만 올수 있다. 원래의 리스트에 x 리스트를 더한다
aa.extend([4,19,91,2]) # aa += [4,19,91,2]와 동일하다
print(aa) # [45, 21, 18, 17, 4, 19, 91, 2]

print("***************************************************************")

# TUPLE : 튜플은 몇가지 요소만 빼면 리스트와 비슷하다.
# 리스트는 []이지만 튜플은 ()이다.
# *** 리스트는 element의 값을 생성, 삭제, 수정할 수 있지만 튜플은 그렇게 할수 없다!
# 튜플에서는 element가 1개만 있을 때는 t5 = (1,) 이런식으로 뒤에 콤마를 붙여야한다.
# 또, 튜플에서는
# t1 = () / t2 = (1,3,45) / t3 = ('a', 'b'('ffj','we')) <- 예시
t1 =(1,3,5,6,8)
# del t1[3] # del(tl[3]) 는 안 나옴
# t1[3] = 5 # 이거도 불가

print(t1[0]) # 인덱스 0의 값을 리턴
# 슬라이싱
print(t1[:3]) # (1, 3, 5)

# 튜플 더하기
t2 = (4,6,3)
t3 = t1+t2
# print(t3) # (1, 3, 5, 6, 8, 4, 6, 3)

# 튜플 곱하기
t6 = t1*3
# print(t6) # (1, 3, 5, 6, 8, 1, 3, 5, 6, 8, 1, 3, 5, 6, 8)

# 튜플 길이 구하기
print(len(t6)) # 15

print("***************************************************************")

#DICTIONARY 딕셔너리 : Associative array나 Hash라고도 한다.(대응관계를 표현)
# {key1:value1, key2:value2, ..}꼴 key는 변하지 않는 값, value는 변하는 값과 변하지 않는 값 둘다 사용할 수있
dic = {'Name':'Noy', 'Age': 24,'date': 20200115} # key = name, age, date / value = noy, 24, 2020..etc
# a = {1: [2,58,19]} 이런식으로 value에 리스트를 넣을수도 있다

# 딕셔너리 쌍 추가하기
dic['like1'] = 'Nick and Morty'
print(dic) # {'Name': 'Noy', 'Age': 24, 'date': 20200115, 'like1': 'Nick and Morty'}

# 딕셔너리에서 쌍 삭제하기
del dic['date']
print(dic) # {'Name': 'Noy', 'Age': 24, 'like1': 'Nick and Morty'}

# 딕셔너리에서 key를 사용해 value얻기
print(dic['Name'])

# 만약 키값과 밸류값의 위치를 바꾼다면?
dic2 = {'noy':1, 'mandy':2}
print(dic2['noy']) # print(dic2[2]) 얘는 불가

# 딕셔너리를 만들때 주의사항
# 1. 키값은 고유하므로 중복되게 하면 나머지 키값의 요소들은 모두 무시된다
# 2. 딕셔너리의 키 값은 리스트는 쓸수없지만 튜플은 쓸수있다.
# -> 리스트는 element 값이 변할 수 있기 때문에 키로 사용할 수 없고 튜플은 변하지 않는 값이므로 사용가능
# DY{(1,160,46):'dy'} #<- 왜 안돼 시바? # a{[1,160,46]:dy} 불가능

# 딕셔너리 관련 함수들
# 1. 키만 모은 리스트 만들기
print(dic.keys()) # dict_keys(['Name', 'Age', 'like1'])
# 이 dict_keys 집합은 리스트 고유의 함수는 사용불가
for k in dic.keys():
    print(k)
# 이 키 집합을 리스트로 반환 하려면
keys = list(dic.keys())
print(keys)

# 2. 밸류 리스트 만들기
print(dic.values())

# 3. key, value 쌍얻기
print(dic.items()) # dict_items([('Name', 'Noy'), ('Age', 24), ('like1', 'Nick and Morty')])

# 4. 딕셔너리에 있는 모든 쌍 지우기
print(dic2) # {'noy': 1, 'mandy': 2}
dic2.clear()
print(dic2) # {}

# 5. key로 value얻기
print(dic.get('like1'))\
# None은 거짓이라는 뜻이다!**
# 만약 특정 키가 딕셔너리 안에 없을때는 디폴트값을 뱉도록하려면
print(dic.get('Nokey','We bear bears'))

# 6. 해당 키가 딕셔너리 안에 있는지 조사하기 : in
print('name' in dic)
print('Name' in dic)