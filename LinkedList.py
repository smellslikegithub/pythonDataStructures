class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append_at_end(self, data):
        # Append the first node
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        #Append the new_node at the end of the list
        temp_pointer = self.head
        while temp_pointer.next: # This loop brings us to the last node that points to None
            temp_pointer = temp_pointer.next;
        temp_pointer.next = new_node;

    def append_at_front(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head;
            self.head = new_node

    def append_at_position(self,data, pos):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        elif(pos > self.length() or pos == 0):
            print("Index out of Bounds")
            return -1
        elif(pos == 1 ):
            self.append_at_front(data)

        else:
            temp_pointer = self.head
            new_node = Node(data)
            for i in range(0, pos -1 ):
                #print(temp_pointer.data)
                temp_pointer_prev = temp_pointer
                temp_pointer = temp_pointer.next

            temp_pointer_prev.next = new_node
            new_node.next = temp_pointer

    def length(self):
        temp_pointer = self.head
        sum = 0
        if self.head == None:
            return 0
        while(temp_pointer):
            sum+=1
            temp_pointer = temp_pointer.next
        return sum

    def printList(self):
        temp_pointer = self.head;
        while temp_pointer:
            print(temp_pointer.data)
            temp_pointer = temp_pointer.next

def main():
    my_list = LinkedList()
    my_list.append_at_end("Hello")
    my_list.append_at_end("sam")
    my_list.append_at_end("World")
    my_list.append_at_end("this")

    print(my_list.head.data)
if __name__ == "__main__":
    main()