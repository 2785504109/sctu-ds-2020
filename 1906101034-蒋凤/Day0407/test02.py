class Queue:
    #初始化列队
    def __init__(self):
        self.que=[]
        self.size=0#列队的长度

    #判断列队是否为空
    def is_empty(self):
        if self.size==0:
            return True
        return False

    #返回列队的长度
    def que_size(self):
        return self.size

    #列表添加元素
    def enqueue(self,value):
        self.size+=1
        self.que.append(value)

    #删除队列元素
    def dequeue(self):
        if self.size==0:
            print('没东西，不能删')
            return 
        else:
            self.size-=1
            self.que.pop(0)

queue=Queue()

