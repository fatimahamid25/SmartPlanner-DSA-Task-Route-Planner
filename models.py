class Task:

    def __init__(self, task_id, name, priority):

        self.task_id = task_id
        self.name = name
        self.priority = priority
        self.completed = False

    def display(self):

        print("ID:", self.task_id)
        print("Task:", self.name)
        print("Priority:", self.priority)
        print("Completed:", self.completed)