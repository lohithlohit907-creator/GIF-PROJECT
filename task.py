import json
from datetime import datetime
# ===================tasknotfounderror==================?
class TasknotfoundError(Exception):
     
     def __init__(self,task_id):
          self.task_id=task_id

          super().__init__(f"task {task_id} not found")
# ==============invalidmenuchoiceerror=================
class InvalidMenuChoiceError(Exception):
     
     def __init__(self, choice):
          self.choice=choice

          super().__init__(f"invalid menu choice:{choice}")

# ================invalid index error=========================
class InvalidIndexIDError(Exception):
     
     def __init__(self, index):
          self.index = index

          super().__init__(f" Error:Invalid Index ID {index} ")
# =====================================================================
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
        if index<0 or index >= len(self.tasks):
            raise TasknotfoundError (index)
        
        self.tasks.pop(index)
            
    
    def complete_task(self,index):
        if index <0 or index >= len(self.tasks):
            raise TasknotfoundError(index)
        
            

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
# ________________________________________________________________________
    try:
        choice=int(input("enter your choice:"))
        if choice < 0 or choice >6:
            raise InvalidMenuChoiceError(choice) 

    except InvalidMenuChoiceError as e:
         print(e)
    
# ---------------------ADD TASK---------------------
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
                    index=int(input("enter task id:"))


                except TasknotfoundError as e:
                     print (e)    

                except InvalidIndexIDError as e:
                     print(e)

                else :
                     manager.delete_task(index)    
                     manager.save_tasks() 
                     print("task deleted")
# ===================================SAVE TASK===================
    elif choice==4:
                manager.save_tasks()    
                print("Task Saved")
# ====================COMPLETE  TASK==================
    elif choice==5:
                try:
                    index=int(input("enter the task id to complete task:"))
                    

                except TasknotfoundError as e:
                    print(e)

                except InvalidIndexIDError as e:
                    print(e)

                else:
                     
                     manager.complete_task(index)    
                     manager.save_tasks()
                     print("task completed and saved")

        # ====================EXIT========================
    elif choice==6:    
                print("Thank you")    
                break







          










