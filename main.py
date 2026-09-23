from flask import Flask, render_template, request, jsonify
from task_manager import TaskManager

app = Flask(__name__)

manager = TaskManager()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tasks")
def get_tasks():

    tasks = []

    for task in manager.tasks.values():

        tasks.append({
            "id": task.task_id,
            "name": task.name,
            "priority": task.priority,
            "completed": task.completed
        })

    return jsonify(tasks)


@app.route("/add-task", methods=["POST"])
def add_task():

    data = request.json

    task_id = int(data["id"])
    name = data["name"]
    priority = int(data["priority"])

    if task_id in manager.tasks:
        return jsonify({
            "success": False,
            "message": "Task ID already exists!"
        })

    manager.add_task(
        task_id,
        name,
        priority
    )

    return jsonify({
        "success": True,
        "message": "Task added successfully!"
    })


@app.route("/complete-task/<int:task_id>", methods=["POST"])
def complete_task(task_id):

    if task_id not in manager.tasks:

        return jsonify({
            "success": False,
            "message": "Task not found."
        })

    manager.complete_task(task_id)

    return jsonify({
        "success": True,
        "message": "Task completed!"
    })


@app.route("/delete-task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    if task_id not in manager.tasks:

        return jsonify({
            "success": False,
            "message": "Task not found."
        })

    manager.delete_task(task_id)

    return jsonify({
        "success": True,
        "message": "Task deleted!"
    })


if __name__ == "__main__":
    app.run(debug=True)