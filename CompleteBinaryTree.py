# 陈荣榕 42154060
import random
import time


class Node:
    def __init__(self,key=None,next=None):
        self.key = key
        self.next = next

class CompleteBinaryTree:
    def __init__(self,key):
        self.head = Node(key)
        self.tail = self.head
        self.size = 1

    def insert(self,key):
        self.tail.next = Node(key)
        self.tail = self.tail.next
        self.size +=1

    def getParent(self,index):
        index = index +1
        pre_cnt = 1
        cur_cnt = 2
        pre_node = self.head
        cur_node = self.head.next
        while cur_node is not None:
            if cur_cnt != index:
                cur_node = cur_node.next
                if cur_cnt/2 > pre_cnt:
                    pre_cnt +=1
                    pre_node = pre_node.next
                cur_cnt += 1
            else:
                return pre_node
        return None

    def getLeftChild(self,index):
        index = index +1
        cur_index = 1
        child_index = -1
        cur_node = self.head
        while cur_node is not None:
            if cur_index == index:
                child_index = cur_index*2
            if cur_index == child_index:
                return cur_node
            cur_index += 1
            cur_node = cur_node.next

    def getRightChild(self,index):
        index = index +1
        cur_index = 1
        child_index = -1
        cur_node = self.head
        while cur_node is not None:
            if cur_index == index:
                child_index = cur_index*2+1
            if cur_index == child_index:
                return cur_node
            cur_index += 1
            cur_node = cur_node.next

class MinPriorityQueue(CompleteBinaryTree):
    def __init__(self,key):
        super(MinPriorityQueue, self).__init__(key)
    def changeNodeKey(self,node1,node2):
        tmp = node1.key
        node1.key = node2.key
        node2.key = tmp


    def insert(self,key):
        super(MinPriorityQueue, self).insert(key)
        self.percUp(self.size-1,self.tail)

    def percUp(self,i,node):
        while node is not None and i >=0:
            parent = self.getParent(i)
            if parent is None:
                break

            if parent.key > node.key:
                self.changeNodeKey(parent,node)

            node = parent
            i = (i-1)//2

    def delMin(self):
        min = self.head.key
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head.key = self.tail.key
            self.size -= 1
            self.percDown(0,self.head)
            self.changeTail()
        return min

    def percDown(self,index,node):
        while node is not None:
            left = None
            right = None
            if index*2 + 1 < self.size:
                left = self.getLeftChild(index)
            else:
                break
            if index*2 + 2 < self.size:
                right = self.getRightChild(index)

            tmp_node = None
            tmp_index = index
            if right is not None and right.key < node.key:
                self.changeNodeKey(right,node)
                tmp_node = right
                tmp_index = index*2 +2
            if left is not None and left.key < node.key:
                self.changeNodeKey(left,node)
                tmp_node = left
                tmp_index = index*2 + 1
            node = tmp_node
            index = tmp_index

    def changeTail(self):
        curNode = self.head
        pre = None
        while curNode is not None:
            if curNode == self.tail:
                self.tail = pre
                self.tail.next = None
            else:
                pre = curNode
                curNode = curNode.next


import  numpy as np
nums = np.linspace(1000,10000,10,endpoint=True)
print(nums)
inster_time = []
del_time = []
for num in nums:
    queue = MinPriorityQueue(random.randint(0,10000))
    start = time.time()
    for i in range(int(num)):
        queue.insert(random.randint(0,10000))
    end = time.time() - start
    inster_time.append(end)
    start2 = time.time()
    for n in range(int(num)):
        queue.delMin()
    del_time.append(time.time() - start2)
print(inster_time)
print(del_time)





