class Stack(object):
    def __init__(self,limit=10):#初始化一个栈
        self.stack=[] 
        self.limit=limit
    def is_empty(self):#判断是否为空
        return len(self.stack)==0
    def push(self,data):
        if len(self.stack)>=self.limit:
            print('栈溢出')
        else:
            self.stack.append(data)
    def pop(self):#压栈
        if self.stack:
            return self.stack.pop()
        else:
            print("空栈不能被弹出")
    def top(self):#查看栈顶元素
        if self.stack:
            return self.stack[-1]
    def size(self):#判断返回得长度
        return len(self.stack)

stack=Stack()
print(stack.size())

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.size())
print(stack.is_empty())
print(stack.top())
print(stack.pop())
print(stack.top())