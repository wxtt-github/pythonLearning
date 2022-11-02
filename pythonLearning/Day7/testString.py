from re import A
import sys
def main():
    pass
    # s1 = 'hello,world'
    # s2 = 'hello,world'
    # s3 = '''
    # hello,
    # world
    # '''
    # print(s1,s2,s3,end=' ')
    # s1 = '\'hello, world!\''
    # s2 = '\n\\hello, world!\\\n'
    # print(s1, s2, end='')
    # s1 = '\141\142\143\x61\x62\x63'
    # s2 = '\u6d9b\u795e'
    # print(s1, s2)
    # str1 = 'hello, world!'
    # # 通过内置函数len计算字符串的长度
    # print(len(str1)) # 13
    # # 获得字符串首字母大写的拷贝
    # print(str1.capitalize()) # Hello, world!
    # # 获得字符串每个单词首字母大写的拷贝
    # print(str1.title()) # Hello, World!
    # # 获得字符串变大写后的拷贝
    # print(str1.upper()) # HELLO, WORLD!
    # # 从字符串中查找子串所在位置
    # print(str1.find('or')) # 8
    # print(str1.find('shit')) # -1
    # # 与find类似但找不到子串时会引发异常
    # # print(str1.index('or'))
    # # print(str1.index('shit'))
    # # 检查字符串是否以指定的字符串开头
    # print(str1.startswith('He')) # False
    # print(str1.startswith('hel')) # True
    # # 检查字符串是否以指定的字符串结尾
    # print(str1.endswith('!')) # True
    # # 将字符串以指定的宽度居中并在两侧填充指定的字符
    # print(str1.center(50, '*'))
    # # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    # print(str1.rjust(50, ' '))
    # str2 = 'abc123456'
    # # 检查字符串是否由数字构成
    # print(str2.isdigit())  # False
    # # 检查字符串是否以字母构成
    # print(str2.isalpha())  # False
    # # 检查字符串是否以数字和字母构成
    # print(str2.isalnum())  # True
    # str3 = '  jackfrued@126.com '
    # print(str3)
    # # 获得字符串修剪左右两侧空格之后的拷贝
    # print(str3.strip())
    # a,b = 'ab','abc'
    # print(f'{a} * {b} = {a,b}')

    # list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    # list2 = sorted(list1)
    # # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    # list3 = sorted(list1, reverse=True)
    # # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    # list4 = sorted(list1, key=len)
    # print(list1)
    # print(list2)
    # print(list3)
    # print(list4)
    # # 给列表对象发出排序消息直接在列表对象上进行排序
    # list1.sort(reverse=True)
    # print(list1)

    # 
    
    """
    生成器输出斐波那契数列
    """
    def fib(n):
        a,b = 0,1
        for i in range(n):
            a,b = b,a+b
            yield a

    for item in fib(100):
        print(item)

if __name__ == '__main__':
    main()