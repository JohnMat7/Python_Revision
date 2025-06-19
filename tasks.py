import json
from datetime import datetime
import logging

logging.basicConfig(filename='error.log',
                    filemode='a' , 
                    format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG)


def load_tasks():
    with open("tasks.json" , "r") as file:
        current_task_list = json.load(file)
        print("Hi John you have following task today : ")
        i = 0
        for i in current_task_list:
            print (f"Your taks no. {i+1} is : ",i)   


def add_tasks(task , task_time):
    current_time = datetime.now().strftime("%H:%M %p")
    task_time = task_time.strftime("%H:%M %p")
    
    new_task = {
            "Task Timing" : task_time , "Task" : task , "When task was added to schedule" : current_time , "status" : False
        }
    
    try:
        with open ("tasks.json","r") as file:
            tasks = json.load(file)
            tasks.append(new_task)
            print("Print Task inside try catch in tasks.py and task:")

    except (FileNotFoundError , json.JSONDecodeError) as e:
        logging.error("Error occured while loading tasks.json : %s",e)
        tasks = []
        

    
    with open ("tasks.json","w") as file:
        json.dump(new_task,file, indent=4)



