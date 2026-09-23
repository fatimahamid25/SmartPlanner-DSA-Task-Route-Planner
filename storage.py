from models import Task


class Storage:

    def __init__(self, filename="tasks.txt"):
        self.filename = filename

    def save_tasks(self, tasks):

        try:

            with open(self.filename, "w") as file:

                for task in tasks.values():

                    status = "Completed" if task.completed else "Pending"

                    file.write(
                        f"{task.task_id}|"
                        f"{task.name}|"
                        f"{task.priority}|"
                        f"{status}\n"
                    )

            print("Tasks saved successfully.")

        except Exception as e:

            print("Error saving tasks:", e)

    def load_tasks(self):

        tasks = {}

        try:

            with open(self.filename, "r") as file:

                for line in file:

                    line = line.strip()

                    if line == "":
                        continue

                    data = line.split("|")

                    task_id = data[0]
                    name = data[1]
                    priority = data[2]
                    status = data[3]

                    task = Task(
                        task_id,
                        name,
                        priority
                    )

                    if status == "Completed":
                        task.completed = True

                    tasks[task_id] = task

            print("Tasks loaded successfully.")

            return tasks

        except FileNotFoundError:

            print("No saved tasks found.")

            return {}

        except Exception as e:

            print("Error loading tasks:", e)

            return {}

    def clear_tasks(self):

        try:

            with open(self.filename, "w") as file:
                file.write("")

            print("All saved tasks have been cleared.")

        except Exception as e:

            print("Error clearing tasks:", e)