# 1. shirt

# 2.
res = 0;
a = 0;
while a <= 1000:
    if a%3 == 0:
        res = res+a
    a+=1
print(res) #166833

# 3.
i=0
while True:
    i+=1
    if i>5: break
    print('*'*i)

# 4.
for i in range(1,101):
    print(i,end=' ')

print('\n')

# 5.
c = [70,60,55,75,95,90,80,80,85,100]
num = 0
score = 0
for s in c:
    score = score + s
    num +=1
print(score/num)

# 6.
number = [1,2,3,4,5]
# for n in number:
#     if n%2 == 1:
#         result.append(n*2)

result = [n*2 for n in number if n%2 == 1]
print(result) # [2, 6, 10]

