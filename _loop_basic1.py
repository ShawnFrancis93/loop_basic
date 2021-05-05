for i in range(151):
    print(i)


print(list(range(5, 1000, 5)))

for i in range(5,1001,5):
    print(i) 

i = 0
for i in range(1,101):
    if i % 10 == 0:
        print("CodingDojo")
    elif i % 5 == 0:
        print("Coding")
    else: 
        print(i)


m = 0 
finalSum = 0
while m < 500000:
    if m % 2 !=0:
        finalSum += m
    m += 1
print(finalSum)

for j in range(2018,0,-4):
    print(j)

lowNum = 2
highNum = 60
mult = 3

for i in range(lowNum,highNum + 1):
    if i % mult == 0:
        print(i)

