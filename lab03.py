from typing import Optional, Any


class ArrayStack:
    def __init__(self) -> None:
        self._stack: list[Any] = []

    @property
    def data(self) -> list[Any]:
        return self._stack

    def size(self) -> int:
        return len(self.data)

    def isEmpty(self) -> bool:
        return self.size() == 0

    def push(self, data: Any) -> list:
        self._stack.append(data)
        return self.data

    def pop(self) -> Optional[Any | None]:
        if self.isEmpty():
            print('Underflow: Cannot pop stack from an empty list.')
            return None

        x = self.data[-1]
        self.data.pop()

        return x

    def stackTop(self) -> Optional[Any | None]:
        if self.isEmpty():
            print('Underflow: Cannot pop stack from an empty list.')
            return None

        return self.data[-1]

    def printStack(self) -> None:
        print(self.data)

    def clearStack(self) -> None:
        self.data.clear()


def main():
    myStack = ArrayStack()

    myStack.push(10)
    myStack.push(20)
    myStack.push(30)

    myStack.printStack()

    x = myStack.pop()
    print(x)

    myStack.pop()

    myStack.printStack()

    myStack.pop()

    print(myStack.isEmpty())

    myStack.pop()


if __name__ == '__main__':
    main()
