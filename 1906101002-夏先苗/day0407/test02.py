class Queue:
    #初始化队列
    def __init__(self):
        self.que=[]
        self.size=0
    #判断对列是否为空
    def is_empty(self):
        if self.size==0:
            return True
        return False
    #返回队列的长度
    def que_size(self):
        return self.size
    #列表添加元素
    def enqueue(self,value):
        self.size+=1
        self.que.append(value)
    #删除队列元素
    def dequeue(self):
        if self.size==0:
            print("没东西，不能删")
            return 
        else:
            self.size-=1
            self.que.pop(0)
queue=Queue()
queue.enqueue("1")
queue.enqueue("2")
queue.enqueue("3")
print(queue.is_empty())
queue.dequeue()
print(queue.is_empty())
print(queue.que_size())
