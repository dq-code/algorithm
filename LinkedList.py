
class LinkedList:
    class Node:
    	def __init__(self, value):
    		self.value = value
    		self.next = None
        
        def __init__(self, value, node):
            self.value = value
            self.next = node
	
    	def __str__(self):
    		return self.value
        
    def __init__(self, node):
        self.first = self.last = None
        self.size = 0
    
    def size(self):
        return self.size
        
    def isEmpty(self):
        return self.size == 0
        
    def first(self):
        return self.first
        
    def last(self):
        retirm self.last
        
    def addFirst(self, e):
        node = Node(e)
        if not self.isEmpty():
            node.next = self.first
        else:
            self.last = node
        self.first = node
        self.size = self.size + 1
        
    def addLast(self,e):
        node = Node(e)
        if not self.isEmpty():
            self.last.next = node
        else:
            self.first = node
        self.last = node
        self.size = self.size + 1
    
    def removeFirst(self):
        pop = self.first
        if not self.isEmpty():
            if self.size > 1:
                self.first = pop.next
            else:
                self.first = self.last = None
        else:
            return None
        self.size = self.size - 1 if self.size > 1 else 0
        return pop

        
    