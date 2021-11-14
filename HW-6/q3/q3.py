# 3

class Node(object):
    def __init__(node, data):
        node.data = data
        node.next = None


# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")

        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node
            
    def new_insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            node.next = current
            self.head = node

    def delete(self, data):
        if not self.head:return
        temp = self.head
        if self.head.data == data:
            self.head = temp.next
            print("Deleted node is " + str(self.head.data))
            return
        while temp.next:
            if temp.next.data == data:
                print("Node deleted is " + str(temp.next.data))
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Node not found")
        return
    
    def sort(self):
        counter = 0
        tmpnode = self.head
        while tmpnode.next!=None:
            counter = counter + 1
            tmpnode = tmpnode.next
        for i in range(counter):
            tmpnode = self.head
            while tmpnode.next!=None:
                if tmpnode.data>tmpnode.next.data:
                    tmp = tmpnode.data
                    tmpnode.data = tmpnode.next.data
                    tmpnode.next.data = tmp
                    tmpnode = tmpnode.next
                else: tmpnode = tmpnode.next
                    
                
first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(12)
linked_list.insert(3)
linked_list.insert(2)
linked_list.insert(44)
linked_list.insert(553)
linked_list.insert(2)
linked_list.insert(7)
print("The Linked List is:")
linked_list.print_list()
linked_list.sort()
print("After sorting, the Linked List is:")
linked_list.print_list()