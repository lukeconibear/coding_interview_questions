class Solution:
    def sort_k_sorted(self, array, k):  # time O(nlgk), space O(k)
        min_heap_with_k_elements = MinHeap(array[: min(k + 1, len(array))])
        next_index_to_insert_element = 0
        for index in range(k + 1, len(array)):
            min_element = min_heap_with_k_elements.remove()
            array[next_index_to_insert_element] = min_element
            next_index_to_insert_element += 1

            current_element = array[index]
            min_heap_with_k_elements.insert(current_element)

        while not min_heap_with_k_elements.is_empty():
            min_element = min_heap_with_k_elements.remove()
            array[next_index_to_insert_element] = min_element
            next_index_to_insert_element += 1

        return array


class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    def is_empty(self):
        return len(self.heap) == 0

    def build_heap(self, array):
        first_parent_index = (len(array) - 2) // 2
        for current_index in reversed(range(first_parent_index + 1)):
            self.sift_down(current_index, len(array) - 1, array)

        return array

    def sift_down(self, current_index, end_index, heap):
        child_one_index = (current_index * 2) + 1
        while child_one_index <= end_index:
            if (current_index * 2) + 2 <= end_index:
                child_two_index = (current_index * 2) + 2
            else:
                child_two_index = -1

            if child_two_index != -1 and heap[child_two_index] < heap[child_one_index]:
                index_to_swap = child_two_index
            else:
                index_to_swap = child_one_index

            if heap[index_to_swap] < heap[current_index]:
                self.swap(current_index, index_to_swap, heap)
                current_index = index_to_swap
                child_one_index = (current_index * 2) + 1
            else:
                return

    def sift_up(self, current_index, heap):
        parent_index = (current_index - 1) // 2
        while current_index > 0 and heap[current_index] < heap[parent_index]:
            self.swap(current_index, parent_index, heap)
            current_index = parent_index
            parent_index = (current_index - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value_to_remove

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
