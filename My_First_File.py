tasks = []

while True:
    print("\n📚 Smart Study Planner")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter study task: ")
        time = input("Enter time (e.g. 5pm): ")
        tasks.append({"task": task, "time": time})
        print("✅ Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t['task']} at {t['time']}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t['task']}")
            num = int(input("Enter task number to delete: "))
            if 0 < num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"❌ Removed: {removed['task']}")
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice!")