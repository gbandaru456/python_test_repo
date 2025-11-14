

def add_task(tasks):
    task=input('enter your task here :').strip()
    tasks.append(task)
    print('you have added a new task')
def view_tasks(task):
    if not task:
        print('there is no tasks recorded')
    else:
        for i, all_tasks in enumerate (task,1):
            print(f'view tasks are: {i}. {all_tasks}')
def del_task(tasks):
    view_tasks(tasks)
    try:
        task_num=int(input('enter your task numner to deletec : '))
        if 1<=task_num<=len(tasks):
            removed_task=tasks.pop(task_num-1)
            print(f'delete task is {removed_task}')
        else:
            print('Invalid task number')
    except ValueError:
        print('Please enter a valid number')   

def main():
    tasks =[]
    while True:
        print("This is To-do-list ")
        print("1.Add a new task")
        print("2.view a task")
        print("3.delete a task")
        print("4.exit")
        choice = input('choose your choice (1 to 4) : ')
        if choice=='1':
            add_task(tasks)
        elif choice=='2':
            view_tasks(tasks)
        elif choice=='3':
            del_task(tasks)
        elif choice=='4':
            print('Good bye')
            break
        else:
            print('you have choosen invalid option.please try after some time')
if __name__=='__main__':
    main()