"""
说明：子列表指的是列表中索引（下标）连续的元素构成的列表；
列表中的元素是int类型，可能包含正整数、0、负整数；
程序输入列表中的元素，输出子列表元素求和的最大值，例如：

输入：1 -2 3 5 -3 2
输出：8

输入：0 -2 3 5 -1 2
输出：9

输入：-9 -2 -3 -5 -3
输出：-2
"""

def main():
    items = list(map(int, input().split()))
    overall = partial = items[0]
    for i in range(1, len(items)):
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
    print(overall)


if __name__ == '__main__':
    main()