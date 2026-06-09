-----------------project 1-------------------
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __str__(self):
        return f"hi {self.name} you got {self.marks} marks "
s1=Student("lohith",90)
print(s1)

# -------------------project2------------------
class Books:
    def __str__(self):
        return "Atomic Habbits"
    
b1=Books()
print(b1)
-------------------project3--------------------
class Bank:
    def __init__(self,balance):
        self.balance=balance

    def deposite(self):
        amount=int(input("enter amount to deposite:"))
        self.balance=self.balance + amount
        return self.balance
    def __str__(self):
        return self.balance
        
    def withdrawl(self):
        amount= int(input("enter amount to withdrawl:"))
        if amount>self.balance:
            print("insufficiant amount")
            # break
        elif amount<self.balance:
            self.balance=self.balance - amount
            return self.balance
        
    def __str__(self):
        return f"Balance:{self.balance}"    
b1=Bank(1000)
b1.deposite()

b1.withdrawl()

print(b1)

---------------------------------------------------
class Employee:
    total_employees=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.total_employees +=1

    @classmethod
    def show_accounts(cls):
        print(cls.total_employees)

e1=Employee("lohith",50000)
e2=Employee("Kushal",60000)

Employee.show_accounts()

# --------------my own ----------------------
class Animals:
    total_animals=0
    def __init__(self,name):
        self.name=name
        Animals.total_animals +=1
    @classmethod
    def show_animals(cls):
        print(cls.total_animals)

a1=Animals("deer")        
a2=Animals("tiger")
a3=Animals("lion")
a4=Animals("wolf")
Animals.show_animals()
-------------------------------------------
class Calculator:
    
    @staticmethod
    def add(a,b):
        return a+b    
    

print(Calculator.add(10,20))
------------------------------------------------
class Tempertaure:

    @staticmethod
    def celsius_to_farhanite(c):
        f=(9/5)*(c)+32
        return f
    


print(Tempertaure.celsius_to_farhanite(25))

-------------------------------------------------
inheritennce="get parent powers from parent class to child class"
overriding="change parent class method by inheritence"
super="get both parents and child class methods "

class vechile:
    def start(self):
        print("vechile started")


class car(vechile):
    def start(self):
        super().start()
        print("car started")

car1=car()
car1.start()
-----------------------------------------------------
class GameChanger:
    def __init__(self,name):
        self.name=name
        self.__health=100

    def take_damage(self,amount):
        self.__health=self.__health-amount  

    def show_health(self):
        print (f"health:{self.__health}")
    

g1=GameChanger("lohith")        
g1.take_damage(20)
g1.show_health()
print(g1._GameChanger__health)

------------------@property-----------------
class Student:
    def __init__(self):
        self.__marks=100

    @property
    def marks(self):
        return self.__marks    
    


s=Student()
print(s.marks)
-----------------------------------------------
__str__ : used to print the output that humans can read and easily understand
__repr__ : user to reperstent the output that progermers can understand and prints inside the list more cleaner
 

class Movie:
    def __init__(self,name,year):
        self.name=name
        self.year=year

    def __str__(self):
        return f"{self.name}({self.year})"    
    
    def __repr__(self):
        return f"Movie('{self.name}',{self.year})"
    

m1=Movie("oddessy",2026)
print(m1)
print([m1])

------------------tiny project 1---------------
class Bank:
    def __init__(self,name):
        self.name=name
        self.__balance=10000
    def deposite(self,amount):
        self.__balance=self.__balance+amount
        print(f"{amount}$:deposited")    

    def withdrawl(self,amount):
        self.__balance=self.__balance - amount
        print(f"{amount}$:withdrawn")

    def show_balance(self):
        return f"new balance :{self.__balance}"
    

b1=Bank("lohtith")
b1.deposite(2000)
b1.withdrawl(5000)
print(b1.show_balance())
-------------- project 2--------------------
class Library:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @property
    def borrowed_status(self):
        return False
    @property
    def borrow_book(self):
        return True

    def __str__(self):
        return f"{self.title}:{self.author}"    
    
    def __repr__(self):
        return f"Book('{self.title}','{self.author}')"
    
book1=Library("Rich dap Poor dad","Robert T Kiyosaki")
print(book1)
print([book1])
print(book1.borrowed_status)
print(book1.borrow_book)

---------------------------------------------
class Library:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.__borrowed=False

    @property
    def show_status(self):
        return self.__borrowed
    
    def borrow_book(self):
        self.__borrowed=True

    def return_book(self):
        self.__borrowed=False


    def __str__(self):
        status="borrowed " if self.__borrowed else "available"
        return f"{self.title} by {self.author} | {status}"
    
    def __repr__(self):
        return f"('{self.title}','{self.author}')"
    

book=Library("zero to one","peter thiel")
book.borrow_book()
print(book)
book.return_book()
print(book)
book.show_status

-----------------------------------------------
class Employee:
    total_employee=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        Employee.total_employee+=1

    @classmethod
    def show_details(cls):
        print(f"Total Employee:{cls.total_employee}")

    def __str__(self):
        return f"{self.name}-${self.salary}"    
    


e=Employee("lohith",1000000)
print(e)
ee=Employee("kushal",200000)
Employee.show_details()




class Task:
    def __init__(self,title,due_date):
        self.title=title
        self.due_date=due_date
        self.completed=False

task=Task("gym","20-6-2026")        
print({
    f"title:{task.title}",
    f"due_date:{task.due_date}",
    f"completed:{task.completed}"    
    })

{
    "title":"gym",
    "due_date":"15-07-2026",
    "completed":"True"    
    }

        










    

            
















        


