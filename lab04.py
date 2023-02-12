from lab03 import ArrayStack


def isParenthesesMatching(expression: str) -> bool:
    stack = ArrayStack()

    for char in expression:
        if char == '(':
            stack.push('(')
        elif char == ')':
            stack.pop()

    if not stack.isEmpty():
        print(f'Parentheses in {expression} are unmatched.')
        return False

    return stack.isEmpty()


def copyStack(stack1: ArrayStack, stack2: ArrayStack) -> None:
    tempStack = ArrayStack()

    stack2.clearStack()

    while stack1.size() != 0:
        data = stack1.pop()
        tempStack.push(data)

    while tempStack.size() != 0:
        data = tempStack.pop()

        stack1.push(data)
        stack2.push(data)


def inFixToPostfix(expression: str) -> str:
    stack = ArrayStack()
    postfix = ''

    for char in expression:
        if char in '*/':
            stack.push(char)
            continue
        elif char in '+-':
            if '*' in stack.data or '/' in stack.data:
                while stack.size() != 0:
                    expr = stack.pop()
                    postfix += expr

            stack.push(char)
            continue

        postfix += char

    while stack.size() != 0:
        expr = stack.pop()
        postfix += expr

    return postfix


def main() -> None:
    str = '(((A-B)*C)'
    result = isParenthesesMatching(str)
    print(result)

    s1 = ArrayStack()
    s1.push(10)
    s1.push(20)
    s1.push(30)

    s2 = ArrayStack()
    s2.push(15)

    copyStack(s1, s2)

    s1.printStack()
    s2.printStack()

    exp = 'A+B*C-D/E'
    postfix = inFixToPostfix(exp)
    print(f'Postfix of {exp} is {postfix}')


if __name__ == '__main__':
    main()
