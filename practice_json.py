import json
with open("task.json","r") as file:
    task_dict=json.load(file)
    print(task_dict)

for options in task_dict:
    print(options)


data=[

    {
        "title":"gym",
        "due_date":"15-7-2026",
        "completed":False
        
        },

    {
        "title":"gym",
        "due_date":"20-07-2026",
        "completed":False

    }    
]
