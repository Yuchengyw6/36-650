# 7

class Queue:
    def __init__(self,length=0,inner_list=[],counter=0):
        self.length = 0
        self.inner_list = []
        self.counter = 0
    
    def enqueue(self, value):
        self.length+=1
        self.inner_list.append(value)
        return 
        
    def dequeue(self):
        self.length-=1
        self.counter+=1
        return self.inner_list[self.counter-1]

class Node:
    data = None
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.too_big = None
        self.big = None
        self.small = None
        
class tritree:
    root = None
    def __init__(self,root):
        self.root = root
    
    def _insert(self,newdata,root):
        newnode = Node(newdata)
        if newdata - root.data < 0 :
            if root.small == None: 
                root.small = newnode
            else: self._insert(newdata,root.small)
        elif newdata - root.data >= 10:
            if root.too_big == None: 
                root.too_big = newnode
            else:self._insert(newdata,root.too_big)
        elif newdata - root.data < 10 and newdata - root.data >=0:
            if root.big == None: 
                root.big = newnode
            else:self._insert(newdata,root.big)
            

    def insert(self,newdata):
        self._insert(newdata, self.root)
        
    def _traversal(self,root,delete=None):
        if root.small:
            self._traversal(root.small)
        print(root.data)
        if root.big:
            self._traversal(root.big)
        if root.too_big:
            self._traversal(root.too_big)
    def traversal(self):
        self._traversal(self.root)
        
    def search(self,root,data):
        if root.small:
            self.search(root.small,tmp)
        if root.data == data:
            return root
        if root.big:
            self.search(root.big,tmp)
        if root.too_big:
            self.search(root.too_big,tmp)
        return 
    
    def Max(self, root):
        if root.too_big != None:
            return self.Max(root.too_big)
        elif root.big != None:
            return self.Max(root.big)
        elif root.big == None and root.too_big == None:
            return root
        
    def Min(self,root):
        if root.small != None:
            return self.Min(root.small)
        else:
            return root
        
    def level(self,delete = None):
        tmp = []
        queue = Queue(length = 0,inner_list = [],counter = 0)
        if self.root is not None:
            queue.enqueue(self.root)
        while queue.length !=0:
            t = queue.dequeue()
            if t.too_big is not None:queue.enqueue(t.too_big)   
            if t.big is not None:queue.enqueue(t.big)
            if t.small is not None:queue.enqueue(t.small)  
            if t.data != delete:tmp.append(t.data) 
        return tmp
        
    def delete(self,deldata):
        tmp = self.level(deldata)
        for i in range(len(tmp)):
            if i == 0 :
                self.root = Node(tmp[0]) 
            else:
                self.insert(tmp[i])
                
    def ptroot(self):
        print(self.root)



        
        

        
        
root = tritree(Node(20))
root.insert(40)
root.insert(45)
root.insert(32)
print("Tree contents after insertion using the traversal()")
root.traversal()
root.delete(45)
print("Tree contents after deleting 45 using the traversal()")
root.traversal()
