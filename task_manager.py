class Task:
    def __init__(self, task_id, title, description="", status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"[{self.task_id}] {self.title} ({self.status}) - {self.description}"


tasks = []
next_id = 1

def create_task():
    global next_id
    title = input("Task title: ")
    desc = input("Description: ")
    tasks.append(Task(next_id, title, desc))
    print(f"Task {next_id} created.")
    next_id += 1

def read_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        print(t)

def update_task():
    tid = int(input("Task ID to update: "))
    for t in tasks:
        if t.task_id == tid:
            t.title = input(f"New title (was '{t.title}'): ") or t.title
            t.description = input("New description: ") or t.description
            t.status = input("New status (Pending/Done): ") or t.status
            print("Updated.")
            return
    print("Task not found.")

def delete_task():
    tid = int(input("Task ID to delete: "))
    global tasks
    before = len(tasks)
    tasks = [t for t in tasks if t.task_id != tid]
    print("Deleted." if len(tasks) < before else "Task not found.")

def menu():
    while True:
        print("\n1.Create 2.Read 3.Update 4.Delete 5.Exit")
        choice = input("Choose: ")
        if choice == "1": create_task()
        elif choice == "2": read_tasks()
        elif choice == "3": update_task()
        elif choice == "4": delete_task()
        elif choice == "5": break
        else: print("Invalid choice.")

if __name__ == "__main__":
    menu()
