import argparse
import json
import shlex
import datetime

class Task:
    def __init__(self, id:int, description: str,
                 status:str, createdAt: datetime.date,
                 updatedAt: datetime.date):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

tasks: list[Task] = []
cur_index = 1


def save_tasks():
    global tasks
    data = []
    for task in tasks:
        data.append(
            {
                "id": task.id,
                "description": task.description,
                "status": task.status,
                "createdAt":task.createdAt.strftime("%Y-%m-%d"),
                "updatedAt": task.updatedAt.strftime("%Y-%m-%d")
            }
        )
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)



def load_tasks():
    global tasks, cur_index
    try:
        with open("tasks.json", "r",encoding="utf-8") as file:
            data = json.load(file)
        tasks = []
        for item in data:
            tasks.append(Task(item["id"], item["description"],
                              item["status"], datetime.date.fromisoformat(item["createdAt"]),
                              datetime.date.fromisoformat(item["updatedAt"])))
        if tasks:
            cur_index = max(task.id for task in tasks) + 1
        else:
            cur_index = 1

    except FileNotFoundError:
        tasks = []
        cur_index = 1


def list_action(args):
    if args.state == None:
        for task in tasks:
            print(f"id:{task.id} description: {task.description}, status:{task.status}, createdAt: {task.createdAt}, updatedAt:{task.updatedAt}")
    else:
        for task in tasks:
            if task.status == args.state:
                print(f"id:{task.id} description: {task.description}, status:{task.status}, createdAt: {task.createdAt}, updatedAt:{task.updatedAt}")


def add_action(args):
    global cur_index, tasks

    task = Task(cur_index, args.description[0],"todo" , datetime.date.today(), datetime.date.today())
    cur_index += 1
    tasks.append(task)
    save_tasks()


def update_action(args):
    global tasks
    for task in tasks:
        if task.id == int(args.id[0]):
            task.description = args.id[1]
            task.updatedAt = datetime.date.today()
    save_tasks()

def mark_done_action(args):
    global tasks
    for task in tasks:
        if task.id == int(args.id[0]):
            task.status = "done"
            task.updatedAt = datetime.date.today()

    save_tasks()


def mark_progress_action(args):
    global tasks
    for task in tasks:
        if task.id == int(args.id[0]):
            task.status = "in-progress"
            task.updatedAt = datetime.date.today()

    save_tasks()

def delete_action(args):
    global tasks
    tasks = list(filter(lambda x: x.id!= int(args.id[0]),tasks))
    save_tasks()



parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")
add_parser = subparsers.add_parser("add",help="add new task")
add_parser.add_argument("--description", nargs=1)
list_parser = subparsers.add_parser("list", help="list all tasks")
list_parser.add_argument("state", nargs="?", default=None)
list_parser.set_defaults(func = list_action)

#list_parser.set_defaults(func = list_done_action)


add_parser.set_defaults(func = add_action)
update_parser = subparsers.add_parser("update", help= "update the task")
update_parser.add_argument("id", nargs = 2)
update_parser.set_defaults(func = update_action)

mark_done_parser = subparsers.add_parser("markdone")
mark_done_parser.add_argument("id", nargs=1)
mark_done_parser.set_defaults(func = mark_done_action)


mark_progress_parser = subparsers.add_parser("mark-in-progress")
mark_progress_parser.add_argument("id", nargs=1)
mark_progress_parser.set_defaults(func = mark_progress_action)

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id", nargs=1)
delete_parser.set_defaults(func = delete_action)



load_tasks()
while True:
    command = input("> ")
    if command == "quit":
        break
    args = parser.parse_args(shlex.split(command))
    args.func(args)





