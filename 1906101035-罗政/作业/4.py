"""
求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
要求：n需要是input输入，且小于数组长度，不能固定。
"""
n=int(input("请输入一个数："))
L=[14,25,98,75,23,1,4,56,59]
sum=0
if n<len(L):
    for x in L[:n]:
        sum+=x**2
    print(sum)
else:
    print("错误")
