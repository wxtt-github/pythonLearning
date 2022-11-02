### Python学习进程和线程
---------------------------
Proess对象的start方法用来启动进程，而join方法表示等待进程执行结束
```Python
start = time()
p1 = Process(target=download_task, args=('Python从入门到入土.pdf',))
p1.start()
p2 = Process(target=download_task, args=('Pokemon.apk',))
p2.start()
p1.join()
p2.join()
end = time()
print('总共耗费了%.2f秒' %(end - start))
```
几个重要的包和函数
```Python
from time import time
from time import sleep
from multiprocessing import Process
from os import getpid
from threading import Thread

sleep(<time>)
# 休眠time秒

start = time()
end = time()
time = (start - end)
# 如此可以计算出时间

p1 = Process(target=<函数名>, args=('Python从入门到入土', ))
# target后面跟函数名，args后跟传参，注意最后要有一个逗号，否则报错
p1.start()
p1.join()
# 一个控制进程开始，一个等待进程结束

t1 = Thread(target=<函数名>, args=('Python从入门到入土', ))
# target后面跟函数名，args后跟传参，注意最后要有一个逗号，否则报错
t1.start()
t1.join()
# 同进程
```
