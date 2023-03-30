class Student:
    def __init__(self, id: int, name: int, gpa: float):
        self.id = id
        self.name = name
        self.gpa = gpa

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getGPA(self):
        return self.gpa

    def printDetail(self):
        print(f'ID: {self.getId()}')
        print(f'Name: {self.getName()}')
        print(f'GPA: {self.getGPA()}')


class ProbHash:
    def __init__(self, capacity: int) -> None:
        self.hashTable: list[Student] = capacity * [None]
        self.size = capacity

    def hash(self, key: int):
        return key % self.size

    def rehash(self, key: int):
        hashKey = self.hash(key)

        if self.hashTable[hashKey]:
            return self.rehash(hashKey + 1)

        return hashKey

    def insert(self, student: Student):
        hashKey = self.hash(student.getId())

        if self.hashTable[hashKey]:
            hashKey = self.rehash(hashKey)

        self.hashTable[hashKey] = student

        print(f'Insert {student.getId()} at index {hashKey}')

    def search(self, key: int):
        hashKey = self.hash(key)

        for _ in range(self.size):
            if not self.hashTable[hashKey]:
                hashKey = self.hash(hashKey + 1)
                continue

            if self.hashTable[hashKey].getId() == key:
                print(f'Found {key} at index {hashKey}')
                return self.hashTable[hashKey]

            hashKey = self.hash(hashKey + 1)

        print(f'{key} does not exist.')


def main():
    hashTable = ProbHash(20)

    s1 = Student(65070001, "Sandee Boonmak", 3.05)
    s2 = Student(65070077, "Somsak Jaidee", 2.78)
    s3 = Student(65070021, "Somsri Jaiyai", 3.44)
    s4 = Student(65070042, "Sommai Meeboon", 2.89)

    hashTable.insert(s1)
    hashTable.insert(s2)
    hashTable.insert(s3)
    hashTable.insert(s4)

    std = hashTable.search(65070077)
    std.printDetail()
    print("-------------------------")
    std = hashTable.search(65070021)
    std.printDetail()
    print("-------------------------")
    std = hashTable.search(65070042)
    std.printDetail()
    print("-------------------------")
    std = hashTable.search(65070032)

main()
