class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        result = []
        result.append(f'{self.value}')
        while self.next is not None:
            result.append(f'{self.next.value}')
            self.next = self.next.next

        return ''.join(result)

class Solution:
    def remove_duplicates(self, head): # time O(n), space O(1)
        current_node = head
        while current_node is not None:
            next_non_duplicated_node = current_node.next
            while next_non_duplicated_node is not None and next_non_duplicated_node.value == current_node.value:
                next_non_duplicated_node = next_non_duplicated_node.next

            current_node.next = next_non_duplicated_node
            current_node = next_non_duplicated_node

        return head


