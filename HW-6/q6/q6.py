# 6 

class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None
        
class ReverseLinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail
        
    def insert(self, data):
        node = Node(data)
        current = self.tail
        if not current:
            self.tail = node
        else:
            node.previous = self.tail
            self.tail = node
            
    def delete(self, data):
        if not self:print("Node not found");return 
        if not self.tail: print("Node not found");return
        temp = self.tail
        if self.tail.data == data:
            print("Node deleted is " + str(self.tail.data))
            self.tail = temp.previous
            return
        while temp.previous:
            if temp.previous.data == data:
                print("Node deleted is " + str(temp.previous.data))
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        return print("Node not found")

    def search(self,data):
        if not self.tail:
            return False
        temp = self.tail
        while temp != None:
            if temp.data == data:
                return True
            temp = temp.previous
        return False
    
    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")
        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n")
    

reversed_linked_list = ReverseLinkedList(Node(11))
reversed_linked_list.insert(3)
reversed_linked_list.insert(6)
reversed_linked_list.insert(5)
print("The Linked List is (after instertion):")
reversed_linked_list.print_list()
reversed_linked_list.delete(6)
print("The Linked List is (after deleting 6):")
reversed_linked_list.print_list()
print("Does 5 exist in the Linked List?")
print(reversed_linked_list.search(5))
print("Does 17 exist in the Linked List?")
print(reversed_linked_list.search(17))

        