'''
Hello anyone there, please help me!
'''

numberOnCard = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

cardSuffix = {
    '♣': 1,
    '♦': 2,
    '♥': 3,
    '♠': 4,
}


def convertCardToInteger(card: str):
    number = numberOnCard.get(card[:-1])
    return (number * 1000) + cardSuffix[card[-1]]


def convertIntegerToCard(integer: int):
    integerString = str(integer)
    suffixNumber = integerString[:-3]

    number = int(str(integer)[len(integerString) - len(suffixNumber):])
    suffixNumber = int(suffixNumber)

    suffix = ''

    for k in cardSuffix.keys():
        if cardSuffix[k] == number:
            suffix = k
            break

    for k in numberOnCard.keys():
        if numberOnCard[k] == suffixNumber:
            number = k

    return str(number) + suffix


def convertIntegerDeckToCardDeck(deck: list[int]):
    return [convertIntegerToCard(card) for card in deck]


def convertCardDeckToIntegerDeck(deck: list[str]):
    return [convertCardToInteger(card) for card in deck]


def insertionSort(array: list[int], last: int):
    comparison = 0

    for i in range(last + 1):
        current = array[i]

        j = i - 1

        while j > -1 and current < array[j]:
            array[j + 1] = array[j]
            j -= 1

            comparison += 1

        array[j + 1] = current

        if i == 0:
            continue

        print(convertIntegerDeckToCardDeck(array))

    print('Comparison time:', comparison)


def selectionSort(array: list[int], last: int):
    comparison = 0
    swaps = 0

    for i in range(last):
        min = i

        for j in range(i, last + 1):
            if array[j] < array[min]:
                min = j

            comparison += 1

        array[i], array[min] = array[min], array[i]
        swaps += 1

        print(convertIntegerDeckToCardDeck(array))

    print('Comparison time:', comparison - swaps)


def bubbleSort(array: list[int], last: int):
    comparison = 0

    current = 0

    for _ in range(last):
        walker = last

        while walker > current:
            if array[walker] < array[walker - 1]:
                array[walker], array[walker - 1] = \
                    array[walker - 1], array[walker]

            walker -= 1
            comparison += 1

        current += 1

        print(convertIntegerDeckToCardDeck(array))

    print('Comparison times:', comparison)


def main():
    deck = ['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦']
    lastIndex = len(deck) - 1

    array = convertCardDeckToIntegerDeck(deck)

    insertionSort(array.copy(), lastIndex)
    selectionSort(array.copy(), lastIndex)
    bubbleSort(array.copy(), lastIndex)


main()
