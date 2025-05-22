"""
#Time Complexity
-__init__: O(1)
-getMin: O(1)
-insert: O(log n) — due to _heapify_up

-extractMin: O(log n) — due to _heapify_down
-_heapify_up: O(log n) - At most moves up the heap height (log n)
-_heapify_down: O(log n) - At most moves down the heap height (log n)
-_swap: O(1)
-Index helpers (_parent_index, _left_child_index, _right_child_index): O(1)

#Space Complexity
-All methods: O(1) in-place operations
-Overall heap storage: O(n) for storing all elements

# Did this code successfully run on Leetcode : This is not present in Leetcode.
# Any problem you faced while coding this : No, learned about helper functions and complete binary tree
"""

class MinHeap:
    def __init__(self):
        self.heap = []

    def getMin(self):
        if self.heap:
            return self.heap[0]
        else:
            return print("heap is empty")

    def insert(self, val):
        self.heap.append(val)
        insert_index = len(self.heap)-1
        self._heapify_up(insert_index)

    def extractMin(self):
        if not self.heap:
            return None
        else: 
            last_index = len(self.heap) - 1
            self._swap(0, last_index)
            min_element = self.heap.pop()
            self._heapify_down(0)
            return min_element

    def _heapify_up(self, index):
        while index > 0:
            parent_index = self._parent_index(index)
            if self.heap[index] < self.heap[parent_index]:
                self._swap(index,parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        heap_size = len(self.heap)
        while self._left_child_index(index) < heap_size:
            left_child = self._left_child_index(index)
            right_child = self._right_child_index(index)
            smallest = index

            if left_child < heap_size and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child

            if right_child < heap_size and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child
            
            print(f"heap: {self.heap}, index: {index}, smallest: {smallest}")  # Debug line

            if smallest != index:
                self._swap(index,smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _parent_index(self, i):
        return (i - 1) // 2

    def _left_child_index(self, i):
        return 2 * i + 1

    def _right_child_index(self, i):
        return 2 * i + 2

def test_min_heap():
    h = MinHeap()

    # Insert elements (no asserts here, just confirmation)
    h.insert(10)
    print("PASS: Insert 10")
    h.insert(4)
    print("PASS: Insert 4")
    h.insert(15)
    print("PASS: Insert 15")
    h.insert(20)
    print("PASS: Insert 20")
    h.insert(0)
    print("PASS: Insert 0")
    h.insert(8)
    print("PASS: Insert 8")

    # Now do meaningful assertions with try-except for reporting
    try:
        assert h.getMin() == 0
        print("PASS: getMin should return 0")
    except AssertionError:
        print("FAIL: getMin should return 0")

    try:
        assert h.extractMin() == 0
        print("PASS: extractMin should return 0")
    except AssertionError:
        print("FAIL: extractMin should return 0")

    try:
        assert h.getMin() == 4
        print("PASS: New min after removing 0 should be 4")
    except AssertionError:
        print("FAIL: New min after removing 0 should be 4")

    try:
        assert h.extractMin() == 4
        print("PASS: extractMin should return 4")
    except AssertionError:
        print("FAIL: extractMin should return 4")

    try:
        assert h.getMin() == 8
        print("PASS: New min after removing 4 should be 8")
    except AssertionError:
        print("FAIL: New min after removing 4 should be 8")

    # Insert more elements with confirmation prints
    h.insert(2)
    print("PASS: Insert 2")
    h.insert(3)
    print("PASS: Insert 3")

    try:
        assert h.getMin() == 2
        print("PASS: After inserting 2 and 3, min should be 2")
    except AssertionError:
        print("FAIL: After inserting 2 and 3, min should be 2")

    # Extract elements with assertions and prints
    try:
        assert h.extractMin() == 2
        print("PASS: extractMin should return 2")
    except AssertionError:
        print("FAIL: extractMin should return 2")

    try:
        assert h.extractMin() == 3
        print("PASS: extractMin should return 3")
    except AssertionError:
        print("FAIL: extractMin should return 3")

    try:
        assert h.extractMin() == 8
        print("PASS: extractMin should return 8")
    except AssertionError:
        print("FAIL: extractMin should return 8")

    try:
        assert h.extractMin() == 10
        print("PASS: extractMin should return 10")
    except AssertionError:
        print("FAIL: extractMin should return 10")

    try:
        assert h.extractMin() == 15
        print("PASS: extractMin should return 15")
    except AssertionError:
        print("FAIL: extractMin should return 15")

    try:
        assert h.extractMin() == 20
        print("PASS: extractMin should return 20")
    except AssertionError:
        print("FAIL: extractMin should return 20")

    # Heap should be empty now
    try:
        assert h.getMin() is None
        print("PASS: Heap should be empty now")
    except AssertionError:
        print("FAIL: Heap should be empty now")

    try:
        assert h.extractMin() is None
        print("PASS: extractMin should return None on empty heap")
    except AssertionError:
        print("FAIL: extractMin should return None on empty heap")


test_min_heap()
