class Student(object):
    def __init__(self,name,age)->None:
        self.name = name
        self.age = age
    
    def study(self,course_name):
        print('%s正在学习%s' %(self.name,course_name))
    
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《葫芦娃》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)

class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    pass
    stu1 = Student('WB',20)
    stu1.study('Python程序设计')
    stu1.watch_movie()

    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)

if __name__ == '__main__':
    main()