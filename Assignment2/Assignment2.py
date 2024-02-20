"""
Assignment 2: To-Do List Manager
Create a Python script that implements a simple to-do list manager.
Allow users to add tasks, mark tasks as completed, and remove tasks.
Store the tasks in a list of dictionaries where each dictionary represents a task with keys like 'task_name', 'priority', 'completed', etc.
Provide a menu-driven interface for users to interact with the to-do list.
"""
def add(List):
    name=input("Enter task name : ")
    prioty=int(input("Enter priority : "))
    task=input("Task Completed Enter Yes,No : ")
    s={name,prioty,task}
    List.append(s)

def tas(List):
    i=int(input("Enter index: "))
    l=List[i]
    print(l)
    k=list(l)
    if k[1]=="Yes":
        print("Task Successful")

def show(List):
    print(List)

def main():
    List=[]
    while True:
        print("1.Add Task")
        print("2.mark tasks as completed")
        print("3.show task")
        choice=int(input("Enter number : "))
        if(1==choice):
            add(List)
        elif(2==choice):
            tas(List)
        elif(3==choice):
            show(List)
            

if __name__ == "__main__":
    main()


