### 第九天
-------------------------
**Python:学习面向对象进阶**

写getter时在前面加上注解@property，如
```python
class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    # getter方法
    @property
    def title(self):
        return self._title

    # setter方法
    @title.setter
    def title(self, title):
        self._title = title
```
