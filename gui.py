import tkinter as tk
from tkinter import ttk, messagebox

from tkintermapview import TkinterMapView


# =========================================
# COLORS
# =========================================

BG = "#EEF4FF"
SIDEBAR = "#17183B"
PURPLE = "#6C4CF1"
PURPLE_DARK = "#5134C8"
BLUE = "#4F7CFF"
TEAL = "#18B6A4"
WHITE = "#FFFFFF"
TEXT = "#202344"
MUTED = "#7B82A8"
RED = "#F05A67"
ORANGE = "#F59E0B"


# =========================================
# SMART PLANNER GUI
# =========================================

class SmartPlannerGUI:

    def __init__(self, root, manager, scheduler):

        self.root = root
        self.manager = manager
        self.scheduler = scheduler

        self.root.title("SmartPlanner - Smart Task & Route Planner")
        self.root.geometry("1200x720")
        self.root.minsize(1000, 650)
        self.root.configure(bg=BG)

        self.setup_style()

        self.create_sidebar()
        self.create_main_area()

        self.show_dashboard()

    # =====================================
    # STYLE
    # =====================================

    def setup_style(self):

        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Treeview",
            background=WHITE,
            fieldbackground=WHITE,
            foreground=TEXT,
            rowheight=45,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview.Heading",
            background="#E8EDFF",
            foreground=TEXT,
            font=("Segoe UI", 10, "bold"),
            padding=10
        )

        style.map(
            "Treeview",
            background=[("selected", "#DED7FF")],
            foreground=[("selected", TEXT)]
        )

    # =====================================
    # SIDEBAR
    # =====================================

    def create_sidebar(self):

        self.sidebar = tk.Frame(
            self.root,
            bg=SIDEBAR,
            width=245
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        # Logo
        logo_frame = tk.Frame(
            self.sidebar,
            bg=SIDEBAR
        )

        logo_frame.pack(
            fill="x",
            padx=18,
            pady=(22, 18)
        )

        logo = tk.Label(
            logo_frame,
            text="S",
            bg=PURPLE,
            fg=WHITE,
            font=("Segoe UI", 20, "bold"),
            width=3
        )

        logo.pack(side="left")

        text_frame = tk.Frame(
            logo_frame,
            bg=SIDEBAR
        )

        text_frame.pack(
            side="left",
            padx=10
        )

        tk.Label(
            text_frame,
            text="SmartPlanner",
            bg=SIDEBAR,
            fg=WHITE,
            font=("Segoe UI", 13, "bold")
        ).pack(anchor="w")

        tk.Label(
            text_frame,
            text="Capstone Project",
            bg=SIDEBAR,
            fg="#8990B8",
            font=("Segoe UI", 9)
        ).pack(anchor="w")

        tk.Frame(
            self.sidebar,
            bg="#30315A",
            height=1
        ).pack(
            fill="x",
            padx=18,
            pady=(0, 18)
        )

        tk.Label(
            self.sidebar,
            text="NAVIGATION",
            bg=SIDEBAR,
            fg="#62698F",
            font=("Segoe UI", 9, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(0, 8)
        )

        self.nav_buttons = {}

        self.add_nav_button(
            "▦",
            "Dashboard",
            self.show_dashboard
        )

        self.add_nav_button(
            "✓",
            "Tasks",
            self.show_tasks
        )

        self.add_nav_button(
            "↑",
            "Priority Schedule",
            self.show_schedule
        )

        self.add_nav_button(
            "◇",
            "Dependencies",
            self.show_dependencies
        )

        self.add_nav_button(
            "↗",
            "Route Planner",
            self.show_routes
        )

        self.add_nav_button(
            "⌕",
            "Search",
            self.show_search
        )

        self.add_nav_button(
            "↶",
            "History",
            self.show_history
        )

        self.add_nav_button(
            "▦",
            "Statistics",
            self.show_statistics
        )

    # =====================================
    # NAVIGATION BUTTON
    # =====================================

    def add_nav_button(self, icon, name, command):

        button = tk.Button(
            self.sidebar,
            text=f"  {icon}    {name}",
            command=command,
            anchor="w",
            bd=0,
            relief="flat",
            bg=SIDEBAR,
            fg="#B9BEDD",
            activebackground=PURPLE,
            activeforeground=WHITE,
            font=("Segoe UI", 10, "bold"),
            padx=15,
            pady=12,
            cursor="hand2"
        )

        button.pack(
            fill="x",
            padx=12,
            pady=2
        )

        self.nav_buttons[name] = button

    # =====================================
    # ACTIVE BUTTON
    # =====================================

    def set_active(self, name):

        for button_name, button in self.nav_buttons.items():

            if button_name == name:

                button.configure(
                    bg=PURPLE,
                    fg=WHITE
                )

            else:

                button.configure(
                    bg=SIDEBAR,
                    fg="#B9BEDD"
                )

    # =====================================
    # MAIN AREA
    # =====================================

    def create_main_area(self):

        self.main = tk.Frame(
            self.root,
            bg=BG
        )

        self.main.pack(
            side="left",
            fill="both",
            expand=True
        )

    # =====================================
    # CLEAR SCREEN
    # =====================================

    def clear_main(self):

        for widget in self.main.winfo_children():
            widget.destroy()

    # =====================================
    # HEADER
    # =====================================

    def page_header(
        self,
        title,
        subtitle,
        active
    ):

        self.set_active(active)

        frame = tk.Frame(
            self.main,
            bg=BG
        )

        frame.pack(
            fill="x",
            padx=38,
            pady=(28, 18)
        )

        tk.Label(
            frame,
            text=title,
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 25, "bold")
        ).pack(anchor="w")

        tk.Label(
            frame,
            text=subtitle,
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 10)
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

    # =====================================
    # DASHBOARD
    # =====================================

    def show_dashboard(self):

        self.clear_main()

        self.page_header(
            "Good morning, Alex 👋",
            "Here's what's happening with your capstone project today.",
            "Dashboard"
        )

        tasks = list(
            self.manager.tasks.values()
        )

        total = len(tasks)

        completed = sum(
            1 for task in tasks
            if task.completed
        )

        pending = total - completed

        high = sum(
            1 for task in tasks
            if str(task.priority) == "1"
        )

        cards = tk.Frame(
            self.main,
            bg=BG
        )

        cards.pack(
            fill="x",
            padx=38
        )

        self.card(
            cards,
            "Total Tasks",
            total,
            PURPLE,
            "▣"
        )

        self.card(
            cards,
            "Completed",
            completed,
            TEAL,
            "✓"
        )

        self.card(
            cards,
            "Pending",
            pending,
            ORANGE,
            "⌛"
        )

        self.card(
            cards,
            "High Priority",
            high,
            RED,
            "●"
        )

        lower = tk.Frame(
            self.main,
            bg=BG
        )

        lower.pack(
            fill="both",
            expand=True,
            padx=38,
            pady=28
        )

        # Progress
        progress_box = self.box(lower)

        progress_box.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        tk.Label(
            progress_box,
            text="Overall Progress",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 14, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(22, 8)
        )

        percent = 0

        if total > 0:
            percent = int(
                (completed / total) * 100
            )

        tk.Label(
            progress_box,
            text=f"{completed} of {total} tasks done",
            bg=WHITE,
            fg=MUTED,
            font=("Segoe UI", 10)
        ).pack(
            anchor="w",
            padx=25
        )

        progress_bg = tk.Frame(
            progress_box,
            bg="#E4E7F5",
            height=12
        )

        progress_bg.pack(
            fill="x",
            padx=25,
            pady=15
        )

        progress_bg.pack_propagate(False)

        tk.Frame(
            progress_bg,
            bg=PURPLE,
            width=max(
                1,
                int(400 * percent / 100)
            )
        ).pack(
            side="left",
            fill="y"
        )

        tk.Label(
            progress_box,
            text=f"{percent}%",
            bg=WHITE,
            fg=PURPLE,
            font=("Segoe UI", 12, "bold")
        ).pack(
            anchor="w",
            padx=25
        )

        # Quick actions
        quick = self.box(lower)

        quick.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 0)
        )

        tk.Label(
            quick,
            text="Quick Actions",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 14, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(22, 12)
        )

        self.action_button(
            quick,
            "→  Add New Task",
            self.add_task_window
        )

        self.action_button(
            quick,
            "→  Plan a Route",
            self.show_routes
        )

        self.action_button(
            quick,
            "→  View Statistics",
            self.show_statistics
        )

    # =====================================
    # CARD
    # =====================================

    def card(
        self,
        parent,
        title,
        value,
        color,
        icon
    ):

        frame = tk.Frame(
            parent,
            bg=WHITE,
            highlightbackground="#DCE3F5",
            highlightthickness=1
        )

        frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=6
        )

        tk.Label(
            frame,
            text=title,
            bg=WHITE,
            fg=MUTED,
            font=("Segoe UI", 10)
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 4)
        )

        row = tk.Frame(
            frame,
            bg=WHITE
        )

        row.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        tk.Label(
            row,
            text=str(value),
            bg=WHITE,
            fg=color,
            font=("Segoe UI", 25, "bold")
        ).pack(side="left")

        tk.Label(
            row,
            text=icon,
            bg="#F0EDFF",
            fg=color,
            font=("Segoe UI", 15, "bold"),
            padx=8,
            pady=5
        ).pack(side="right")

    # =====================================
    # BOX
    # =====================================

    def box(self, parent):

        return tk.Frame(
            parent,
            bg=WHITE,
            highlightbackground="#DCE3F5",
            highlightthickness=1
        )

    # =====================================
    # ACTION BUTTON
    # =====================================

    def action_button(
        self,
        parent,
        text,
        command
    ):

        tk.Button(
            parent,
            text=text,
            command=command,
            anchor="w",
            bg="#F7F8FD",
            fg=PURPLE,
            activebackground="#EDE9FF",
            activeforeground=PURPLE_DARK,
            bd=0,
            font=("Segoe UI", 10, "bold"),
            padx=18,
            pady=12,
            cursor="hand2"
        ).pack(
            fill="x",
            padx=25,
            pady=5
        )

    # =====================================
    # TASK PAGE
    # =====================================

    def show_tasks(self):

        self.clear_main()

        self.page_header(
            "Task Management",
            "Add, edit, delete, search, and complete your tasks.",
            "Tasks"
        )

        top = tk.Frame(
            self.main,
            bg=BG
        )

        top.pack(
            fill="x",
            padx=38,
            pady=(0, 15)
        )

        self.task_search_entry = tk.Entry(
            top,
            bg=WHITE,
            fg=TEXT,
            relief="flat",
            font=("Segoe UI", 11)
        )

        self.task_search_entry.pack(
            side="left",
            ipady=11,
            padx=(0, 10)
        )

        tk.Button(
            top,
            text="⌕ Search",
            command=self.refresh_tasks,
            bg="#E8E4FF",
            fg=PURPLE_DARK,
            bd=0,
            padx=20,
            pady=10,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        ).pack(side="left")

        tk.Button(
            top,
            text="+ Add Task",
            command=self.add_task_window,
            bg=PURPLE,
            fg=WHITE,
            activebackground=PURPLE_DARK,
            bd=0,
            padx=22,
            pady=10,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        ).pack(side="right")

        table_frame = tk.Frame(
            self.main,
            bg=WHITE
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=38,
            pady=(0, 30)
        )

        columns = (
            "id",
            "title",
            "priority",
            "status"
        )

        self.task_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.task_table.heading(
            "id",
            text="ID"
        )

        self.task_table.heading(
            "title",
            text="TASK"
        )

        self.task_table.heading(
            "priority",
            text="PRIORITY"
        )

        self.task_table.heading(
            "status",
            text="STATUS"
        )

        self.task_table.column(
            "id",
            width=70
        )

        self.task_table.column(
            "title",
            width=450
        )

        self.task_table.column(
            "priority",
            width=150
        )

        self.task_table.column(
            "status",
            width=150
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.task_table.yview
        )

        self.task_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.task_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.refresh_tasks()

        buttons = tk.Frame(
            self.main,
            bg=BG
        )

        buttons.place(
            relx=0.52,
            rely=0.91,
            anchor="center"
        )

        self.small_button(
            buttons,
            "✓ Complete",
            self.complete_selected,
            TEAL
        )

        self.small_button(
            buttons,
            "✕ Delete",
            self.delete_selected,
            RED
        )

    # =====================================
    # REFRESH TASKS
    # =====================================

    def refresh_tasks(self):

        if not hasattr(
            self,
            "task_table"
        ):
            return

        for item in self.task_table.get_children():
            self.task_table.delete(item)

        search_text = ""

        if hasattr(
            self,
            "task_search_entry"
        ):
            search_text = (
                self.task_search_entry
                .get()
                .lower()
                .strip()
            )

        for task_id, task in self.manager.tasks.items():

            name = str(task.name)

            if (
                search_text
                and search_text not in name.lower()
            ):
                continue

            priority = self.priority_text(
                task.priority
            )

            status = (
                "Done"
                if task.completed
                else "Pending"
            )

            self.task_table.insert(
                "",
                "end",
                iid=str(task_id),
                values=(
                    task_id,
                    name,
                    priority,
                    status
                )
            )

    # =====================================
    # PRIORITY TEXT
    # =====================================

    def priority_text(self, priority):

        if str(priority) == "1":
            return "High"

        if str(priority) == "2":
            return "Medium"

        if str(priority) == "3":
            return "Low"

        return str(priority)

    # =====================================
    # SMALL BUTTON
    # =====================================

    def small_button(
        self,
        parent,
        text,
        command,
        color
    ):

        tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg=WHITE,
            bd=0,
            padx=18,
            pady=8,
            font=("Segoe UI", 9, "bold"),
            cursor="hand2"
        ).pack(
            side="left",
            padx=5
        )

    # =====================================
    # ADD TASK WINDOW
    # =====================================

    def add_task_window(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Add New Task"
        )

        window.geometry(
            "400x350"
        )

        window.configure(
            bg=WHITE
        )

        window.resizable(
            False,
            False
        )

        tk.Label(
            window,
            text="Add New Task",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 18, "bold")
        ).pack(
            pady=(25, 20)
        )

        fields = tk.Frame(
            window,
            bg=WHITE
        )

        fields.pack(
            fill="x",
            padx=35
        )

        tk.Label(
            fields,
            text="Task ID",
            bg=WHITE,
            fg=TEXT
        ).pack(anchor="w")

        id_entry = tk.Entry(
            fields,
            font=("Segoe UI", 11)
        )

        id_entry.pack(
            fill="x",
            pady=(4, 12),
            ipady=5
        )

        tk.Label(
            fields,
            text="Task Name",
            bg=WHITE,
            fg=TEXT
        ).pack(anchor="w")

        name_entry = tk.Entry(
            fields,
            font=("Segoe UI", 11)
        )

        name_entry.pack(
            fill="x",
            pady=(4, 12),
            ipady=5
        )

        tk.Label(
            fields,
            text="Priority (1 = High, 2 = Medium, 3 = Low)",
            bg=WHITE,
            fg=TEXT
        ).pack(anchor="w")

        priority_entry = tk.Entry(
            fields,
            font=("Segoe UI", 11)
        )

        priority_entry.pack(
            fill="x",
            pady=(4, 18),
            ipady=5
        )

        def save():

            try:

                task_id = int(
                    id_entry.get()
                )

                name = (
                    name_entry
                    .get()
                    .strip()
                )

                priority = int(
                    priority_entry.get()
                )

                if not name:

                    messagebox.showerror(
                        "Error",
                        "Please enter a task name."
                    )

                    return

                if priority not in [1, 2, 3]:

                    messagebox.showerror(
                        "Error",
                        "Priority must be 1, 2, or 3."
                    )

                    return

                self.manager.add_task(
                    task_id,
                    name,
                    priority
                )

                window.destroy()

                self.show_tasks()

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Task ID and priority must be numbers."
                )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

        tk.Button(
            window,
            text="Add Task",
            command=save,
            bg=PURPLE,
            fg=WHITE,
            bd=0,
            padx=30,
            pady=10,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        ).pack()

    # =====================================
    # SELECTED TASK
    # =====================================

    def selected_id(self):

        selected = self.task_table.selection()

        if not selected:

            messagebox.showwarning(
                "Select Task",
                "Please select a task first."
            )

            return None

        return selected[0]

    # =====================================
    # COMPLETE TASK
    # =====================================

    def complete_selected(self):

        task_id = self.selected_id()

        if task_id is None:
            return

        try:

            self.manager.complete_task(
                int(task_id)
            )

            self.show_tasks()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =====================================
    # DELETE TASK
    # =====================================

    def delete_selected(self):

        task_id = self.selected_id()

        if task_id is None:
            return

        answer = messagebox.askyesno(
            "Delete Task",
            "Are you sure you want to delete this task?"
        )

        if answer:

            try:

                self.manager.delete_task(
                    int(task_id)
                )

                self.show_tasks()

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

    # =====================================
    # PRIORITY SCHEDULE
    # =====================================

    def show_schedule(self):

        self.clear_main()

        self.page_header(
            "Priority Schedule",
            "Tasks arranged according to priority.",
            "Priority Schedule"
        )

        box = self.box(
            self.main
        )

        box.pack(
            fill="both",
            expand=True,
            padx=38,
            pady=(0, 30)
        )

        tk.Label(
            box,
            text="Priority Queue",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 15, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(22, 10)
        )

        text = tk.Text(
            box,
            bg="#FAFBFF",
            fg=TEXT,
            font=("Consolas", 10),
            bd=0,
            padx=20,
            pady=20
        )

        text.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=15
        )

        try:

            import io
            import contextlib

            output = io.StringIO()

            with contextlib.redirect_stdout(
                output
            ):

                self.scheduler.priority_schedule(
                    self.manager.tasks
                )

            result = output.getvalue()

            if result.strip():

                text.insert(
                    "1.0",
                    result
                )

            else:

                text.insert(
                    "1.0",
                    "No schedule output."
                )

        except Exception as e:

            text.insert(
                "1.0",
                str(e)
            )

        text.config(
            state="disabled"
        )

    # =====================================
    # DEPENDENCIES
    # =====================================

    def show_dependencies(self):

        self.clear_main()

        self.page_header(
            "Task Dependencies",
            "Manage dependencies using the graph structure.",
            "Dependencies"
        )

        box = self.box(
            self.main
        )

        box.pack(
            fill="both",
            expand=True,
            padx=38,
            pady=(0, 30)
        )

        tk.Label(
            box,
            text="Graph & Dependencies",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 15, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(22, 10)
        )

        info = (
            "The graph module handles task dependencies.\n\n"
            "DSA algorithms used in this project:\n\n"
            "• Adjacency List\n"
            "• BFS\n"
            "• DFS\n"
            "• Cycle Detection\n"
            "• Topological Sort\n"
            "• Dependency Management"
        )

        tk.Label(
            box,
            text=info,
            justify="left",
            bg=WHITE,
            fg=MUTED,
            font=("Segoe UI", 11)
        ).pack(
            anchor="w",
            padx=25,
            pady=15
        )

    # =====================================
    # GOOGLE MAP STYLE ROUTE PLANNER
    # =====================================

    def show_routes(self):

        self.clear_main()

        self.page_header(
            "Route Planner",
            "Find and visualize routes between locations.",
            "Route Planner"
        )

        # Main route area
        route_area = tk.Frame(
            self.main,
            bg=BG
        )

        route_area.pack(
            fill="both",
            expand=True,
            padx=38,
            pady=(0, 30)
        )

        # =================================
        # LEFT MAP
        # =================================

        map_frame = tk.Frame(
            route_area,
            bg=WHITE,
            highlightbackground="#DCE3F5",
            highlightthickness=1
        )

        map_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 12)
        )

        self.map_widget = TkinterMapView(
            map_frame,
            width=650,
            height=520,
            corner_radius=0
        )

        self.map_widget.pack(
            fill="both",
            expand=True
        )

        # Starting position
        self.map_widget.set_position(
            32.1617,
            74.1883
        )

        self.map_widget.set_zoom(
            12
        )

        # =================================
        # RIGHT PANEL
        # =================================

        panel = tk.Frame(
            route_area,
            bg=WHITE,
            width=300,
            highlightbackground="#DCE3F5",
            highlightthickness=1
        )

        panel.pack(
            side="right",
            fill="y"
        )

        panel.pack_propagate(
            False
        )

        tk.Label(
            panel,
            text="Plan Your Route",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=22,
            pady=(25, 5)
        )

        tk.Label(
            panel,
            text="Search two locations",
            bg=WHITE,
            fg=MUTED,
            font=("Segoe UI", 9)
        ).pack(
            anchor="w",
            padx=22,
            pady=(0, 20)
        )

        # Start
        tk.Label(
            panel,
            text="●  START LOCATION",
            bg=WHITE,
            fg=TEAL,
            font=("Segoe UI", 9, "bold")
        ).pack(
            anchor="w",
            padx=22
        )

        start_entry = tk.Entry(
            panel,
            bg="#F7F8FD",
            fg=TEXT,
            relief="flat",
            font=("Segoe UI", 10)
        )

        start_entry.pack(
            fill="x",
            padx=22,
            pady=(5, 15),
            ipady=10
        )

        # Destination
        tk.Label(
            panel,
            text="●  DESTINATION",
            bg=WHITE,
            fg=PURPLE,
            font=("Segoe UI", 9, "bold")
        ).pack(
            anchor="w",
            padx=22
        )

        destination_entry = tk.Entry(
            panel,
            bg="#F7F8FD",
            fg=TEXT,
            relief="flat",
            font=("Segoe UI", 10)
        )

        destination_entry.pack(
            fill="x",
            padx=22,
            pady=(5, 20),
            ipady=10
        )

        # Route button
        tk.Button(
            panel,
            text="Find Route  →",
            command=lambda: self.find_map_route(
                start_entry.get(),
                destination_entry.get(),
                result_label
            ),
            bg=PURPLE,
            fg=WHITE,
            activebackground=PURPLE_DARK,
            bd=0,
            font=("Segoe UI", 10, "bold"),
            pady=11,
            cursor="hand2"
        ).pack(
            fill="x",
            padx=22
        )

        # Clear
        tk.Button(
            panel,
            text="Clear Map",
            command=self.clear_map,
            bg="#E9F8F6",
            fg=TEAL,
            activebackground="#D7F1ED",
            bd=0,
            font=("Segoe UI", 9, "bold"),
            pady=9,
            cursor="hand2"
        ).pack(
            fill="x",
            padx=22,
            pady=8
        )

        # Result
        tk.Label(
            panel,
            text="ROUTE INFORMATION",
            bg=WHITE,
            fg=MUTED,
            font=("Segoe UI", 9, "bold")
        ).pack(
            anchor="w",
            padx=22,
            pady=(25, 8)
        )

        result_label = tk.Label(
            panel,
            text="Enter locations above\nand click Find Route.",
            bg="#F7F8FD",
            fg=MUTED,
            justify="left",
            anchor="nw",
            font=("Segoe UI", 10),
            padx=15,
            pady=15
        )

        result_label.pack(
            fill="x",
            padx=22
        )

        # DSA information
        tk.Label(
            panel,
            text="DSA CONNECTION",
            bg=WHITE,
            fg=MUTED,
            font=("Segoe UI", 9, "bold")
        ).pack(
            anchor="w",
            padx=22,
            pady=(25, 8)
        )

        tk.Label(
            panel,
            text="Graph → Shortest Path\nDijkstra → Route Calculation",
            bg="#EEF8F7",
            fg="#168C7D",
            justify="left",
            anchor="w",
            font=("Segoe UI", 9, "bold"),
            padx=15,
            pady=12
        ).pack(
            fill="x",
            padx=22
        )

    # =====================================
    # FIND MAP ROUTE
    # =====================================

    def find_map_route(
        self,
        start,
        destination,
        result_label
    ):

        start = start.strip()
        destination = destination.strip()

        if not start or not destination:

            messagebox.showwarning(
                "Missing Location",
                "Please enter both locations."
            )

            return

        try:

            # Search start location
            start_position = (
                self.map_widget.set_address(
                    start,
                    marker=True
                )
            )

            # Search destination
            destination_position = (
                self.map_widget.set_address(
                    destination,
                    marker=True
                )
            )

            if (
                start_position is None
                or destination_position is None
            ):

                messagebox.showerror(
                    "Location Error",
                    "Could not find one of the locations."
                )

                return

            # Draw route line
            self.map_widget.set_path(
                [
                    start_position,
                    destination_position
                ]
            )

            # Move map to route
            self.map_widget.fit_bounding_box(
                (
                    start_position,
                    destination_position
                )
            )

            result_label.config(
                text=(
                    "START\n"
                    f"{start}\n\n"
                    "DESTINATION\n"
                    f"{destination}\n\n"
                    "✓ Route displayed on map"
                ),
                fg=TEXT
            )

        except Exception as e:

            messagebox.showerror(
                "Map Error",
                str(e)
            )

    # =====================================
    # CLEAR MAP
    # =====================================

    def clear_map(self):

        if hasattr(
            self,
            "map_widget"
        ):

            self.map_widget.delete_all_marker()

            self.map_widget.delete_all_path()

    # =====================================
    # SEARCH
    # =====================================

    def show_search(self):

        self.clear_main()

        self.page_header(
            "Search Tasks",
            "Quickly find a task using its ID or name.",
            "Search"
        )

        box = self.box(
            self.main
        )

        box.pack(
            fill="both",
            expand=True,
            padx=38,
            pady=(0, 30)
        )

        search_entry = tk.Entry(
            box,
            font=("Segoe UI", 12),
            bg="#F8F9FE",
            fg=TEXT,
            relief="flat"
        )

        search_entry.pack(
            fill="x",
            padx=25,
            pady=(25, 10),
            ipady=12
        )

        result = tk.Text(
            box,
            bg="#FAFBFF",
            fg=TEXT,
            bd=0,
            font=("Segoe UI", 11)
        )

        result.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=15
        )

        def search():

            result.delete(
                "1.0",
                "end"
            )

            value = (
                search_entry
                .get()
                .strip()
            )

            if not value:

                result.insert(
                    "1.0",
                    "Enter a task ID or task name."
                )

                return

            try:

                task_id = int(value)

                if hasattr(
                    self.manager,
                    "search_task"
                ):

                    found = (
                        self.manager
                        .search_task(task_id)
                    )

                    result.insert(
                        "1.0",
                        str(found)
                    )

                else:

                    result.insert(
                        "1.0",
                        "search_task() was not found."
                    )

            except ValueError:

                found = []

                for task in self.manager.tasks.values():

                    if value.lower() in str(
                        task.name
                    ).lower():

                        found.append(
                            f"ID: {task.task_id}\n"
                            f"Task: {task.name}\n"
                            f"Priority: "
                            f"{self.priority_text(task.priority)}\n"
                            f"Status: "
                            f"{'Done' if task.completed else 'Pending'}\n"
                            f"{'-' * 35}\n"
                        )

                if found:

                    result.insert(
                        "1.0",
                        "\n".join(found)
                    )

                else:

                    result.insert(
                        "1.0",
                        "No matching task found."
                    )

        tk.Button(
            box,
            text="Search",
            command=search,
            bg=PURPLE,
            fg=WHITE,
            bd=0,
            padx=25,
            pady=9,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        ).pack(
            anchor="e",
            padx=25
        )

    # =====================================
    # HISTORY
    # =====================================

    def show_history(self):

        self.clear_main()

        self.page_header(
            "History",
            "Undo and redo information.",
            "History"
        )

        box = self.box(
            self.main
        )

        box.pack(
            fill="both",
            expand=True,
            padx=38,
            pady=(0, 30)
        )

        undo = getattr(
            self.manager,
            "undo_stack",
            []
        )

        redo = getattr(
            self.manager,
            "redo_stack",
            []
        )

        text = tk.Text(
            box,
            bg="#FAFBFF",
            fg=TEXT,
            bd=0,
            font=("Consolas", 10),
            padx=20,
            pady=20
        )

        text.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        text.insert(
            "1.0",
            f"UNDO STACK\n"
            f"{'=' * 40}\n"
            f"{undo}\n\n"
            f"REDO STACK\n"
            f"{'=' * 40}\n"
            f"{redo}"
        )

        text.config(
            state="disabled"
        )

    # =====================================
    # STATISTICS
    # =====================================

    def show_statistics(self):

        self.clear_main()

        self.page_header(
            "Task Statistics",
            "A simple overview of your current tasks.",
            "Statistics"
        )

        tasks = list(
            self.manager.tasks.values()
        )

        total = len(tasks)

        completed = sum(
            1 for task in tasks
            if task.completed
        )

        pending = total - completed

        high = sum(
            1 for task in tasks
            if str(task.priority) == "1"
        )

        medium = sum(
            1 for task in tasks
            if str(task.priority) == "2"
        )

        low = sum(
            1 for task in tasks
            if str(task.priority) == "3"
        )

        box = self.box(
            self.main
        )

        box.pack(
            fill="both",
            expand=True,
            padx=38,
            pady=(0, 30)
        )

        data = [
            ("Total Tasks", total, PURPLE),
            ("Completed", completed, TEAL),
            ("Pending", pending, ORANGE),
            ("High Priority", high, RED),
            ("Medium Priority", medium, ORANGE),
            ("Low Priority", low, TEAL)
        ]

        for i, (
            title,
            value,
            color
        ) in enumerate(data):

            row = i // 3
            col = i % 3

            item = tk.Frame(
                box,
                bg="#FAFBFF"
            )

            item.grid(
                row=row,
                column=col,
                padx=15,
                pady=15,
                sticky="nsew"
            )

            tk.Label(
                item,
                text=title,
                bg="#FAFBFF",
                fg=MUTED,
                font=("Segoe UI", 10)
            ).pack(
                pady=(18, 3)
            )

            tk.Label(
                item,
                text=str(value),
                bg="#FAFBFF",
                fg=color,
                font=("Segoe UI", 24, "bold")
            ).pack(
                pady=(0, 18)
            )

        for i in range(3):

            box.grid_columnconfigure(
                i,
                weight=1
            )

    # =====================================
    # RUN
    # =====================================

    def run(self):

        self.root.mainloop()


# =========================================
# TEST RUN
# =========================================

if __name__ == "__main__":

    from task_manager import TaskManager
    from scheduler import Scheduler

    manager = TaskManager()
    scheduler = Scheduler()

    root = tk.Tk()

    app = SmartPlannerGUI(
        root,
        manager,
        scheduler
    )

    app.run()