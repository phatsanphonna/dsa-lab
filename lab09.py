def isSorted(list: list[int]):
    return list == sorted(list)


def insertionSort(array: list[int], last: int):
    comparison = 0

    for i in range(1, last + 1):
        hold = i
        walker = i - 1

        while walker >= 0 and array[hold] < array[walker]:
            array[walker + 1] = array[walker]
            array[walker] = array[hold]
            walker -= 1

            comparison += 1

        hold = walker + 1

        print(array)

    print('Comparison time:', comparison)


def selectionSort(array: list[int], last: int):
    comparison = 0

    for i in range(last):
        min = i

        for j in range(i, last + 1):
            if array[j] < array[min]:
                min = j

            comparison += 1

        array[i], array[min] = array[min], array[i]

        print(array)

    print('Comparison time:', comparison)


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

        print(array)

    print('Comparison times:', comparison)


def main():
    data = [23, 78, 45, 8, 32, 56]
    lastIndex = len(data) - 1

    insertionSort(data.copy(), lastIndex)
    selectionSort(data.copy(), lastIndex)
    bubbleSort(data.copy(), lastIndex)


if __name__ == '__main__':
    main()
