class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1

linked_list = LinkedList()
elements = input("enter array ").split()
elements = [int(x) for x in elements]

for element in elements:
    linked_list.append(element)

find_num = int(input("Enter number that want to find "))
result = linked_list.search(find_num)

if result != -1:
    print(f"number {find_num} is found at index {result}")
else:
    print(f"nnot found")