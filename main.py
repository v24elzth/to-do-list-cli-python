'''
Mini Project Mid-Term 1
To Do List
'''

def view_tasks(tasks):
    if len(tasks) == 0:
        print("You have no task available yet")
        add_tasks(tasks) # to check, If empty, it prints a message that there are no tasks available, and call add task function
        print()
    else:
        print("your task:")  # if not empty, it prints a header that the task will be displayed
        for i in range(len(tasks)): # then loops through the tasks list using a for loop, 
            print(f"{i+1}. {tasks[i][0]} - deadline: {tasks[i][1]}") # and prints each task with its corresponding number (starting from 1).

def add_tasks(tasks):
    while True:
        new_task = input("add your new task: ")
        if new_task == '':
            print('Your task is invalid, please try again')
            continue
        for character in new_task:
            if character in '0123456789':
                print('Your task is invalid, please try again')
                break
        else:
            if any(task[0] == new_task for task in tasks):
                print("Task already added")
            else:
                deadline_date = input("Enter the deadline date: ")
                while deadline_date == '':
                    print("Deadline date cannot be empty, please try again")
                    deadline_date = input("Enter the deadline date: ")
                deadline_time = input("Enter the deadline time: ")
                while deadline_time == '':
                    print("Deadline time cannot be empty, please try again")
                    deadline_time = input("Enter the deadline time: ")
                tasks.append([new_task, f"{deadline_date} {deadline_time}"])
                print(f"Task '{new_task}' will be due at {deadline_date} {deadline_time}.")
                break

def delete_tasks(tasks):
    if len(tasks) == 0: # checks if empty then prints that there are no tasks to delete.
        print("You have no task to delete")
        return # to stop the loop
    while True: # then enters a while loop that continues until the user enters a valid task number to delete.
        view_tasks(tasks)
        task_number = input("Enter the task number to delete: ") #ask user to enter the task number to delete using the input function
        if task_number == "":
            print("invalid input, please enter a number")
        else:
            for character in task_number:
                if character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    print("invalid input, please enter a number")
                    break
            else:
                task_number = int(task_number)
                if 1 <= task_number <= len(tasks):
                    delete_tasks = tasks.pop(task_number - 1) # to checks if the entered task number is valid like between 1 and the length of the tasks list,  deletes the task using the pop method and prints a message indicating that the task has been deleted.
                    view_tasks(tasks)
                    print(f"Task '{delete_tasks[0]}' deleted.")
                    break  # stop the loop                                   
                else: # If invalid, prints an error message and continue the next loop.
                    print("invalid task number, please try again")

def main():
    tasks = [] # empty tasks list that need to be filled
    print('Welcome to the "To-Do List!"') # prints a welcome message to the user.
    while True: # enters a while loop that continues until the user chooses to quit.
        print()
        print("\n---To Do List---")
        print("1. View tasks")
        print("2. Add tasks")
        print("3. Delete tasks")
        print("4. Quit")
        # displays a menu to the user
        
        choice = input("Select your option (1-4): ")
        # asks the user to enter their choice using input function.

        # to determine which function to call based on the user's choice.
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            delete_tasks(tasks)
        elif choice == "4":
            print("Goodbye!")
            break # if user choose to quit, it prints a goodbye message and exits the loop with break function.
        else:
            print("Invalid choice number, please try again")
            continue  # if invalid choice, prints an error message and continues to the next loop.

main()

