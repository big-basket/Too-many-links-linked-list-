class linkedLinkeedList:
    def add(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def remove(self, node):
        if self.head == node:
            self.head = self.head.next
        else:
            current = self.head
            while current.next != None:
                if current.next == node:
                    current.next = current.next.next
                    break
                current = current.next
    def __init__(self):
        self.head = None
        self.tail = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
