"""
计算斐波那契数列
"""

s0 = 1
s1 = 1
print(s0)
print(s1)
for i in range(10000):
    print(s0 + s1)
    temp = s0 + s1
    s0 = s1
    s1 = temp

    