class Solution:
    def task_assignment(self, k, tasks): # time O(nlgn), space O(n)
        paired_tasks = []
        task_durations_as_indices = self.get_task_durations_as_indices(tasks)
        sorted_tasks = sorted(tasks)
        for index in range(k): # as k pairs
            task_one_sorted_index = index
            task_two_sorted_index = len(tasks) - (index + 1)

            task_one_duration = sorted_tasks[task_one_sorted_index]
            task_two_duration = sorted_tasks[task_two_sorted_index]

            indices_of_task_one_duration = task_durations_as_indices[task_one_duration]
            indices_of_task_two_duration = task_durations_as_indices[task_two_duration]

            task_one_index = indices_of_task_one_duration.pop()
            task_two_index = indices_of_task_two_duration.pop()

            paired_tasks.append([task_one_index, task_two_index])

        return paired_tasks


    def get_task_durations_as_indices(self, tasks):
        task_durations_as_indices = {}
        for index, task_duration in enumerate(tasks):
            if task_duration in task_durations_as_indices:
                task_durations_as_indices[task_duration].append(index)
            else:
                task_durations_as_indices[task_duration] = [index]

        return task_durations_as_indices
