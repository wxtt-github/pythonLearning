# import random

# answer = random.randint(1,100)
# cnt = 0
# while True:
#     cnt+=1
#     number = int(input('请输入一个整数'))
#     if number < answer:
#         print('猜小了')
#     elif number == answer:
#         print('猜对了')
#         break
#     else:
#         print('猜大了')
# print('次数为%d' %(cnt))
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j),end = '\t')
    print()