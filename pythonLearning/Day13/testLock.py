'''
测试用锁来保护临界资源
'''

from time import sleep
from threading import Thread
from threading import Lock

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续操作
        self._lock.acquire()
        try:
            self._balance = self._balance + money
            sleep(0.01)
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()
        
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    for i in range(0,100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
    
    for i in range(0,100):
        threads[i].start()

    for i in range(0,100):
        threads[i].join()

    print('账户余额为: %d元' % account.balance)

if __name__ == '__main__':
    main()