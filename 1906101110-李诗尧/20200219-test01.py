#连接字符
# a='hi'
# b='hello'
# print(a+b)

#重复字符
# c='hi'
# print(c*3)

#切片
# str1='asdfg'
# print(str1[0])
# print(str1[-1])
# print(str1[0:4])

#格式化输出
# print("我叫%s"%('张三'))
# print("我今年%d岁"%(12))

#列表
lis1=[5,4,7,3,8]
print(len(lis1))
# lis1.append(1)
# lis1.extend([1,2])
# lis1.pop(1)  #通过下标删值，默认是最后一个
# lis1.sort()
print(lis1.index(7))

# for x in range(len(lis1)):
#     print(lis1[x])

#元祖
tup=("s",100,[1,2])
# tup[1]=200  #元祖元素不能被更改
print(tup)