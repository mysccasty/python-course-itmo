class DynamicHashTable:
    def __init__(self, initial_size=256):
        self.size = initial_size
        self.table = [None] * self.size
        self.count = 0
        self.load_factor = 0.75
        self.shrink_factor = 0.25

    def _hash_function_1(self, key):
        return hash(key) % 256

    def _hash_function_2(self, key):
        return hash(key) % 128

    def _hash(self, key):
        return self._hash_function_2(self._hash_function_1(key)) % self.size

    def _resize(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [None] * self.size
        self.count = 0
        for bucket in old_table:
            if bucket is not None:
                for key, value in bucket:
                    self.insert(key, value)

    def _check_resize(self):
        if self.count / self.size > self.load_factor:
            self._resize(self.size * 2)
        elif self.count / self.size < self.shrink_factor and self.size > 256:
            self._resize(self.size // 2)

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.count += 1
        self._check_resize()

    def search(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    self.count -= 1
                    self._check_resize()
                    return

    def __str__(self):
        return str(self.table)

