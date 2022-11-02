x = float(input('请输入x值:'))
if x > 1:
    total = 3 * x -5
elif x >= -1 and x <= 1:
    total = x + 2
else:
    total = 5 * x + 3

print('total值为%f' %(total))
