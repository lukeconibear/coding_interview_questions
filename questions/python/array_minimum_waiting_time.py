class Solution:
    def minimum_waiting_time(self, queries): # time O(nlgn), space O(n)
        queries.sort()
        waiting_time = 0
        for index, duration in enumerate(queries):
            queries_left = len(queries) - (index + 1)
            waiting_time += queries_left * duration

        return waiting_time