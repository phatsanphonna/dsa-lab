class Item:
    def __init__(self, name: str, price: int, weight: float):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getWeight(self):
        return self.__weight

    def __str__(self) -> str:
        return str(self.getWeight())


def coinExchange(amountPlaceholder: int, coinList: list[int]):
    amount = int(amountPlaceholder)
    result = [0, 0, 0, 0]

    while coinList[0] and amount >= 10:
        coinList[0] = coinList[0] - 1
        result[0] = result[0] + 1
        amount -= 10

    while coinList[1] and amount >= 5:
        coinList[1] = coinList[1] - 1
        result[1] = result[1] + 1
        amount -= 5

    while coinList[2] and amount >= 2:
        coinList[2] = coinList[2] - 1
        result[2] = result[2] + 1
        amount -= 2

    while coinList[3] and amount >= 1:
        coinList[3] = coinList[3] - 1
        result[3] = result[3] + 1
        amount -= 1

    print('Amount:', amountPlaceholder)

    if amount:
        print('Coins are not enough.')
    else:
        print('Coin exchange result:', result)
        print('Number of coins:', sum(result))


def knapsack(amount: float, itemList: list[Item]):
    cart: list[Item] = []
    total_weight = 0
    total_price = 0

    itemList = sorted(itemList, key=Item.getWeight)

    for item in itemList:
        if total_weight < amount and total_weight + item.getWeight() <= amount:
            total_weight += item.getWeight()
            total_price += item.getPrice()
            cart.append(item)

    print('Knapsack Size:', amount, 'kg.')
    print('===============================')

    for item in cart:
        print(item.getName(), '->', item.getWeight(),
              'kg ->', item.getPrice(), 'THB')

    print('Total:', total_price, 'THB')


def main():
    item1 = Item('tablet', 7000, 0.5)
    item2 = Item('perfume', 6000, 0.5)
    item3 = Item('guitar', 9000, 1)
    item4 = Item('air purifier', 9000, 2)
    item5= Item('watch', 8000, 0.5)
    itemList = [item1, item2, item3, item4, item5]
    knapsack(3, itemList)


main()
