try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node

class LinkedNode:
    def __init__(self, node_id, datum, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 

class LinkedList:
    def __init__(self, elements):
        
        if not elements:
            self.head = None
            self.tail = None
            self.end = None
            self.size = 0

        else:
            elements = list(elements)
            for idx, elem in enumerate(elements):
                if not isinstance(elem, LinkedNode):
                    elements[idx] = LinkedNode(idx, elem)

            self.head = elements[0]
            self.end = elements[-1]

            for idx, elem in enumerate(elements):
                if idx == len(elements)-1:
                    elem.next = None
                else:
                    elem.next = elements[idx+1]
            
            self.tail = LinkedList(elements[1:])
            self.size = len(elements)
            
    def add_to_head(self, elem):
        new_node = LinkedNode(0, elem)
        new_node.next = self.head
        self.head = new_node

        if self.end is None:
            self.end = new_node
        self.size += 1    

    def delete_from_back(self):
        if self.size == 0:
            return "This list is empty"
        
        if self.size == 1:
            deleted_node = self.end
            self.head = None
            self.end = None
            self.size -= 1

            return deleted_node.datum

        cur = self.head
        # stop right before the last one
        while cur.next is not self.end:
            cur = cur.next
        assert cur.next == self.end
        deleted_node = self.end
        self.end = cur # the second from behind
        self.end.next = None
        self.size -= 1

        return deleted_node.datum

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur.datum
            cur = cur.next        
            
    def __str__(self):
        res = []
        current = self.head
        while current is not None:
            res.append(str(current.datum))
            current = current.next
        return ' -> '.join(res)

    def __len__(self):
        return self.size        

class DoublyLinkedNode(Node):
    def __init__(self, node_id, datum, prev = None, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 
        self.prev = prev 

class DoublyLinkedList:
    def __init__(self, elements):
        if elements is None:
            elements = []
        
        elements = list(elements)

        if not elements:
            self.head = None
            self.tail = None
            self.end = None
            self.size = 0
        
        else: 
            nodes = [DoublyLinkedNode(idx, elem) for idx, elem in enumerate(elements)]

            self.head = nodes[0]
            self.end = nodes[-1]

            for idx in range(len(nodes)):
                if idx == len(nodes) - 1:
                    nodes[idx].next = None
                else:
                    nodes[idx].next = nodes[idx + 1]

                if idx == 0:
                    nodes[idx].prev = None
                else:
                    nodes[idx].prev = nodes[idx - 1]

            self.size = len(elements)
            # below is wrong. next nonetype error
            # for idx, elem in enumerate(elements):
            #     if not isinstance(elem, DoublyLinkedNode):
            #         elements[idx] = DoublyLinkedNode(idx, elem)

            # self.head = elements[0]
            # self.end = elements[-1]

            # for idx, elem in enumerate(elements):
            #     if idx == len(elements) - 1:
            #         elem.next = None
            #     else:
            #         elem.next = elements[idx + 1]

            #     if idx == 0:
            #         elem.prev = None
            #     else:
            #         elem.prev = elements[idx-1]

            # self.tail = DoublyLinkedList(elements[1:])
            # self.size = len(elements)

    def add_to_head(self, elem):
        new_node = DoublyLinkedNode(self.size, elem)

        if self.head is None:
            self.head = new_node
            self.end = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1 

    def delete_from_back(self):
        if self.size == 0:
            return "The list is empty"

        if self.size == 1:
            deleted_node = self.end
            self.head = None
            self.end = None
            self.size -= 1
            return deleted_node.datum

        deleted_node = self.end
        self.end = self.end.prev  # Move the end pointer to the previous node
        self.end.next = None  # Remove the reference to the deleted node
        self.size -= 1

        return deleted_node.datum

        # deleted_node = self.end
        # self.end = self.end.prev
        # # Move the end pointer to the previous node
        
        # if self.end: # Check if the new end is not None
        #     self.end.next = None
        #     # Remove the reference to the deleted node
        # else:
        #     self.head = None
        
        # self.size -= 1

        # return deleted_node.datum

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur.datum
            cur = cur.next

    def __str__(self):
        res = []
        cur = self.head
        while cur is not None:
            res.append(str(cur.datum))
            cur = cur.next
        return ' -> '.join(res)
    
    def __len__(self):
        return self.size

if __name__ == '__main__':

    lst = LinkedList([1,2,3])

    print(lst) 
    print(LinkedList.__str__(lst))
    str(lst)
    LinkedList.__str__(lst)
    