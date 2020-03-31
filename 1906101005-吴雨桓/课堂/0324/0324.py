class Node:
    def __init__(self,value):
        self.value = value #当前节点的值
        self.next = None #下一个节点

class List:
    def __init__(self):
        #头节点
        self.head = Node(-1)

    #前插法创建单链表（用当前节点的next连接上一个节点）
    def insert_before(self,data):
        for i in data:
            node = Node(i)#创建新节点
            #判断头节点的下一个节点是否为空
            if self.head.next is None: #如果为空，则将新节点加入到next
                self.head.next = node
            else:
                node.next = self.head.next #将头节点的下一个节点加入到当前节点的next
                self.head.next = node

    #尾插法创建单链表（用当前节点的next连接下一个节点）
     def insert_tail(self,data):
        tail = self.head.next #将头节点的下一个节点存在tail里
        for i in data:
            node = Node(i) #创建新节点
            #判断头节点的下一个节点是否为空
            if tail is None: #为空，则将新节点加入到next
                self.head.next = node
                tail = node
            else:
                tail.next = node
                tail = node

    #打印单链表
    def list_print(self):
        node = self.head.next
        while node:
            print(node.value,'',end='')
            node = node.next
        print('')

    #删除链表中重复元素
    def clear_repetition(self):
        cur=self.head #将头节点的值赋给cur
        while cur: #只要cur存在，就会进入while循环
            while cur.next and cur.value==cur.next.value: #只要这两个条件存在,就跳过重复的节点，连接到下个节点
                cur.next=cur.next.next
            cur=cur.next

    #第i个节点前插入值为value的节点
    def list_element_add(self,i,value):
        node_new = Node(value) #创建新节点
        index = 0
        node = self.head.next #向后挪一位，避开之前创建的头节点-1

        while node: #找位置
            index = index + 1
            if index == i-1: #在第i个节点前插入，要先找到第i-1个节点
                break
            node = node.next
        if node is None:
            return False

        node_new.next = node.next #插入节点
        node.next = node_new