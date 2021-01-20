class InfiniteBot:

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num = num + 2
        return num


bot1 = InfiniteBot()
x = iter(bot1)

print(next(x))  # 1
print(next(x))  # 3
print(next(x))  # 5


for i in range(10):
    print(next(x))