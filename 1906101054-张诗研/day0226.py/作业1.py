#1.设f(x)=3x4-9x2+x/2，请将f(x)封装为一个函数，求当x等于以下值时，f(x)是多少.
#X取值：54,96,83,64,234,158,364
list1=[54,96,83,64,234,158,364]
def f(x):
    y=3*x**4-9*x**2+x/2
    return y
for x in list1:
    print(f(x))
