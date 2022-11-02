from random import randint
from time import time
from time import sleep
from multiprocessing import Process
import os
from threading import Thread

# 单进程下载，下载慢
def download_task1(filename):
    print('开始下载%s...' %filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成!耗费了%d秒' %(filename, time_to_download))

# 多进程下载，下载快
def download_task2(filename):
    print('启动下载进程，进程号[%d].' %os.getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒' %(filename, time_to_download))

# 用于多线程下载的函数
def download(filename):
    print('开始下载%s...' %filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成!耗费了%d秒' %(filename, time_to_download))

# 继承Thread类来创建自定义的线程类
class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成！耗费了%d秒' %(self._filename, time_to_download))


def main():
    pass
    # # 单进程下载
    # start = time()
    # download_task1('Python从入门到入土.pdf')
    # download_task1('Pokemon.apk')
    # end = time()
    # print('总共耗费了%.2f秒' %(end - start))

    # # 多进程下载
    # start = time()
    # p1 = Process(target=download_task2, args=('Python从入门到入土.pdf',))
    # p1.start()
    # p2 = Process(target=download_task2, args=('Pokemon.apk',))
    # p2.start()
    # p1.join()
    # p2.join()
    # end = time()
    # print('总共耗费了%.2f秒' %(end - start))

    # # 多线程下载
    # start = time()
    # t1 = Thread(target=download, args=('Python从入门到入土.pdf',))
    # t1.start()
    # t2 = Thread(target=download, args=('Pokemon.apk',))
    # t2.start()
    # t1.join()
    # t2.join()
    # end = time()
    # print('总共耗费了%.2f秒' %(end - start))
    
    # 继承Thread类来创建自定义线程类
    start = time()
    t1 = DownloadTask('Python从入门到入土.pdf')
    t1.start()
    t2 = DownloadTask('Pokemon.apk')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()