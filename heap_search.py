# heap_search.py

class HeapSearch:
    def __init__(self, arr):
        self.heap = []
        for num in arr:
            self.insert(num)

    def insert(self, num):
        self.heap.append(num)
        self._sift_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_val
            self._sift_down(0)
        return min_val

    def _sift_up(self, index):
        parent_idx = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_idx]:
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
            index = parent_idx
            parent_idx = (index - 1) // 2

    def _sift_down(self, index):
        left_child_idx = 2 * index + 1
        right_child_idx = 2 * index + 2
        smallest_idx = index

        if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[smallest_idx]:
            smallest_idx = left_child_idx

        if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[smallest_idx]:
            smallest_idx = right_child_idx

        if smallest_idx != index:
            self.heap[index], self.heap[smallest_idx] = self.heap[smallest_idx], self.heap[index]
            self._sift_down(smallest_idx)


# Example usage
arr = [5, 3, 8, 4, 2]
heap = HeapSearch(arr)

print("Heap elements:")
while True:
    minimum = heap.extract_min()
    if minimum is None:
        break
    print(minimum)
