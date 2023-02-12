class DataNode:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.next: DataNode = None


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

    def insert_front(self, name: str) -> None:
        '''Insert DataNode into first index of the list'''

        data_node: DataNode = DataNode(name)
        pointer: DataNode = self.head

        if not pointer:
            self.head = data_node
            self.count += 1
            return

        data_node.next = self.head
        self.head = data_node
        self._increase_count()

    def insert_last(self, name: str) -> None:
        '''Insert DataNode into last index of the list'''

        data_node: DataNode = DataNode(name)
        pointer: DataNode = self.head

        if not pointer:
            self.head = data_node
            self.count += 1
            return

        while pointer.next is not None:
            pointer: DataNode = pointer.next

        pointer.next = data_node
        self._increase_count()

    def insert_before(self, name: str, insert_node: str) -> None:
        '''Create DataNode and insert created node into front of selected node'''

        data_node: DataNode = DataNode(insert_node)
        node: DataNode = DataNode(name)
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
            print(f'Cannot insert, "{node.name}" does not exist.')
            return
    
        data_node.next = select_node
        last_pointer.next = data_node

        self._increase_count()
    
    def delete(self, name: str) -> None:
        '''Delete DataNode from the list (break)'''

        node: DataNode = DataNode(name)
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
            print(f'Cannot delete, "{node.name}" not found.')
            return

        if not last_pointer:
            self.head = select_node.next
        else:
            last_pointer.next = select_node.next

        self._decrease_count()
    
    def _increase_count(self) -> None:
        '''Increase list count'''

        self.count += 1

    def _decrease_count(self) -> None:
        '''Decrease list count'''

        self.count -= 1


def main():
    '''Main Function'''

    my_list = SinglyLinkedList()

    my_list.insert_last('John')
    my_list.insert_last('Tony')
    my_list.insert_front('Bill')
    my_list.traverse()

    print('---')

    my_list.insert_before('Tony', 'Kim')
    my_list.traverse()

    my_list.delete('John')

    print('---')

    my_list.traverse()


main()
