# 1+1 = 2 1+2 = 
# for  loops 

num1 = 1
num2 = 1
result = 0


for i in range(10+1):
    result = num1 + num2
    num1 = num2
    num2 = result 

    print(result)



list = [1,2,3,4,5,6,7,8,9,10]
num = 1

while True:
    if num <= 5:
        list.remove(num)
        num += 1
    else:
        print(list)
        break