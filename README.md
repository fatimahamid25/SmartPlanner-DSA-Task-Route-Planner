SmartPlanner: Task and Route Planner

A Python app that organizes your tasks, schedules them by priority, and finds the best route between locations, built to show Data Structures and Algorithms solving a real everyday problem.

App screenshot

<!-- Add a screenshot of the app and save it as screenshot.png in the repo -->
The problem

Planning a day means deciding what to do first and how to get between places efficiently. SmartPlanner handles both: it keeps your tasks organized, orders them sensibly, and works out an efficient route.

What it does
Add, edit, delete and view tasks
Schedule tasks by [priority / deadline: ADD WHAT YOU USED]
Find the best route between locations using a graph
Search tasks quickly by [keyword / name / date: ADD WHAT YOU USED]
Save tasks so they are still there next time you open the app
Use it from [a desktop GUI and/or a web interface: KEEP WHAT APPLIES]
Data structures and algorithms used
Part	File	What it uses
Task scheduling	scheduler.py	[e.g. priority queue / heap, sorting]
Route planning	graph.py	[e.g. graph with Dijkstra's shortest path]
Task search	search.py	[e.g. binary search / hash map lookup]
Task handling	task_manager.py, models.py	[e.g. classes, lists, dictionaries]
Saving data	storage.py	[e.g. JSON / file handling]

Fill in the bracketed parts with what your code really does. This table is the most valuable section of the README, because it shows you understand the algorithms and didn't just copy them.

Tech stack

Python, [Flask: remove if not used], [Tkinter: remove if not used], HTML, CSS, JavaScript

Run it locally
bash
git clone https://github.com/fatimahamid25/SmartPlanner-DSA-Task-Route-Planner.git
cd SmartPlanner-DSA-Task-Route-Planner
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt   # add this file if missing

Desktop version:

bash
python main.py

Web version:

bash
python app.py

Then open the address shown in your terminal (usually http://127.0.0.1:5000).

Project structure
SmartPlanner-DSA-Task-Route-Planner/
├── app.py            # web app entry point
├── main.py           # desktop app entry point
├── gui.py            # desktop interface
├── task_manager.py   # add, edit, delete tasks
├── scheduler.py      # task ordering
├── graph.py          # route finding
├── search.py         # task search
├── models.py         # data models
├── storage.py        # saving and loading
├── frontend/         # web assets
└── templates/        # HTML pages
What I learned
Applying graphs, queues and searching to a practical problem
Structuring a Python project into separate modules
Connecting one core logic layer to both a desktop and a web interface
Author

Fatima Hamid, Software Engineering student focused on Python, machine learning and data science. GitHub: @fatimahamid25
