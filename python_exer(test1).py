################연습 문제##########################
# 1.
# s = [80, 75, 55]
# print(s.mean())
q = 80
w = 75
e = 55
mean = (q+w+e)/3
print(mean)

#2
a =13%2
if a == 1 :
    print("Odd")
else:
    print("Even")

# 3.
pin = "881120-1068234"
date = pin[:6]
other = pin[7:]
print(date)
print(other)
#4.
gender = pin[7]
print(gender)
# 5.
al = "a:b:c:d"
all = al.replace(":","#") # '가 아니라 "가 더쎄다
print(all)
#6.
aa = [1,3,5,4,2]
aa.sort()
aa.reverse()
print(aa)

#7.
st = ["Life","is","too","short"]
# sti = str(st)
res = " ".join(st)
print(res)

#8.
et = (1,2,3)
print(id(et))
et = et+(4,) # 튜플에 튜플꼴로 더하면 된다.
print(id(et)) # 하지만 더한 튜플은 예전의 튜플로 같은 튜플이 아니구 주소값이 다른 튜플이다.
print(et)

#9. 2틀림 ->3
# d[[1]] = 'python' # 딕셔너리의 키로는 변하는 값인 리스트를 쓸수 없다.

#10.
ad = {'A':90, 'B':80, 'C':70}
print(ad['B'])

#ii)
result = ad.pop('B')
print(result)
#11.
ali = [1,1,1,2,2,3,3,3,4,4,5]
ase = set(ali) # 맞다! -> 리스트를 집합 자료형으로 변환
alist = list(ase)
print(alist)
#12.b도 변한다./