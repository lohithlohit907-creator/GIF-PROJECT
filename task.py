from datetime import datetime



class Task:
    def __init__(self,title,due_date):
        self.title=title
        self.due_date=due_date
        self.__completed=False

    @property
    def completed(self):
        return self.__completed    
    
    def complete_task(self):
        self.__completed=True

    def due_status(self):
        today= datetime.now()
        due_date=datetime.strptime(
             self.due_date,
             "%d-%m-%Y"
         )
        difference=due_date - today    
        if difference.days==0:
            return ("due today")  
        elif difference.days > 0:
             return (f"{difference.days} days left")
        elif difference.days < 0 :
             return ("overdue") 

    def __str__(self):
        status="completed" if self.__completed else "pending" 
        return f"{self.title}|{self.due_date}|{status}|{self.due_status()}"    
    
    def __repr__(self):
        return f"Task('{self.title}','{self.due_date}')"
    
    
         
class TaskManager:
    def __init__(self):
        self.tasks=[]

    def add_task(self,task):
        self.tasks.append(task)
            
    def view_tasks(self):
        if not self.tasks:
            print("no tasks found")    
            return
        
        for index,task in enumerate(self.tasks):
            print(index,task)

    def delete_task(self,index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print(f"sorry {index} cannot excits ")    
            

    def complete_task(self,index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete_task()
        else:
            print(f"invalid index {index}")    
            


    def save_tasks(self):
            with open("taskmanager.txt","w") as file:
                for task in self.tasks:
                    file.write(f"{str(task)}\n")    


    def load_task(self):
        try:
            with open("taskmanager.txt","r") as file:
                for line in file:
                    newline=line.strip()
                    title,due_date,status=newline.split("|")
                    task=Task(title,due_date)
                    if status=="completed":
                        task.complete_task() 
                    self.tasks.append(task)
        except FileNotFoundError:
            pass

manager=TaskManager() 
manager.load_task()
while True:
    print("MENU")
    print("1-->Add Task")
    print("2-->view Task")
    print("3-->Delete Task")
    print("4-->Save Task")
    print("5-->complete Task")
    print("6-->exit")

    choice=input("enter your choice:")
    if choice=="1":
        title=input("enter title of the task:")
        due_date=input("enter due date of the task:")
        task=Task(title,due_date)
        manager.add_task(task)

    elif choice=="2":
        manager.view_tasks()    

    elif choice=="3":
        index=int(input("enter the task number to delete task:"))    
        manager.delete_task(index)
        print("Task deleted")

    elif choice=="4":
        manager.save_tasks()    
        print("Task Saved")

    elif choice=="5":
        index=int(input("enter the task number to complete task:"))
        manager.complete_task(index)

    elif choice=="6":
        manager.save_tasks()    

        print("Thank you")    
        break







          










