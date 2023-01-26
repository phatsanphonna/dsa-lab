class DataNode:
    def __init__(self, name) -> None:
        self.name = name
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.count = 0
        self.head = None

    def traverse(self) -> None:
        '''Loop through the list'''

        pointer: DataNode = self.head

        if not pointer:
            print('This is an empty list.')
            return

        while pointer is not None:
            print(pointer.name)
            pointer = pointer.next

    def insert_front(self, data_node: DataNode) -> None:
        '''Insert DataNode into first index of the list'''

        pointer: DataNode = self.head

        if not pointer:
            self.head = data_node
            self.count += 1
            return

        data_node.next = self.head
        self.head = data_node
        self.count += 1

    def insert_last(self, data_node: DataNode) -> None:
        '''Insert DataNode into last index of the list'''

        pointer: DataNode = self.head

        if not pointer:
            self.head = data_node
            self.count += 1
            return

        while pointer.next is not None:
            pointer: DataNode = pointer.next

        pointer.next = data_node
        self.count += 1

    def insert_before(self, node: DataNode, name: str) -> None:
        '''Create DataNode and insert created node into front of selected node'''

        data_node = DataNode(name)
        select_node: DataNode = None

        pointer: DataNode = self.head
        last_pointer: DataNode = None

        while pointer is not None:
            if pointer.name == node.name:
                select_node = pointer
                break

            last_pointer = pointer
            pointer = pointer.next
        
        if not select_node:
            print(f'Cannot insert, {node} does not exist.')
            return
    
        data_node.next = select_node
        last_pointer.next = data_node

        self.count += 1
    
    def delete(self, node: DataNode) -> None:
        '''Delete DataNode from the list (break)'''

        select_node: DataNode = None

        pointer: DataNode = self.head
        last_pointer: DataNode = None

        while pointer is not None:
            if pointer.name == node.name:
                select_node = pointer
                break

            last_pointer = pointer
            pointer = pointer.next
        
        if not select_node:
            print(f'Cannot delete {node} from the list.')
            return

        if not last_pointer:
            self.head = select_node.next
        else:
            last_pointer.next = select_node.next

        self.count -= 1


def main():
    my_list = SinglyLinkedList()

    p_new = DataNode('John')
    my_list.head = p_new

    k_new = DataNode('Fluke')
    my_list.insert_front(k_new)

    j_new = DataNode('James')
    my_list.insert_last(j_new)

    l_new = DataNode('Lisa')
    my_list.insert_last(l_new)

    my_list.delete(p_new)

    my_list.traverse()


main()
