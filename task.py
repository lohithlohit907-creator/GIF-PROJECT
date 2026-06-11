import json
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
        if index < 0 or index >= len(self.tasks):
            self.tasks.pop(index)

        else:    
            raise IndexError("task index out of range")
            
        
            

    def complete_task(self,index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete_task()
        else:
            print(f"invalid index {index}")    
            

    def save_tasks(self):
        data=[]

        for task in self.tasks:
            task_data={
                "title":task.title,
                "due_date":task.due_date,
                "completed":task.completed
            }

            data.append(task_data)
        
            with open("tasksdata.json","w") as file:
                json.dump(data,file,indent=4)
        


    def load_tasks(self):
            
        try:    
            with open("tasksdata.json","r") as file:
                data=json.load(file)

            for task_data in data:
                    title=task_data["title"]
                    due_date=task_data["due_date"]    
                    completed=task_data["completed"]

                    task=Task(title,due_date)

                    if completed:
                        task.complete_task()
            
                    self.tasks.append(task)    

        except FileNotFoundError:
            pass
    # def search_task(self):
    #     title=input("enter the task title to search:")        
    #     for title in data

manager=TaskManager() 
manager.load_tasks()
while True:
    print("MENU")
    print("1-->Add Task")
    print("2-->view Task")
    print("3-->Delete Task")
    print("4-->Save Task")
    print("5-->complete Task")
    print("6-->exit")
# ---------------------ADD TASK---------------------
    try:
        choice=int(input("enter your choice:"))
    except ValueError:
        print("please enter a number ")  
        continue  
    if choice==1:
                try:
                    title=input("enter title of the task:")
                    due_date=(input("enter due date of the task(DD/MM/YYYY):"))
                    datetime.strptime(due_date,"%d-%m-%Y")
                    task=Task(title,due_date)

                    manager.add_task(task)
                    manager.save_tasks()
                    print("task added and saved")

                except ValueError:
                    print("date must be DD-MM-YYYY format")    
# ---------------------VIEW TASK---------------------
    elif choice==2:
            manager.view_tasks()    
# --------------------DELETE TASK----------------------

    elif choice==3:
                try:
                    index=input("enter the task number to delete task:")
                    manager.delete_task(index)
                    manager.save_tasks()
                    print("Task deleted")

                except ValueError:
                    print("please enter a number")    

                except IndexError:
                    print("please enter valid index number")

        # ====================SAVE TASK===================
    elif choice==4:
                manager.save_tasks()    
                print("Task Saved")
        # =================COMPLETE  TASK==================
    elif choice==5:
                try:
                    index=int(input("enter the task number to complete task:"))
                    manager.complete_task(index)
                    manager.save_tasks()
                    print("task completed and saved")

                except ValueError:
                    print("please enter a number")

                except IndexError:
                    print("please enter valid index number")

        # ====================EXIT========================
    elif choice==6:    
                print("Thank you")    
                break







          










