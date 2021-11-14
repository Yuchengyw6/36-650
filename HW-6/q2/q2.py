# 2
import copy
class Queue:
    inner_list = []
    counter = 0
    
    def enqueue(node, value):
        node.inner_list.append(value)
        return 
        
    def dequeue(node):
        node.counter+=1
        return node.inner_list[node.counter-1]
    
    
    def delete(node,value):
        tmpcounter = len(node.inner_list)
        for i in range(tmpcounter):
            tmp = node.dequeue()
            if tmp != value:
                node.enqueue(tmp)
        return 
obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)
obj.delete(7)
print(obj.dequeue())





        
