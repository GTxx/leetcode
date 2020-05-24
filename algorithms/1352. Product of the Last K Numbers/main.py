class ProductOfNumbers:

    def __init__(self):
        self.product = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.product = [1]
            return
        else:
            self.product.append(num * self.product[-1])

    def getProduct(self, k: int) -> int:
        if k >= len(self.product) :
            return 0
        else:
            return self.product[-1] // self.product[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

if __name__ == "__main__":
    productOfNumbers = ProductOfNumbers()
    productOfNumbers.add(3)
    productOfNumbers.add(0)
    productOfNumbers.add(2)
    productOfNumbers.add(5)
    productOfNumbers.add(4)
    assert productOfNumbers.getProduct(2) == 20
    assert productOfNumbers.getProduct(3) == 40
    assert productOfNumbers.getProduct(4) == 0
    productOfNumbers.add(8);
    assert productOfNumbers.getProduct(2) == 32