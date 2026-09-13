class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.count = 0


    @property
    def load_factor(self):
        return self.count / self.size


    def collision_count(self):
        total_collisions = 0
        for bucket in self.table:
            if len(bucket) > 1:
                total_collisions += len(bucket) - 1
        return total_collisions


    def max_chain_length(self):
        return max(len(bucket) for bucket in self.table)


    def _hash_function(self, key):
        return abs(hash(key)) % self.size


    def set(self, key, value):
        bucket_index = self._hash_function(key)
        bucket = self.table[bucket_index]

        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1


    def get(self, key):
        bucket_index = self._hash_function(key)
        bucket = self.table[bucket_index]

        for k, v in bucket:
            if k == key:
                return v
        return None


    def remove(self, key):
        bucket_index = self._hash_function(key)
        bucket = self.table[bucket_index]

        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                bucket.pop(i)
                self.count -= 1
                return True
        return False


    def __str__(self):
        result = []
        for idx, bucket in enumerate(self.table):
            result.append(f"Корзина {idx}: {bucket}")
        return "\n".join(result)
