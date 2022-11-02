'''
验证用户名和QQ号
规则如下：
用户名由字母、数字或下划线组成，长度在6~20个字符之间
QQ号是5~12位的数字且首位不能为0
'''
import re
def main():
    pass
    username = input('Please input your username:')
    qq = input('Please input your QQ number:')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if m1 == None:
        print('Please input valid username')
    m2 = re.match(r'^[1-9][0-9]{4,11}$', qq)
    if m2 == None:
        print('Please input valid qq number')

if __name__ == '__main__':
    main()