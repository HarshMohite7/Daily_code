# 1. Add task
# 2. Delete task
# 3. Rename task
# 4. Mark task complete
# 5. Show tasks
# 6. Show pending vs completed



# add_task()
# delete_task()
# rename_task()
# mark_complete()           this are going to me my function
# show_tasks()


Goals = ("TODAYS GOALS (AIM's) ")    # input from user

tasks = {}                                             # Empty dictionary

def add_task():                                         # function is define
    
    task_name = input("Enter task:")
    task_id = len(tasks) + 1
    tasks[task_id] = {
        
    "title": task_name,
    "done": False
}
    
    print(tasks)
add_task()                                              # we called the function

# we have just brush up the functions and uers input

