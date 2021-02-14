class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, value):
        self.children.append(Node(value))
        return self

    def depth_first_search(self, array):  # time O(v + e), space O(v)
        array.append(self.value)
        for child in self.children:
            child.depth_first_search(array)

        return array
