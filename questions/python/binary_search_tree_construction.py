class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):  # time O(average = lgn, worst = n), space O(1)
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = Node(value)
                    break
                else:
                    current_node = current_node.left
            elif value > current_node.value:
                if current_node.right is None:
                    current_node.right = Node(value)
                    break
                else:
                    current_node = current_node.right

        return self

    def contains(self, value):  # time O(average = lgn, worst = n), space O(1)
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True

        return False

    def remove(
        self, value, parent_node=None
    ):  # time O(average = lgn, worst = n), space O(1)
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.get_min_value()
                    current_node.right.remove(current_node.value, current_node)
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        pass  # single node
                elif parent_node.left == current_node:
                    if current_node.left is not None:
                        current_node.left = current_node.left
                    else:
                        current_node.left = current_node.right
                elif parent_node.right == current_node:
                    if current_node.right is not None:
                        current_node.right = current_node.left
                    else:
                        current_node.right = current_node.right
                break

        return self

    def get_min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left

        return current_node.value
