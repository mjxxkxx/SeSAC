try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node

class TreeNode:
    def __init__(self, node_id, datum):
        self.node_id = node_id
        self.datum = datum 

class Tree:
    def __init__(self, root, children = []):
        if not isinstance(root, TreeNode):
            root = TreeNode(node_id=0, datum=root)
        self.root = root
        self.children = children

    def iter_nodes(self):
        yield self.root
        for child in self.children:
            yield from child.iter_nodes()    

    def iter_nodes_with_address(self):
        '''
        [] => 1
        [0] => 11
        [0, 0] => 111
        [0, 1] => 112
        [1] => 12
        [1, 0] => 121
        [1, 1] => 122
        '''
        res = [([], self.root)]

        for idx, child in enumerate(self.children):
            lst = child.iter_nodes_with_address()
            for addr, node in lst:
                res.append(([idx] + addr, node))
        return res
            
    def __iter__(self):
        yield from self.iter_nodes() 

    def insert(self, address, elem):
        idx = address[0]
        if len(address) == 1:
            self.children = self.children[:idx] + [elem] + self.children[idx:]
        else:
            self.children[idx].insert(address[1:], elem)

    def delete(self, address):
        idx = address[0]
        if len(address) == 1:
            res = self.children[idx].root.datum 
            self.children = self.children[:idx] + self.children[idx+1:]
            return res 
        else:
            return self.children[idx].delete(address[1:])
        
    def search(self, elem):
        if self.root.datum == elem:
            return []
        
        for idx, child in enumerate(self.children):
            result = child.search(elem)
            if result is not None:
                return [idx] + result
        return None

    def root_datum(self):
        return self.root.datum

    def height(self):
        res = [[]]
        for idx, child in enumerate(self.children):
            lst = child.iter_nodes_with_address()
            for addr, node in lst:
                res.append([idx] + addr)
        
        max_height = len(res[0])
        for addr in res[1:]:
            if len(addr) > max_height:
                max_height = len(addr)
        return max_height + 1

    def __str__(self):
        return '\n'.join(self.s())
    
    def s(t):
        res = [str(t.root.datum)]
        tab = '    '
        for child in t.children:
            part = child.s()
            for line in part:
                res.append(tab + line)
        return res

if __name__ == '__main__':
    t1 = Tree(1, [
                Tree(11, [Tree(111), Tree(112)],), 
                Tree(12, [Tree(121), Tree(122), Tree(123),])
             ]
         )
    print(t1)
    """
    1
    ├── 11
    │   ├── 111
    │   └── 112 
    └── 12
        ├── 121
        ├── 122
        └── 123 

    t1.insert([2], Tree(13, [Tree(131), Tree(132), Tree(133)]))

    1
    ├── 11
    │   ├── 111
    │   └── 112 
    ├── 12
    │   ├── 121
    │   ├── 122
    │   └── 123 
    └── 13
        ├── 131
        ├── 132
        └── 133 

    t1.insert([1, 1], Tree(122, [Tree(1221), Tree(1222)]))

    1
    ├── 11
    │   ├── 111
    │   └── 112 
    ├── 12
    │   ├── 121
    │   ├── 122
    │   |   ├──1221
    │   |   └──1222
    │   ├── 122
    │   └── 123 
    └── 13
        ├── 131
        ├── 132
        └── 133 
    1
        11
            111
            112 
        12
            121
            122
            123 
    """
    
    for addr, n in t1.iter_nodes_with_address():
        print(addr, n.datum)

    assert t1.root_datum() == 1 
    assert t1.height() == 3

    for addr, n in t1.iter_nodes_with_address():
        assert [int(e)-1 for e in list(str(n.datum))[1:]] == addr 
        assert t1.search(n.datum) == addr 

    t1.insert([2], Tree(13, [Tree(131), Tree(132), Tree(133)]))
    t1.insert([1, 1], Tree(122, [Tree(1221), Tree(1222)]))

    print(t1)
    
    assert 122 == t1.delete([1,2])
    assert 123 == t1.delete([1,2])

    for addr, n in t1.iter_nodes_with_address():
        assert [int(e)-1 for e in list(str(n.datum))[1:]] == addr 
        assert t1.search(n.datum) == addr 

    print(t1)
