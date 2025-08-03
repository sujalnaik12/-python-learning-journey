tasks = []

while True:
  print("\nTo-Do List:")
  for i, task in enumerate(tasks, start= 1):
    print(f"{i}. {task}")

  print("\n Options: add / remove / exit")
  action = input("What do you want to do? ").lower()

  if action == 'add':
    new_task = input("Enter new task: ")
    tasks.append(new_task)
  elif action == 'remove':
    task_num = int(input("Enter task number to remove: "))
    if 1 <= task_num <= len(tasks):
      tasks.pop(task_num - 1)
    else:
      print("Invalid task number.")
  elif action =='exit':
    break
  else:
    print("Invalid option. Please try again.")