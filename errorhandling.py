# # class you_are_poor_Error(Exception):
# #     pass

# # try:
# #     amount=int(input("enter your networth$:"))
# # except ValueError:
# #     print("please enter number ")    
    
# # try:
# #     if amount < 10000000:
# #         raise you_are_poor_Error("you are poor you need more networth to become rich")


# # except you_are_poor_Error as e:
# #     print("Low networth Error:",e)

# class TaskNotFoundError(Exception):
#     pass

# try:
#     raise TaskNotFoundError("Task does not exist")

# except Exception as e:
#     print("General:", e)

# except TaskNotFoundError:
#     print("Task Error")

# print("Done")
# try:
#     x = int("abc")

# except ValueError:
#     print("Value Error")

# except Exception:
#     print("General Error")

# try:
#     password = input("enter password:")
    
#     if password !="lohith2007":
#         raise ValueError ("wrong password")
    
# except ValueError as e:
#     print("Error:",e) 

# else:
#     print ("login sussesfull")    
          
# finally:
#     print("thank you")          
    
# try:
#     print("A")
#     x = 10 / 0

# except ValueError:
#     print("B")

# except ZeroDivisionError:
#     print("C")

# else:
#     print("D")

# finally:
#     print("E")

# print("F")
# class DatabaseError(Exception):
#     pass


# try:
#     amount= int("bhoj")

# except ValueError as e:
#     raise DatabaseError(
#         "operatio failed"
#     )    from e 


class TaskNotFoundError(Exception):

    def __init__(self, task_id):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} not found"
        )

try:
    raise TaskNotFoundError(25)

except TaskNotFoundError as e:
    print(type(e))




