import heapq


class Scheduler:

    def priority_schedule(self, tasks):

        priority_queue = []

        for task in tasks.values():

            heapq.heappush(
                priority_queue,
                (int(task.priority), task.task_id, task)
            )

        print("\n--- PRIORITY SCHEDULE ---")

        if len(priority_queue) == 0:

            print("No tasks available.")

        else:

            while priority_queue:

                priority, task_id, task = heapq.heappop(priority_queue)

                print(
                    "Task:",
                    task.name,
                    "| Priority:",
                    task.priority
                )