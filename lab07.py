import random
from time import time


def summationWithLoop(n: int):
    '''Find Summation of n with loops'''

    total = 0

    for i in range(1, n+1):
        total += i

    return total


def summationWithEquation(n: int):
    '''Find Summation of n with equation'''
    return (n / 2) * (n + 1)


def analyzeSummationlgorithm(func, n: int):
    '''Analyze Algorithm'''

    start = time()
    result = func(n)
    end = time() - start

    print(f"{func.__name__} has execution time in {end} seconds with result is {result}.")


def isIntersectWithBigO2(array1: set[int], array2: set[int], array3: set[int]):
    '''Check that all arrays is intersect with O(n^2)'''

    intersect = []

    for a1 in array1:
        for a2 in array2:
            if a1 == a2:
                intersect.append(a1)

    for data in intersect:
        if data in array3:
            return True

    return False


def isIntersectWithBigO3(array1: set[int], array2: set[int], array3: set[int]):
    '''Check that all arrays is intersect with O(n^3)'''

    for a1 in array1:
        for a2 in array2:
            for a3 in array3:
                if (a1 == a2) == a3:
                    return True

    return False


def analyzeIsIntersectAlgorithm(func, a1: list, a2: list, a3: list):
    '''Analyze Algorithm'''

    start = time()
    result = func(a1, a2, a3)
    end = time() - start

    print(f"{func.__name__} has execution time in {end} seconds with result is {result}.")


def randomList(members: int):
    '''List of random number with total of members in'''

    array = set()

    while len(array) != members:
        data = int(random.random() * (members*10000000))
        array.add(data)

    return array


def main():
    '''Main Function'''

    members = [100, 1000, 10000, 100000]

    for member in members:

        array1 = randomList(member)
        array2 = randomList(member)
        array3 = randomList(member)

        print(f'- Set with {member} -')
        analyzeIsIntersectAlgorithm(
            isIntersectWithBigO2, array1, array2, array3)
        analyzeIsIntersectAlgorithm(
            isIntersectWithBigO3, array1, array2, array3)


main()
