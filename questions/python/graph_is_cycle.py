class Solution:
    def is_cycle(self, edges):  # time O(v + e), space O(v)
        number_of_nodes = len(edges)
        visited = [False for _ in range(number_of_nodes)]
        currently_in_stack = [False for _ in range(number_of_nodes)]

        for node in range(number_of_nodes):
            if visited[node]:
                continue

            contains_cycle = self.is_node_in_cycle(
                node, edges, visited, currently_in_stack
            )
            if contains_cycle:
                return True

        return False

    def is_node_in_cycle(self, node, edges, visited, currently_in_stack):
        visited[node] = True
        currently_in_stack[node] = True
        neighbours = edges[node]
        for neighbour in neighbours:
            if not visited[neighbour]:
                contains_cycle = self.is_node_in_cycle(
                    neighbour, edges, visited, currently_in_stack
                )
                if contains_cycle:
                    return True
            elif currently_in_stack[neighbour]:
                return True

        currently_in_stack[node] = False
        return False
