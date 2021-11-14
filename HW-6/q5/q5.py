# 5

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
                else:tmpnode = tmpnode.next
                    
    def remove_dups(self):
        node = self.head
        while node!=None and node.next != None :
            tmpnode1 = node.next
            tmpnode2 = node
            while tmpnode1!=None:
                if node.data == tmpnode1.data:
                    tmpnode1 = tmpnode1.next
                    tmpnode2.next = tmpnode1
                else:
                    tmpnode1 = tmpnode1.next
                    tmpnode2 = tmpnode2.next
            node = node.next
        return 
    
    
    
first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(11)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(5)
linked_list.insert(11)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(11)
linked_list.insert(5)
linked_list.insert(5)
linked_list.insert(11)
linked_list.insert(11)

print("The Linked List is:")
linked_list.print_list()
linked_list.remove_dups()
print("After removing the duplications, the Linked List is:")
linked_list.print_list()
            