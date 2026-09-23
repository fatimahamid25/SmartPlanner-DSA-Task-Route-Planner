class Search:

    def search_task(self, tasks, keyword):

        results = []

        for task in tasks.values():

            if keyword.lower() in task.name.lower():
                results.append(task)

        if results:

            print("\n--- SEARCH RESULTS ---")

            for task in results:

                task.display()
                print()

        else:

            print("No task found.")

        return results

    def search_by_priority(self, tasks, priority):

        results = []

        for task in tasks.values():

            if task.priority.lower() == priority.lower():
                results.append(task)

        if results:

            print("\n--- TASKS BY PRIORITY ---")

            for task in results:

                task.display()
                print()

        else:

            print("No tasks found with this priority.")

        return results

    def search_by_status(self, tasks, status):

        results = []

        for task in tasks.values():

            if status.lower() == "completed" and task.completed:
                results.append(task)

            elif status.lower() == "pending" and not task.completed:
                results.append(task)

        if results:

            print("\n--- TASKS BY STATUS ---")

            for task in results:

                task.display()
                print()

        else:

            print("No tasks found with this status.")

        return results