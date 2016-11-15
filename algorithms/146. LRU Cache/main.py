class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.least_used = []
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            self.least_used.remove(key)
            self.least_used.append(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            self.least_used.remove(key)
            self.least_used.append(key)
            self.cache[key] = value
        else:
            if len(self.least_used) == self.capacity:
                least = self.least_used[0]
                self.cache.pop(least)
                self.least_used = self.least_used[1:]
            self.cache[key] = value
            self.least_used.append(key)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.set(2, 1)
    cache.set(1, 1)
    print cache.get(2)
    cache.set(4, 1)
    print cache.get(1)
    print cache.get(2)

    cache = LRUCache(2)
    cache.set(2, 1)
    cache.set(2, 2)
    print cache.get(2)
    cache.set(1, 1)
    cache.set(4, 1)
    print cache.get(2)