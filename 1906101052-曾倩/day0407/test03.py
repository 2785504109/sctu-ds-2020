#连表队列
class Node:
#初始化，value为当前节点的值
    def __init__(self,value):
        self.value=value
        self.next-next
class Queue_:
#初始化队列
    def __init__(self):
        self.head=None#头节点初始化
        self.end=Node#尾节点初始化
        self.size=0
#判断队列是否为空
    def is_empty(self):
        if self.size==0:
            return True
            return False
#返回队列的长度
    def que size(self):
        return self.size
        
#列表添加元素
    def enqueue(self,value):
        self.size+=1
        que=Node(value)#创建节点
        if self.head is None:#判断头节点是否为空
            self.head-self.end=que
        else：
            self.end.next=que
            self.end=que
#删除队列元素
    def dequeue(self):
        if self.head is None:
            print("没东西，不能删")
            return
        else：
            self.size-=1
            self.head-self.head.next
            if self.head is None:
                self.end=None
queue=Queue_（)
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.dequeue()
print(queue.que_size())