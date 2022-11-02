# import random
# # 摇骰子函数
# def roll(n = 2):
#     total = 0
#     for i in range(n):
#         total += random.randint(1,6)
#     return total

# def calculateAll(a = 0, b = 0, c = 0):
#     total = a + b + c
#     return total

# # 在参数名前面的*表示args是一个可变参数
# def add(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total

# # 如果没有指定参数那么使用默认值摇两颗色子
# print(roll())
# # 摇三颗色子
# print(roll(3))
# print(calculateAll())
# print(calculateAll(1))
# print(calculateAll(1, 2))
# print(calculateAll(1, 2, 3))
# # 传递参数时可以不按照设定的顺序进行传递
# print(calculateAll(c=50, a=100, b=200))

# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 3, 5, 7, 9))

# def foo():
#     print('hello, world!')


# def foo():
#     print('goodbye, world!')


# # 下面的代码会输出什么呢？
# foo()

# def foo():
#     b = 'hello'

#     # Python中可以在函数内部再定义函数
#     def bar():
#         c = True
#         print(a)
#         print(b)
#         print(c)

#     bar()
#     # print(c)  # NameError: name 'c' is not defined


# if __name__ == '__main__':
#     a = 100
#     # print(b)  # NameError: name 'b' is not defined
#     foo()

# def foo():
#     global a
#     a = 200
#     print(a)  # 200


# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 200

def main():
    pass #什么都不做的空语句
    print('standard rule')

if __name__ == '__main__':
    main()