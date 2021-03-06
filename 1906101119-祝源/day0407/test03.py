#链表的方式实现队列
class Node:
    #初始化,value为当前节点的值
    def __init__(self,value):
        self.value=value
        self.next=next


class Queue_:
    #初始化队列
    def __init__(self):
        self.head=Node#头节点初始化
        self.end=Node#尾节点初始化
        self.size=0#对列的长度

    #判断队列是否为空
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
        que=Node(value)#创建节点
        if self.head is Node:#判断是否存在头节点
            self.head=self.end=que
        else:#如果存在头节点
            self.end.next=que#将新节点放在为节点后(第一步)
            self.end=que#将尾节点指针指向新节点（第二步）

    #删除队列元素
    def dequeue(self):
        #判断队列是否为空
        if self.head is Node:
            print('dada')
        else:
            self.size-=1
            self.head=self.head.next#删除元素，使头指针指向下一个元素
    #如果删除元素后，队列没有元素，head此时为None,end此时也应该为None
            if self.head is Node:
                self.end=Node
           
            
queue=Queue_()
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.dequeue()
print(queue.que_size())