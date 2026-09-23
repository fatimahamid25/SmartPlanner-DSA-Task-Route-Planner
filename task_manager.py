from collections import deque
from models import Task


class TaskManager:

    def __init__(self):

        self.tasks = {}

        self.undo_stack = []

        self.redo_stack = []

        self.task_queue = deque()


    def add_task(self, task_id, name, priority):

        if task_id in self.tasks:

            print("Task ID already exists!")

        else:

            task = Task(task_id, name, priority)

            self.tasks[task_id] = task

            self.task_queue.append(task)

            self.undo_stack.append(("add", task))

            self.redo_stack.clear()

            print("Task added successfully!")


    def view_tasks(self):

        if len(self.tasks) == 0:

            print("No tasks available.")

        else:

            for task in self.tasks.values():

                task.display()

                print()


    def search_task(self, task_id):

        if task_id in self.tasks:

            print("\nTask Found!")

            self.tasks[task_id].display()

        else:

            print("Task not found.")


    def update_task(self, task_id, name, priority):

        if task_id in self.tasks:

            task = self.tasks[task_id]

            old_name = task.name
            old_priority = task.priority

            task.name = name
            task.priority = priority

            self.undo_stack.append(
                ("update", task_id, old_name, old_priority)
            )

            self.redo_stack.clear()

            print("Task updated successfully!")

        else:

            print("Task not found.")


    def delete_task(self, task_id):

        if task_id in self.tasks:

            task = self.tasks[task_id]

            del self.tasks[task_id]

            self.undo_stack.append(("delete", task))

            self.redo_stack.clear()

            print("Task deleted successfully!")

        else:

            print("Task not found.")


    def complete_task(self, task_id):

        if task_id in self.tasks:

            task = self.tasks[task_id]

            old_status = task.completed

            task.completed = True

            self.undo_stack.append(
                ("complete", task_id, old_status)
            )

            self.redo_stack.clear()

            print("Task marked as completed!")

        else:

            print("Task not found.")


    def process_task(self):

        if len(self.task_queue) == 0:

            print("No tasks in processing queue.")

        else:

            task = self.task_queue.popleft()

            print("\n--- PROCESSING TASK ---")

            task.display()


    def undo(self):

        if len(self.undo_stack) == 0:

            print("Nothing to undo.")

            return

        action = self.undo_stack.pop()


        if action[0] == "add":

            task = action[1]

            if task.task_id in self.tasks:

                del self.tasks[task.task_id]

            self.redo_stack.append(action)


        elif action[0] == "delete":

            task = action[1]

            self.tasks[task.task_id] = task

            self.redo_stack.append(action)


        elif action[0] == "update":

            task_id = action[1]
            old_name = action[2]
            old_priority = action[3]

            task = self.tasks[task_id]

            current_name = task.name
            current_priority = task.priority

            task.name = old_name
            task.priority = old_priority

            self.redo_stack.append(
                ("update", task_id, current_name, current_priority)
            )


        elif action[0] == "complete":

            task_id = action[1]
            old_status = action[2]

            task = self.tasks[task_id]

            current_status = task.completed

            task.completed = old_status

            self.redo_stack.append(
                ("complete", task_id, current_status)
            )


        print("Undo successful!")


    def redo(self):

        if len(self.redo_stack) == 0:

            print("Nothing to redo.")

            return

        action = self.redo_stack.pop()


        if action[0] == "add":

            task = action[1]

            self.tasks[task.task_id] = task

            self.undo_stack.append(action)


        elif action[0] == "delete":

            task = action[1]

            if task.task_id in self.tasks:

                del self.tasks[task.task_id]

            self.undo_stack.append(action)


        elif action[0] == "update":

            task_id = action[1]
            name = action[2]
            priority = action[3]

            task = self.tasks[task_id]

            old_name = task.name
            old_priority = task.priority

            task.name = name
            task.priority = priority

            self.undo_stack.append(
                ("update", task_id, old_name, old_priority)
            )


        elif action[0] == "complete":

            task_id = action[1]
            status = action[2]

            task = self.tasks[task_id]

            old_status = task.completed

            task.completed = status

            self.undo_stack.append(
                ("complete", task_id, old_status)
            )


        print("Redo successful!")