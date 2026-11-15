class MyHashSet:

    def __init__(self):
        self.hash = []
        return
    def add(self, key: int) -> None:
        self.hash.append(key)
        return

    def remove(self, key: int) -> None:
        l = []
        for i in self.hash:
            if i == key:
                continue
            else:
                l.append(i)
        self.hash = l
        return

    def contains(self, key: int) -> bool:
        return key in self.hash


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)