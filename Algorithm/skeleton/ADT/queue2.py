import sys 
sys.path.append('../data_structure')

try:
    from linked_list2 import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList
except ModuleNotFoundError:
    from data_structure.linked_list2 import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList

class Queue:
    def __init__(self, *elements, backend):
        assert backend in [list, LinkedList, DoublyLinkedList]
        assert isinstance(elements, (list, tuple))
        self.backend = backend

        if self.backend == list:
            self.list = list(elements)

        elif self.backend == LinkedList:
            self.linked_list = LinkedList(elements)

        elif self.backend == DoublyLinkedList:
            self.doubly_linked_list = DoublyLinkedList(elements)

    def elements(self):
        if self.backend == list:
            return self.list 

        elif self.backend == LinkedList:
            res = []
            cur = self.linked_list.head
            
            while cur is not None:
                res.append(cur.datum)
                cur = cur.next
            
            return res

        elif self.backend == DoublyLinkedList:
            # res = []
            # cur = self.doubly_linked_list.head

            # while cur is not None:
            #     res.append(cur.datum)
            #     cur = cur.next

            # return res
            res = []
            for i in self.doubly_linked_list:
                res.append(i)

            return res

    def enqueue(self, elem):
        if self.backend == list:
            return self.list.insert(0,elem)

        elif self.backend == LinkedList:
            return self.linked_list.add_to_head(elem)
        
        elif self.backend == DoublyLinkedList:
            return self.doubly_linked_list.add_to_head(elem)

    def dequeue(self):
        if self.backend == list:
            return self.list.pop()
                
        elif self.backend == LinkedList:
            return self.linked_list.delete_from_back()

        elif self.backend == DoublyLinkedList:
            return self.doubly_linked_list.delete_from_back()
    
    def front(self):
        if self.backend == list:
            return self.list[-1]

        elif self.backend == LinkedList:
            return self.linked_list.end.datum
        
        elif self.backend == DoublyLinkedList:
            return self.doubly_linked_list.end.datum

    def size(self):
        if self.backend == list:
            return len(self.list)
    
        elif self.backend == LinkedList:
            return len(self.linked_list)
        
        elif self.backend == DoublyLinkedList:
            return len(self.doubly_linked_list)

    def is_empty(self):
        return self.size() == 0
        # if self.backend == list:
        #     return self.list == []
        
        # elif self.backend == LinkedList:
        #     return self.linked_list.size == 0

        # elif self.backend == DoublyLinkedList:
        #     return self.doubly_linked_list.size == 0

    def __str__(self):
        return str(self.elements())
       
    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements() == other.elements()
        return True 


class PriorityQueue:
    def __init__(self, *elements_with_priority, backend = list):
        """Get list of 2-tuple containing (obj, number), which denotes object and its priority. Higher the number, the element have hight priority. 
        """
        assert backend in [list, LinkedList, DoublyLinkedList]
        assert isinstance(elements_with_priority, (list, tuple))

        self.backend = backend

        if self.backend == list:
            self.list = sorted(elements_with_priority, key=lambda x: x[1])
        
        elif self.backend == LinkedList:
            self.linked_list = LinkedList([])
            for element in sorted(elements_with_priority, key = lambda x: x[1], reverse=True):
                self.linked_list.add_to_head(element)
        
        elif self.backend == DoublyLinkedList:
            self.doubly_linked_list = DoublyLinkedList([])
            for element in sorted(elements_with_priority, key = lambda x: x[1], reverse=True):
                self.doubly_linked_list.add_to_head(element)
    
    def elements(self):
        if self.backend == list:
            return self.list
             
        elif self.backend == LinkedList:
            res = []
            cur = self.linked_list.head
            while cur is not None:
                res.append(cur.datum)
                cur = cur.next
            return res

        elif self.backend == DoublyLinkedList:
            res = []
            cur = self.doubly_linked_list.head
            while cur is not None:
                res.append(cur.datum)
                cur = cur.next
            return res
        
    def enqueue(self, elem):
        if self.backend == list:
            for idx, e in enumerate(self.list):
                if elem[1] <= e[1]:
                    self.list.insert(idx, elem)
                    break
            else:
                self.list.append(elem)

        elif self.backend == LinkedList:
            new_node = LinkedNode(node_id=0, datum=elem)

            # when linked list is empty or elem's num is smaller than head's num, add to head
            if not self.linked_list.head or elem[1] < self.linked_list.head.datum[1]:
                new_node.next = self.linked_list.head
                self.linked_list.head = new_node

            # when elem's num is bigger than the last one's num, add to end
            elif elem[1] > self.linked_list.end.datum[1]:
                self.linked_list.end.next = new_node
                new_node.next = None
                self.linked_list.end = new_node

            else:
                cur = self.linked_list.head
                
                # check if there's cur.next(if none, False) and
                # still elem's num is bigger than cur.next(upcoming one)
                while cur.next and cur.next.datum[1] < elem[1]:
                    # loop stops when cur.next[1] is same or bigger than elem[1], meaning the correct insertion point is found
                    cur = cur.next
                new_node.next =cur.next
                cur.next = new_node
            
            self.linked_list.size += 1

        elif self.backend == DoublyLinkedList:
            new_node = DoublyLinkedNode(node_id=0, datum=elem)

            # if head is none -> True which means list is empty or elem'num is smaller than head's num
            if not self.doubly_linked_list.head or elem[1] < self.doubly_linked_list.head.datum[1]:
                new_node.next = self.doubly_linked_list.head
                if self.doubly_linked_list.head: # prevent attribute error which occurs when list is empty
                    self.doubly_linked_list.head.prev = new_node
                    self.doubly_linked_list.head = new_node

            # when elem's num is bigger than end of the list
            elif elem[1] > self.doubly_linked_list.end.datum[1]:
                self.doubly_linked_list.end.next = new_node
                new_node.next = None
                new_node.prev = self.doubly_linked_list.end
                self.doubly_linked_list.end = new_node

            else:
                cur = self.doubly_linked_list.head
                while cur.next and cur.next.datum[1] < elem[1]:
                    cur = cur.next
                new_node.next = cur.next
                if cur.next:
                    cur.next.prev = new_node
                cur.next = new_node
                new_node.prev = cur
            
            self.doubly_linked_list.size += 1

    def dequeue(self):
        if self.backend == list:
            return self.list.pop(-1)

        elif self.backend == LinkedList:
            return self.linked_list.delete_from_back()

        elif self.backend == DoublyLinkedList:
            return self.doubly_linked_list.delete_from_back()
                
    def front(self):
        if self.backend == list:
            return max(self.list, key=lambda x: x[1])
       
        elif self.backend == LinkedList:
            return max(self.linked_list, key=lambda x: x[1])

        elif self.backend == DoublyLinkedList:
            return max(self.doubly_linked_list, key=lambda x: x[1])

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
            return len(self.linked_list)

        elif self.backend == DoublyLinkedList:
            return len(self.doubly_linked_list)

    def is_empty(self):
        if self.backend == list:
            return self.list == []
        
        elif self.backend == LinkedList:
            return self.linked_list.size == 0

        elif self.backend == DoublyLinkedList:
            return self.doubly_linked_list.size == 0

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements == other.elements 
        return True 

if __name__ == '__main__':
    available_backends =[list, LinkedList,DoublyLinkedList]
  
    for backend in available_backends:
        q1 = Queue(1,2,3,4, backend = backend)
        assert q1.elements() == [1,2,3,4], backend
        assert q1.size() == 4, backend

        q1.enqueue(5)
        assert q1.elements() == [5,1,2,3,4]
        assert q1.size() == 5
        assert q1.dequeue() == 4
        assert q1.size() == 4
        print(q1.elements())
        assert q1.elements() == [5,1,2,3]
        assert q1.front() == 3 


        q2 = Queue(backend = backend)

        assert q2.elements() == []
        assert q2.size() == 0
        assert q2.is_empty(), backend
        
        q2.enqueue(1)

        assert q2.elements() == [1]
        assert q2.size() == 1
        assert not q2.is_empty()
        
        if backend == LinkedList:
            print(q1.linked_list, q2.linked_list)

        q2 = PriorityQueue(('c',1), ('d',4), ('e',2), ('b',3), backend = backend)
        # print(q2.elements())
        assert q2.elements() == [('c',1), ('e',2), ('b',3), ('d',4)], backend  
    
        assert q2.size() == 4
        assert q2.front() == ('d', 4), backend
        assert not q2.is_empty()
        # print('q2:', q2, backend)
        # print('q2size is', q2.size(), backend)
        q2.dequeue()
        
        # print(q2.elements())
        assert q2.elements() == [('c',1), ('e',2), ('b',3)], backend
        # print('q2:', q2, backend)
        # print('q2size is', q2.size(), backend)
        assert q2.size() == 3, backend
        assert q2.front() == ('b', 3) 
        assert not q2.is_empty()

        q2.enqueue(('x', 0))
        q2.enqueue(('y', 4))
        q2.enqueue(('z', 2))

        assert q2.elements() == [('x', 0), ('c',1), ('z', 2), ('e',2), ('b',3), ('y', 4)], backend

        print('q2:', q2, backend)
        print('q2size is', q2.size(), backend)
        assert q2.size() == 6, backend
        print('q2:', q2, backend)
        q2.dequeue()
        print('five remians:', q2, backend)
        q2.dequeue()
        print('four remains:', q2, backend)
        q2.dequeue()
        print('three remains:', q2, backend)
        q2.dequeue()
        print('two remains:', q2, backend)
        q2.dequeue()
        print('1 remains in q2:', q2, backend)  
        q2.dequeue()
        print('empty q2:', q2, backend)
        assert q2.is_empty()

