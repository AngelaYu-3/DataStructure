# python3

class HeapItem:
    def __init__(self, key, index):
        self.key = key
        self.index = index

class MinHeap:
    def __init__(self, max_len):
        self.max_len = max_len
        self.heap = []

    def insert(self, item):
        self.item = item
        length = len(self.heap)
        curr = length
        if curr % 2 == 0:
            p = int((curr - 2) / 2)
        else:
            p = int((curr - 1) / 2)

        if length < self.max_len:
            self.heap.insert(length, item)
            while self.heap[p].key > self.heap[curr].key:
                self.heap[p].key, self.heap[curr].key = self.heap[curr].key, self.heap[p].key
                if p == 0:
                    break
                if p % 2 == 0:
                    curr = p
                    p = int((p - 2) / 2)
                else:
                    curr = p
                    p = int((p - 1) / 2)

    def extract_min(self):
        root = 0
        smallest = root
        l = (2 * root) + 1
        r = (2 * root) + 2

        min_val = self.heap[0].key
        swap = len(self.heap) - 1

        self.heap[0].key, self.heap[swap].key = self.heap[swap].key, self.heap[0].key
        self.heap.pop(swap)

        if l < len(self.heap) and self.heap[l].key < self.heap[smallest].key:
            smallest = l
        if r < len(self.heap) and self.heap[r].key < self.heap[smallest].key:
            smallest = r

        if smallest == 0:
            pass
        else:
            while self.heap[smallest].key < self.heap[root].key:
                self.heap[root].key, self.heap[smallest].key = self.heap[smallest].key, self.heap[root].key
                root = smallest
                l = (2 * root) + 1
                r = (2 * root) + 2

                if l < len(self.heap) and self.heap[l].key < self.heap[smallest].key:
                    smallest = l
                if r < len(self.heap) and self.heap[r].key < self.heap[smallest].key:
                    smallest = r

        return min_val

    def get_min(self):
        return self.heap[0].key

    def get_min_index(self):
        return self.heap[0].index

    def print(self):
        for i in range(self.max_len):
            print("ft: {}  index: {}".format(self.heap[i].key, self.heap[i].index))
